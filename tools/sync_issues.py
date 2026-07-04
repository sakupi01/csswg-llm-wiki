#!/usr/bin/env python3
"""Mirror GitHub issues (and bot-commented PRs) into raw/data/github/<repo>/.

Strategy (see AGENTS.md "Tools"):
- Issues:   GET /repos/{repo}/issues?state=all&sort=updated&direction=asc&since=<cursor>
- Comments: GET /repos/{repo}/issues/comments?sort=updated&direction=asc&since=<cursor>
  (repo-level endpoint: ~100 comments/request instead of 1 request/issue)

Cursors are persisted to .sync-state.json after every page, so an interrupted
run resumes where it left off. Files are rewritten whole from an in-file store
(frontmatter + sentinel-delimited comments), so reruns are idempotent.

PRs: skipped unless they carry css-meeting-bot comments; those are fetched
individually at the end and stored under pulls/.

Intentionally dropped: reactions, edit history, label-change events.
Deleted comments are not detected (updated_at based sync).
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_DEFAULT = "w3c/csswg-drafts"
ROOT = Path(__file__).resolve().parent.parent
BOT = "css-meeting-bot"
EPOCH = "1970-01-01T00:00:00Z"
PER_PAGE = 100

SENTINEL_RE = re.compile(
    r"^<!-- comment id=(\d+) author=(\S+) created=(\S+) url=(\S+?)( resolution=true)? -->$",
    re.M,
)
RESOLVED_RE = re.compile(r"^\s*(?:[*-]\s*)?`?(?:RESOLVED|RESOLUTION):\s*.+", re.M)


def log(msg: str) -> None:
    print(f"[sync_issues] {msg}", flush=True)


def gh_api(path: str, tries: int = 5) -> list | dict:
    """GET via `gh api` with backoff on secondary rate limits."""
    for attempt in range(tries):
        proc = subprocess.run(
            ["gh", "api", "--method", "GET", path],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            return json.loads(proc.stdout)
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


def paged(repo: str, endpoint: str, cursor: str):
    """Yield (page_items, new_cursor). since-cursor advance, page fallback."""
    page = 1
    while True:
        path = (
            f"/repos/{repo}/{endpoint}?sort=updated&direction=asc"
            f"&since={cursor}&per_page={PER_PAGE}&page={page}"
        )
        if endpoint == "issues":
            path += "&state=all"
        items = gh_api(path)
        if not items:
            return
        newest = max(i["updated_at"] for i in items)
        if newest == cursor and len(items) == PER_PAGE:
            page += 1  # pathological: a full page with identical timestamps
        else:
            cursor = newest
            page = 1
        yield items, cursor
        if len(items) < PER_PAGE:
            return


def sync(repo: str, full: bool, dry_run: bool) -> None:
    state = load_state(repo)
    if full:
        state["issues_cursor"] = EPOCH
        state["comments_cursor"] = EPOCH

    n_issues = n_comments = n_dropped = 0
    bot_pr_numbers: set[int] = set()
    pr_numbers: set[int] = set(state["pr_numbers"])

    log(f"issues since {state['issues_cursor']}")
    for items, cursor in paged(repo, "issues", state["issues_cursor"]):
        for item in items:
            if "pull_request" in item:
                pr_numbers.add(item["number"])
                continue  # PRs mirrored below, only if bot-commented
            if not dry_run:
                write_item(repo, item, "issues")
            n_issues += 1
        state["issues_cursor"] = cursor
        state["pr_numbers"] = sorted(pr_numbers)
        if not dry_run:
            save_state(repo, state)
        log(f"  issues: +{len(items)} (total {n_issues}, cursor {cursor})")

    log(f"comments since {state['comments_cursor']}")
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
        state["comments_cursor"] = cursor
        state["pr_numbers"] = sorted(pr_numbers)
        if not dry_run:
            save_state(repo, state)
        log(f"  comments: +{len(items)} (total {n_comments}, cursor {cursor})")

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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=REPO_DEFAULT)
    ap.add_argument("--full", action="store_true", help="reset cursors, remirror all")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    (data_dir(args.repo) / "issues").mkdir(parents=True, exist_ok=True)
    (data_dir(args.repo) / "pulls").mkdir(parents=True, exist_ok=True)
    try:
        sync(args.repo, args.full, args.dry_run)
    except KeyboardInterrupt:
        log("interrupted; cursors saved, rerun to resume")
        sys.exit(130)


if __name__ == "__main__":
    main()
