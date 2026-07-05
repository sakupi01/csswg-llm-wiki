#!/usr/bin/env python3
"""Gather the week's digest candidates from local data — NO GitHub API calls.

Everything the weekly digest needs is already mirrored and indexed by the
Thursday sync, so this is a deterministic read over `_generated/` + the mirror.
The LLM `/digest` step consumes the output; it must not invent items beyond it.

Output: _generated/digest-candidates/<until>.json (structured, every item has a
permalink) and .md (human-readable). Sections:
- resolutions   : bot RESOLVED lines dated in the window, tagged with the wiki
                  feature page whose spec labels match (if any). Each carries the
                  discussion substance so the digest can explain *why*, not just
                  *what*: `background` (issue body opener), `related` (issues the
                  body references — links the digest may cite), `irc` (verbatim
                  IRC log from the bot comment; the LLM summarises it, never the
                  tool — keeps facts traceable).
- agenda        : issues currently labeled Agenda+/Needs Edits with window activity
- hot           : issues/PRs with >=5 comments dated in the window, plus `recent`
                  (the window's last human comments — author + one-line gist)
- notable       : HIGH_INTEREST_LABELS threads with window activity below the hot bar
                  — a recall aid so quiet-but-developer-notable items reach the digest
- fresh         : high-interest / important issues newly opened in the window (new
                  proposals), with `background`+`related`
- spec_changes  : specs whose latest TR version date falls in the window
- deep          : MONTHLY only (`--month YYYY-MM`) — the month's busiest threads,
                  each with a full in-window comment ledger (author/date/gist +
                  permalink). This is the case-C material: the monthly digest reads
                  the mirror threads directly, and because every ledger URL is in
                  the pack, build_feed's link gate still holds.

Weekly window = (until-days, until]; monthly window = the calendar month.
Output stem is <until> for weeklies, <YYYY-MM> for monthlies (`span` marks which).
"""

import argparse
import html
import json
import re
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "_generated"
GITHUB = ROOT / "raw" / "data" / "github"
W3C = ROOT / "raw" / "data" / "w3c-api" / "specifications"
OUT = GEN / "digest-candidates"
IMPORTANT_LABELS = {"Agenda+", "Agenda+ F2F", "Needs Edits", "Needs Testcase (WPT)"}
# Developer-high-interest surfaces (a RECALL AID for `notable`/`fresh`, NOT the
# selector — the digest still weights editorially by the mozaic lens in AGENTS.md).
# Quiet-but-notable threads here (below the hot bar) would otherwise be dropped.
HIGH_INTEREST_LABELS = {
    "css-anchor-position-1", "css-forms-1", "css-view-transitions-1",
    "css-view-transitions-2", "css-contain-3", "scroll-animations-1",
    "animation-triggers-1", "css-grid-3", "css-pseudo-4", "css-nesting-1",
    "css-values-5", "css-gaps-1", "css-ui-4", "css-ui-5", "css-inline-3",
    "web-animations-2", "css-color-5", "css-mixins-1", "css-link-params-1",
}
HOT_COMMENT_THRESHOLD = 5
NOTABLE_MIN_COMMENTS = 1    # high-interest threads with >=this window activity (below hot)
FRESH_CAP = 20             # newly-opened high-interest issues surfaced per pack
IRC_MAX_LINES = 60          # cap verbatim log so the pack stays lean
RECENT_COMMENTS = 3         # human comments surfaced per hot issue
DEEP_TOP_N = 15             # monthly: threads that get a full comment ledger

SENTINEL_RE = re.compile(
    r"^<!-- comment id=(\d+) author=(\S+) created=(\S+) url=(\S+?)( resolution=true)? -->$",
    re.M,
)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n(.*)\Z", re.S)
IRC_RE = re.compile(r"<details>.*?full IRC log.*?</summary>(.*?)</details>", re.S | re.I)


