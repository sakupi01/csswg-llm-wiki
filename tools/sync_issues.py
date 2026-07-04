#!/usr/bin/env python3
"""Mirror GitHub issues (and bot-commented PRs) into raw/data/github/<repo>/.

Strategy (see AGENTS.md "Tools"; hard-won API quirks in paged()'s docstring):
- Incremental stream: GET /repos/{repo}/issues and /repos/{repo}/issues/comments
  with sort=created&direction=asc&since=<cursor> (created-order is the only
  stable listing order; `since` still filters by updated_at).
- Full/backfill integrity: --repair lists every item (fits the ~40k pagination
  cap) and refetches comments per-issue wherever the local comment count
  disagrees with the API's — the full comment history itself exceeds the cap.

Cursors persist to .sync-state.json at the end of each completed pass; reruns
are idempotent (files are rewritten whole from frontmatter + sentinels).

PRs: skipped unless they carry css-meeting-bot comments; those are stored
under pulls/.

Intentionally dropped: reactions, edit history, label-change events.
Deleted comments/issues are not detected (additive sync; see AGENTS.md).
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_DEFAULT = "w3c/csswg-drafts"
ROOT = Path(__file__).resolve().parent.parent
BOT = "css-meeting-bot"
# GitHub's /issues endpoint silently returns [] for a since= before ~2000;
# 2008-01-01 (pre-GitHub-founding) is safe for any repo.
EPOCH = "2008-01-01T00:00:00Z"
PER_PAGE = 100

SENTINEL_RE = re.compile(
    r"^<!-- comment id=(\d+) author=(\S+) created=(\S+) url=(\S+?)( resolution=true)? -->$",
    re.M,
)
RESOLVED_RE = re.compile(r"^\s*(?:[*-]\s*)?`?(?:RESOLVED|RESOLUTION):\s*.+", re.M)


def log(msg: str) -> None:
    print(f"[sync_issues] {msg}", flush=True)


def gh_api(path: str, tries: int = 8) -> list | dict:
    """GET via `gh api` with backoff on secondary rate limits."""
    for attempt in range(tries):
        proc = subprocess.run(
            ["gh", "api", "--method", "GET", path],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            return json.loads(proc.stdout)
        if "pagination is limited" in proc.stderr:
            raise RuntimeError(
                f"deep-pagination cap hit on {path} — window too large for the "
                "stream; run --repair to fill via per-issue fetches"
            )
        wait = min(60 * (attempt + 1), 300)
        log(f"gh api failed ({proc.stderr.strip()[:200]}); retry in {wait}s")
        time.sleep(wait)
    raise RuntimeError(f"gh api failed after {tries} tries: {path}")


def data_dir(repo: str) -> Path:
    return ROOT / "raw" / "data" / "github" / repo.split("/")[1]


def state_path(repo: str) -> Path:
    return data_dir(repo) / ".sync-state.json"


def load_state(repo: str) -> dict:
    p = state_path(repo)
    if p.exists():
        state = json.loads(p.read_text())
        state.setdefault("pr_numbers", [])
        return state
    return {
        "repo": repo,
        "issues_cursor": EPOCH,
        "comments_cursor": EPOCH,
        "pr_numbers": [],
    }


def save_state(repo: str, state: dict) -> None:
    state["last_run"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_path(repo).write_text(json.dumps(state, indent=2) + "\n")


def bucket(number: int) -> str:
    return f"{number // 1000:02d}xxx"


def issue_path(repo: str, number: int, kind: str = "issues") -> Path:
    return data_dir(repo) / kind / bucket(number) / f"{number:05d}.md"


def escape_body(body: str) -> str:
    """A body line matching the sentinel pattern would corrupt reparsing."""
    return re.sub(r"^<!-- comment ", "<!-- comment(escaped) ", body or "", flags=re.M)


# ---------------------------------------------------------------- file store


def parse_file(path: Path) -> dict | None:
    """Reparse an existing mirror file into {meta, body, comments}."""
    if not path.exists():
        return None
    text = path.read_text()
    m = re.match(r"\A---\n(.*?\n)---\n", text, re.S)
    if not m:
        return None
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = json.loads(v.strip()) if v.strip() else None
    rest = text[m.end():]
    parts = SENTINEL_RE.split(rest)
    body = parts[0].strip("\n")
    comments = {}
    # split() yields [pre, id, author, created, url, resflag, chunk, ...] per match
    for i in range(1, len(parts), 6):
        cid, author, created, url, _resflag, chunk = parts[i : i + 6]
        # chunk = "\n## @author — date\n(body)\n"
        body_lines = chunk.strip("\n").split("\n")
        cbody = "\n".join(body_lines[1:]).strip("\n") if body_lines else ""
        comments[int(cid)] = {
            "id": int(cid),
            "author": author,
            "created_at": created,
            "url": url,
            "body": cbody,
        }
    return {"meta": meta, "body": body, "comments": comments}


def render_file(meta: dict, body: str, comments: dict) -> str:
    ordered = sorted(comments.values(), key=lambda c: (c["created_at"], c["id"]))
    has_resolution = any(
        c["author"] == BOT and RESOLVED_RE.search(c["body"] or "") for c in ordered
    )
    meta = dict(meta)
    meta["comments"] = len(ordered)
    meta["has_resolution"] = has_resolution
    keys = [
        "number", "title", "state", "labels", "author",
        "created_at", "closed_at", "url", "comments", "has_resolution", "synced_at",
    ]
    fm = "\n".join(f"{k}: {json.dumps(meta.get(k))}" for k in keys)
    out = [f"---\n{fm}\n---", "", escape_body(body), ""]
    for c in ordered:
        res = " resolution=true" if (
            c["author"] == BOT and RESOLVED_RE.search(c["body"] or "")
        ) else ""
        day = c["created_at"][:10]
        out.append(
            f"<!-- comment id={c['id']} author={c['author']} "
            f"created={c['created_at']} url={c['url']}{res} -->"
        )
        out.append(f"## @{c['author']} — {day}")
        out.append("")
        out.append(escape_body(c["body"]))
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def write_item(repo: str, item: dict, kind: str) -> None:
    """Write/refresh one issue (or PR) from an API issue object, keeping comments."""
    number = item["number"]
    path = issue_path(repo, number, kind)
    existing = parse_file(path)
    comments = existing["comments"] if existing else {}
    meta = {
        "number": number,
        "title": item.get("title") or "",
        "state": item.get("state"),
        "labels": sorted(l["name"] for l in item.get("labels", [])),
        "author": (item.get("user") or {}).get("login", "ghost"),
        "created_at": item.get("created_at"),
        "closed_at": item.get("closed_at"),
        "url": item.get("html_url"),
        "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_file(meta, item.get("body") or "", comments))


def merge_comment(repo: str, number: int, comment: dict, kind: str) -> bool:
    """Merge one comment into an existing mirror file. False if file absent."""
    path = issue_path(repo, number, kind)
    existing = parse_file(path)
    if existing is None:
        return False
    existing["comments"][comment["id"]] = {
        "id": comment["id"],
        "author": (comment.get("user") or {}).get("login", "ghost"),
        "created_at": comment.get("created_at"),
        "url": comment.get("html_url"),
        "body": comment.get("body") or "",
    }
    path.write_text(render_file(existing["meta"], existing["body"], existing["comments"]))
    return True


# ------------------------------------------------------------------ streams


def minus_1s(ts: str) -> str:
    dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ") - timedelta(seconds=1)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def paged(repo: str, endpoint: str, since: str):
    """Yield (page_items, resume_cursor) for `since=<fixed>`, pages 1..N.

    Hard-won constraints (see memory/gotchas and git history):
    - sort=updated ordering is UNRELIABLE: pages contain occasional items whose
      displayed updated_at disagrees with the hidden sort key (an outlier months
      ahead can sit mid-page). Any since-re-anchoring scheme built on updated_at
      therefore skips items deterministically. Never re-anchor.
    - sort=created is stable (created_at is immutable), so a plain page walk has
      consistent boundaries. `since` still filters by updated_at, which is fine.
    - Deep pagination is capped server-side (~40k items, HTTP 422). The issues
      listing (~14k) fits; a full-history comments walk does NOT — full comment
      coverage comes from repair()'s per-issue fetches instead. This stream is
      for incremental windows only.

    resume_cursor = (max updated_at seen - 1s) is only safe to persist AFTER the
    pass completes: created-order ≠ updated-order, so mid-pass the unseen tail
    may still hold small updated_at values.
    """
    page = 1
    max_updated = since
    while True:
        path = (
            f"/repos/{repo}/{endpoint}?sort=created&direction=asc"
            f"&since={since}&per_page={PER_PAGE}&page={page}"
        )
        if endpoint == "issues":
            path += "&state=all"
        items = gh_api(path)
        if not items:
            return
        max_updated = max([max_updated] + [i["updated_at"] for i in items])
        yield items, minus_1s(max_updated)
        if len(items) < PER_PAGE:
            return
        page += 1


def sync(repo: str, full: bool, dry_run: bool) -> None:
    state = load_state(repo)
    if full:
        # Only the issues cursor resets: a full-history comments walk exceeds
        # the deep-pagination cap. Run --repair afterwards for comment gaps.
        state["issues_cursor"] = EPOCH

    n_issues = n_comments = n_dropped = 0
    bot_pr_numbers: set[int] = set()
    pr_numbers: set[int] = set(state["pr_numbers"])

    log(f"issues since {state['issues_cursor']}")
    issues_final = state["issues_cursor"]
    for items, cursor in paged(repo, "issues", state["issues_cursor"]):
        for item in items:
            if "pull_request" in item:
                pr_numbers.add(item["number"])
                continue  # PRs mirrored below, only if bot-commented
            if not dry_run:
                write_item(repo, item, "issues")
            n_issues += 1
        issues_final = cursor  # persist only after the pass completes (see paged)
        state["pr_numbers"] = sorted(pr_numbers)
        if not dry_run:
            save_state(repo, state)
        log(f"  issues: +{len(items)} (total {n_issues})")
    state["issues_cursor"] = issues_final
    if not dry_run:
        save_state(repo, state)

    log(f"comments since {state['comments_cursor']}")
    comments_final = state["comments_cursor"]
    for items, cursor in paged(repo, "issues/comments", state["comments_cursor"]):
        for c in items:
            number = int(c["issue_url"].rstrip("/").rsplit("/", 1)[1])
            author = (c.get("user") or {}).get("login")
            if dry_run:
                n_comments += 1
                continue
            if merge_comment(repo, number, c, "issues"):
                n_comments += 1
            elif merge_comment(repo, number, c, "pulls"):
                n_comments += 1
            elif author == BOT and number in pr_numbers:
                bot_pr_numbers.add(number)  # first bot comment on a skipped PR
            elif number in pr_numbers:
                n_dropped += 1  # non-bot comment on a skipped PR: intentional drop
            else:
                # unknown number: an issue created after the issues pass — fetch it
                item = gh_api(f"/repos/{repo}/issues/{number}")
                if "pull_request" in item:
                    pr_numbers.add(number)
                    if author == BOT:
                        bot_pr_numbers.add(number)
                    else:
                        n_dropped += 1
                else:
                    write_item(repo, item, "issues")
                    merge_comment(repo, number, c, "issues")
                    n_issues += 1
                    n_comments += 1
        comments_final = cursor  # persist only after the pass completes (see paged)
        state["pr_numbers"] = sorted(pr_numbers)
        if not dry_run:
            save_state(repo, state)
        log(f"  comments: +{len(items)} (total {n_comments})")
    state["comments_cursor"] = comments_final
    if not dry_run:
        save_state(repo, state)

    for number in sorted(bot_pr_numbers):
        item = gh_api(f"/repos/{repo}/issues/{number}")
        write_item(repo, item, "pulls")
        for c in gh_api(f"/repos/{repo}/issues/{number}/comments?per_page={PER_PAGE}"):
            merge_comment(repo, number, c, "pulls")
        n_comments += 1
        log(f"  bot PR mirrored: #{number}")

    log(
        f"done: {n_issues} issues touched, {n_comments} comments merged, "
        f"{len(bot_pr_numbers)} bot PRs, {n_dropped} skipped-PR comments dropped"
    )


def fetch_all_comments(repo: str, number: int) -> list:
    """Per-issue comments endpoint: created-order, stable — safe pagination."""
    out, page = [], 1
    while True:
        items = gh_api(f"/repos/{repo}/issues/{number}/comments?per_page={PER_PAGE}&page={page}")
        out += items
        if len(items) < PER_PAGE:
            return out
        page += 1


def repair(repo: str) -> None:
    """Verify mirror completeness against a fresh full listing; fix gaps.

    (a) missing issues (skipped by any past stream run) are written;
    (b) issue files whose local comment count != the listing's `comments`
        count get their comments refetched via the stable per-issue endpoint.
    Unmirrored PRs stay unmirrored (bot-PR detection is the stream's job);
    deleted comments still cannot be detected (local > API is refetched but
    stale comments are not removed — documented limitation).
    """
    state = load_state(repo)
    pr_numbers = set(state["pr_numbers"])
    listing: dict[int, dict] = {}
    log("repair: full listing pass")
    for items, _cursor in paged(repo, "issues", EPOCH):
        for item in items:
            listing[item["number"]] = item
    log(f"repair: {len(listing)} items listed")

    n_missing = n_refetched = 0
    for number, item in sorted(listing.items()):
        is_pr = "pull_request" in item
        if is_pr:
            pr_numbers.add(number)
        kind = "pulls" if is_pr else "issues"
        path = issue_path(repo, number, kind)
        existing = parse_file(path)
        if is_pr and existing is None:
            continue
        n_local = len(existing["comments"]) if existing else 0
        if existing is None:
            n_missing += 1
            log(f"  missing #{number} — mirrored")
        if existing is None or n_local != item.get("comments", 0):
            write_item(repo, item, kind)
            if item.get("comments", 0):
                for c in fetch_all_comments(repo, number):
                    merge_comment(repo, number, c, kind)
            if existing is not None:
                n_refetched += 1
    state["pr_numbers"] = sorted(pr_numbers)
    save_state(repo, state)
    log(f"repair done: {n_missing} missing mirrored, {n_refetched} comment sets refetched")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=REPO_DEFAULT)
    ap.add_argument("--full", action="store_true", help="reset cursors, remirror all")
    ap.add_argument("--repair", action="store_true", help="verify against a fresh listing, fix gaps")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    (data_dir(args.repo) / "issues").mkdir(parents=True, exist_ok=True)
    (data_dir(args.repo) / "pulls").mkdir(parents=True, exist_ok=True)
    try:
        if args.repair:
            repair(args.repo)
        else:
            sync(args.repo, args.full, args.dry_run)
    except KeyboardInterrupt:
        log("interrupted; cursors saved, rerun to resume")
        sys.exit(130)


if __name__ == "__main__":
    main()