def load_jsonl(name: str) -> list:
    p = GEN / name
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def spec_label_to_feature() -> dict:
    """Map a spec github_label -> feature slug, via each feature's `specs` list
    and each spec page's github_label."""
    spec_to_label = {}
    for f in (ROOT / "wiki" / "specs").glob("*.md"):
        head = f.read_text().split("\n---", 1)[0]
        gh = re.search(r"^github_label:\s*(\S+)", head, re.M)
        if gh:
            spec_to_label[f.stem] = gh.group(1).strip()
    label_to_feature = {}
    for f in (ROOT / "wiki" / "features").glob("*.md"):
        head = f.read_text().split("\n---", 1)[0]
        slug = re.search(r"^slug:\s*(\S+)", head, re.M)
        specs = re.search(r"^specs:\s*\[(.*?)\]", head, re.M)
        if not (slug and specs):
            continue
        for spec in (s.strip() for s in specs.group(1).split(",") if s.strip()):
            label = spec_to_label.get(spec, spec)
            label_to_feature[label] = slug.group(1).strip()
    return label_to_feature


def mirror_index() -> dict:
    """{issue_number: path} over every mirrored issue/PR file."""
    idx = {}
    for path in list(GITHUB.glob("*/issues/*/*.md")) + list(GITHUB.glob("*/pulls/*/*.md")):
        idx[int(path.stem)] = path
    return idx


_PARSE_CACHE = {}


def parse_mirror(path: Path) -> tuple:
    """(body, comments) where body is text before the first comment and each
    comment is {id, author, created, url, resolution, block}. Cached per path."""
    if path in _PARSE_CACHE:
        return _PARSE_CACHE[path]
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    content = m.group(1) if m else text
    sentinels = list(SENTINEL_RE.finditer(content))
    body = (content[: sentinels[0].start()] if sentinels else content).strip()
    comments = []
    for i, sm in enumerate(sentinels):
        end = sentinels[i + 1].start() if i + 1 < len(sentinels) else len(content)
        cid, author, created, url, res = sm.groups()
        comments.append({"id": cid, "author": author, "created": created,
                         "url": url, "resolution": bool(res),
                         "block": content[sm.end():end]})
    _PARSE_CACHE[path] = (body, comments)
    return body, comments


def first_para(body: str, limit: int = 400) -> str:
    """First real paragraph of the issue body (background), collapsed to one line."""
    for para in re.split(r"\n\s*\n", body):
        p = re.sub(r"\s+", " ", para.strip())
        if p and not p.startswith(("<!--", "#", ">", "```")):
            return p[:limit]
    return ""


def first_line(block: str, limit: int = 200) -> str:
    """First substantive line of a comment (skip the `## @author` header, quotes)."""
    for ln in block.splitlines():
        s = re.sub(r"\s+", " ", ln.strip())
        if not s or s.startswith(("## @", ">", "<!--", "<details", "```", "|")):
            continue
        return s[:limit]
    return ""


def related_refs(body: str, self_n: int) -> list:
    """Issues the body references (#N or a csswg-drafts URL) — background the
    digest may link. URLs land in the pack so build_feed's gate allows them."""
    nums = {int(m.group(1)) for m in re.finditer(r"#(\d{3,6})\b", body)}
    nums |= {int(m.group(1))
             for m in re.finditer(r"github\.com/w3c/csswg-drafts/(?:issues|pull)/(\d+)", body)}
    nums.discard(self_n)
    return [{"issue": n, "url": f"https://github.com/w3c/csswg-drafts/issues/{n}"}
            for n in sorted(nums)][:6]


def extract_irc(block: str) -> list:
    """Verbatim IRC discussion lines from a bot resolution comment's <details>."""
    m = IRC_RE.search(block)
    if not m:
        return []
    lines = [html.unescape(ln).strip() for ln in m.group(1).split("<br>")]
    lines = [ln for ln in lines if ln][:IRC_MAX_LINES]
    return lines


def scan_comment_activity(mirror: dict, since: str, until: str) -> dict:
    """{issue_number: comment_count_in_window} from mirror sentinels."""
    counts = defaultdict(int)
    for n, path in mirror.items():
        for c in parse_mirror(path)[1]:
            if since <= c["created"][:10] <= until:
                counts[n] += 1
    return counts


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--until", default=None, help="YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--month", default=None,
                    help="YYYY-MM: build the deeper monthly pack (adds `deep` "
                         "comment ledgers; overrides --days/--until)")
    args = ap.parse_args()

    if args.month:
        y, mo = (int(x) for x in args.month.split("-"))
        since = f"{args.month}-01"
        until = (date(y + (mo == 12), mo % 12 + 1, 1) - timedelta(days=1)).isoformat()
        span, out_stem = "month", args.month
    else:
        until = args.until or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        since = (datetime.strptime(until, "%Y-%m-%d") - timedelta(days=args.days)).strftime("%Y-%m-%d")
        span, out_stem = "week", until
    l2f = spec_label_to_feature()
    mirror = mirror_index()

    # resolutions in window (bot only — official minutes), enriched with the
    # discussion behind each: background, related issues, verbatim IRC log.
    resolutions = []
    for r in load_jsonl("resolutions-index.jsonl"):
        if r.get("source") != "bot" or not (since < (r.get("date") or "") <= until):
            continue
        feature = next((l2f[l] for l in r.get("labels", []) if l in l2f), None)
        item = {"date": r["date"], "issue": r["issue"], "labels": r.get("labels", []),
                "resolution": r["resolution"], "url": r["comment_url"], "feature": feature,
                "background": "", "related": [], "irc": []}
        path = mirror.get(r["issue"])
        if path:
            body, comments = parse_mirror(path)
            item["background"] = first_para(body)
            item["related"] = related_refs(body, r["issue"])
            cid = re.search(r"issuecomment-(\d+)", r["comment_url"] or "")
            cid = cid.group(1) if cid else None
            item["irc"] = next((extract_irc(c["block"]) for c in comments if c["id"] == cid), [])
        resolutions.append(item)

    issues = {r["number"]: r for r in load_jsonl("issues-index.jsonl")}
    activity = scan_comment_activity(mirror, since, until)

    # agenda: important-labeled issues created or commented in the window
    agenda = []
    for n, r in issues.items():
        if not (IMPORTANT_LABELS & set(r["labels"])):
            continue
        if since < (r.get("created_at") or "")[:10] <= until or activity.get(n, 0):
            feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
            agenda.append({"issue": n, "title": r["title"], "labels": r["labels"],
                           "url": r["url"], "feature": feature,
                           "comments_in_window": activity.get(n, 0)})

    def window_recent(n: int) -> list:
        """The window's last human comments on issue n (author + one-line gist)."""
        out = [{"author": cm["author"], "date": cm["created"][:10], "url": cm["url"],
                "gist": first_line(cm["block"])}
               for cm in (parse_mirror(mirror[n])[1] if n in mirror else [])
               if since <= cm["created"][:10] <= until and cm["author"] != "css-meeting-bot"]
        return out[-RECENT_COMMENTS:]

    # hot: >= threshold comments in the window, with the window's recent human voices
    hot = []
    for n, c in sorted(activity.items(), key=lambda kv: -kv[1]):
        if c < HOT_COMMENT_THRESHOLD or n not in issues:
            continue
        r = issues[n]
        feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
        hot.append({"issue": n, "title": r["title"], "labels": r["labels"],
                    "url": r["url"], "comments_in_window": c, "feature": feature,
                    "recent": window_recent(n)})

    # notable: high-interest surfaces with window activity BELOW the hot bar — a
    # recall aid so quiet-but-developer-notable threads reach the digest. The mozaic
    # lens (AGENTS.md), not comment count, decides what actually gets written up.
    hot_nums = {h["issue"] for h in hot}
    notable = []
    for n, c in sorted(activity.items(), key=lambda kv: -kv[1]):
        if n in hot_nums or n not in issues or c < NOTABLE_MIN_COMMENTS:
            continue
        r = issues[n]
        if not (HIGH_INTEREST_LABELS & set(r["labels"])):
            continue
        feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
        notable.append({"issue": n, "title": r["title"], "labels": r["labels"],
                        "url": r["url"], "comments_in_window": c, "feature": feature,
                        "recent": window_recent(n)})

    # fresh: high-interest / important-labeled issues newly OPENED in the window —
    # new proposals & requests that carry no discussion yet but may be mozaic-worthy.
    fresh = []
    for n, r in issues.items():
        if not (since < (r.get("created_at") or "")[:10] <= until):
            continue
        if not ((HIGH_INTEREST_LABELS | IMPORTANT_LABELS) & set(r["labels"])):
            continue
        feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
        body = parse_mirror(mirror[n])[0] if n in mirror else ""
        fresh.append({"issue": n, "title": r["title"], "labels": r["labels"], "url": r["url"],
                      "feature": feature, "created_at": (r.get("created_at") or "")[:10],
                      "background": first_para(body), "related": related_refs(body, n)})
    fresh = sorted(fresh, key=lambda x: x["created_at"], reverse=True)[:FRESH_CAP]

    # deep (monthly only): the busiest threads UNION the quiet high-interest ones get
    # a FULL in-window comment ledger, so the digest can trace an argument across the
    # month and cite any turn. Every ledger URL lands in the pack, so build_feed's
    # link gate stays satisfied even though the monthly digest (case-C) reads the
    # mirror threads directly.
    deep = []
    if span == "month":
        resolved = {r["issue"] for r in resolutions}
        loud = sorted((n for n, c in activity.items() if n in issues and c >= HOT_COMMENT_THRESHOLD),
                      key=lambda n: -activity[n])[:DEEP_TOP_N]
        # give a ledger only to quiet high-interest threads active enough to warrant one
        quiet_hi = [h["issue"] for h in notable if h["comments_in_window"] >= 3]
        for n in list(dict.fromkeys(loud + quiet_hi))[:DEEP_TOP_N * 2]:
            r = issues[n]
            feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
            ledger = [{"author": cm["author"], "date": cm["created"][:10], "url": cm["url"],
                       "resolution": cm["resolution"], "gist": first_line(cm["block"])}
                      for cm in parse_mirror(mirror[n])[1]
                      if since <= cm["created"][:10] <= until]
            deep.append({"issue": n, "title": r["title"], "labels": r["labels"], "url": r["url"],
                         "feature": feature, "comments_in_window": activity[n],
                         "resolved": n in resolved, "ledger": ledger})

    # spec status changes: latest TR version dated in the window
    spec_changes = []
    for f in sorted(W3C.glob("*.json")):
        spec = json.loads(f.read_text())
        vs = spec.get("versions") or []
        if vs and since < (vs[-1].get("date") or "") <= until:
            spec_changes.append({"shortname": spec["shortname"], "title": spec.get("title"),
                                 "maturity": vs[-1].get("maturity"), "date": vs[-1].get("date"),
                                 "url": vs[-1].get("uri")})

    pack = {"span": span, "since": since, "until": until,
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "resolutions": sorted(resolutions, key=lambda r: (r["date"], r["issue"])),
            "agenda": sorted(agenda, key=lambda a: -a["comments_in_window"]),
            "hot": hot, "notable": notable, "fresh": fresh, "spec_changes": spec_changes}
    if span == "month":
        pack["month"] = args.month
        pack["deep"] = deep

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{out_stem}.json").write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n")
    render_md(pack).write_to(OUT / f"{out_stem}.md")
    print(f"[digest_candidates] {span} {since}..{until}: {len(resolutions)} resolutions, "
          f"{len(agenda)} agenda, {len(hot)} hot, {len(notable)} notable, {len(fresh)} fresh, "
          f"{len(deep)} deep, {len(spec_changes)} spec changes -> {OUT}/{out_stem}.{{json,md}}")


class render_md:
    """Small helper so main() reads top-down; produces the human-readable pack."""

    def __init__(self, pack: dict):
        self.pack = pack

    def write_to(self, path: Path) -> None:
        p = self.pack
        kind = "Monthly digest" if p.get("span") == "month" else "Digest"
        L = [f"# {kind} candidates {p['since']}..{p['until']}",
             f"generated_at: {p['generated_at']}", ""]
        L.append(f"## Resolutions ({len(p['resolutions'])})")
        for r in p["resolutions"]:
            feat = f" -> [[{r['feature']}]]" if r["feature"] else ""
            L.append(f"- {r['date']} #{r['issue']} [{','.join(r['labels']) or '-'}]{feat}\n"
                     f"  RESOLVED: {r['resolution']}\n  {r['url']}")
            if r["background"]:
                L.append(f"  background: {r['background']}")
            if r["related"]:
                L.append(f"  related: {', '.join('#%d %s' % (x['issue'], x['url']) for x in r['related'])}")
            if r["irc"]:
                L.append(f"  irc ({len(r['irc'])} lines):")
                L.extend(f"    | {ln}" for ln in r["irc"])
        L.append(f"\n## Agenda+ / Needs Edits ({len(p['agenda'])})")
        for a in p["agenda"]:
            feat = f" -> [[{a['feature']}]]" if a["feature"] else ""
            L.append(f"- #{a['issue']} {a['title']}{feat} ({a['comments_in_window']} comments) {a['url']}")
        L.append(f"\n## Hot discussions ({len(p['hot'])})")
        for h in p["hot"]:
            feat = f" -> [[{h['feature']}]]" if h["feature"] else ""
            L.append(f"- #{h['issue']} {h['title']}{feat} ({h['comments_in_window']} comments) {h['url']}")
            for c in h["recent"]:
                L.append(f"    @{c['author']} ({c['date']}): {c['gist']}")
        L.append(f"\n## Notable (high-interest, below hot bar) ({len(p.get('notable', []))})")
        for h in p.get("notable", []):
            feat = f" -> [[{h['feature']}]]" if h["feature"] else ""
            L.append(f"- #{h['issue']} {h['title']}{feat} ({h['comments_in_window']} comments) {h['url']}")
            for c in h["recent"]:
                L.append(f"    @{c['author']} ({c['date']}): {c['gist']}")
        L.append(f"\n## Fresh (opened in window) ({len(p.get('fresh', []))})")
        for fr in p.get("fresh", []):
            feat = f" -> [[{fr['feature']}]]" if fr["feature"] else ""
            L.append(f"- #{fr['issue']} {fr['title']}{feat} (opened {fr['created_at']}) {fr['url']}")
            if fr["background"]:
                L.append(f"    background: {fr['background']}")
            if fr["related"]:
                L.append(f"    related: {', '.join('#%d %s' % (x['issue'], x['url']) for x in fr['related'])}")
        if p.get("deep"):
            L.append(f"\n## Deep threads — full ledger ({len(p['deep'])})")
            for d in p["deep"]:
                feat = f" -> [[{d['feature']}]]" if d["feature"] else ""
                flag = " [resolved]" if d["resolved"] else ""
                L.append(f"- #{d['issue']} {d['title']}{feat}{flag} "
                         f"({d['comments_in_window']} comments) {d['url']}")
                for c in d["ledger"]:
                    mark = " RESOLVED" if c["resolution"] else ""
                    L.append(f"    @{c['author']} ({c['date']}){mark}: {c['gist']}\n      {c['url']}")
        L.append(f"\n## Spec status changes ({len(p['spec_changes'])})")
        for s in p["spec_changes"]:
            L.append(f"- {s['shortname']} -> {s['maturity']} ({s['date']}) {s['url']}")
        path.write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
