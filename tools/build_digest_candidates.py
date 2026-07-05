#!/usr/bin/env python3
"""Gather the week's digest candidates from local data — NO GitHub API calls.

Everything the weekly digest needs is already mirrored and indexed by the
Thursday sync, so this is a deterministic read over `_generated/` + the mirror.
The LLM `/digest` step consumes the output; it must not invent items beyond it.

Output: _generated/digest-candidates/<until>.json (structured, every item has a
permalink) and .md (human-readable). Sections:
- resolutions   : bot RESOLVED lines dated in the window, tagged with the wiki
                  feature page whose spec labels match (if any)
- agenda        : issues currently labeled Agenda+/Needs Edits with window activity
- hot           : issues/PRs with >=5 comments dated in the window
- spec_changes  : specs whose latest TR version date falls in the window

Window = [until-days, until], date strings compared lexicographically.
"""

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "_generated"
GITHUB = ROOT / "raw" / "data" / "github"
W3C = ROOT / "raw" / "data" / "w3c-api" / "specifications"
OUT = GEN / "digest-candidates"
IMPORTANT_LABELS = {"Agenda+", "Agenda+ F2F", "Needs Edits", "Needs Testcase (WPT)"}
HOT_COMMENT_THRESHOLD = 5

SENTINEL_RE = re.compile(
    r"^<!-- comment id=(\d+) author=(\S+) created=(\S+) url=(\S+?)( resolution=true)? -->$",
    re.M,
)


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


def scan_comment_activity(since: str, until: str) -> dict:
    """{issue_number: comment_count_in_window} from mirror sentinels."""
    counts = defaultdict(int)
    for path in list(GITHUB.glob("*/issues/*/*.md")) + list(GITHUB.glob("*/pulls/*/*.md")):
        text = path.read_text()
        for _id, _author, created, _url, _res in SENTINEL_RE.findall(text):
            if since <= created[:10] <= until:
                counts[int(path.stem)] += 1
    return counts


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--until", default=None, help="YYYY-MM-DD (default: today UTC)")
    args = ap.parse_args()

    until = args.until or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    since = (datetime.strptime(until, "%Y-%m-%d") - timedelta(days=args.days)).strftime("%Y-%m-%d")
    l2f = spec_label_to_feature()

    # resolutions in window (bot only — official minutes)
    resolutions = []
    for r in load_jsonl("resolutions-index.jsonl"):
        if r.get("source") != "bot" or not (since < (r.get("date") or "") <= until):
            continue
        feature = next((l2f[l] for l in r.get("labels", []) if l in l2f), None)
        resolutions.append(
            {"date": r["date"], "issue": r["issue"], "labels": r.get("labels", []),
             "resolution": r["resolution"], "url": r["comment_url"], "feature": feature}
        )

    issues = {r["number"]: r for r in load_jsonl("issues-index.jsonl")}
    activity = scan_comment_activity(since, until)

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

    # hot: >= threshold comments in the window
    hot = []
    for n, c in sorted(activity.items(), key=lambda kv: -kv[1]):
        if c < HOT_COMMENT_THRESHOLD or n not in issues:
            continue
        r = issues[n]
        feature = next((l2f[l] for l in r["labels"] if l in l2f), None)
        hot.append({"issue": n, "title": r["title"], "labels": r["labels"],
                    "url": r["url"], "comments_in_window": c, "feature": feature})

    # spec status changes: latest TR version dated in the window
    spec_changes = []
    for f in sorted(W3C.glob("*.json")):
        spec = json.loads(f.read_text())
        vs = spec.get("versions") or []
        if vs and since < (vs[-1].get("date") or "") <= until:
            spec_changes.append({"shortname": spec["shortname"], "title": spec.get("title"),
                                 "maturity": vs[-1].get("maturity"), "date": vs[-1].get("date"),
                                 "url": vs[-1].get("uri")})

    pack = {"since": since, "until": until,
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "resolutions": sorted(resolutions, key=lambda r: (r["date"], r["issue"])),
            "agenda": sorted(agenda, key=lambda a: -a["comments_in_window"]),
            "hot": hot, "spec_changes": spec_changes}

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{until}.json").write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n")
    render_md(pack).write_to(OUT / f"{until}.md")
    print(f"[digest_candidates] {since}..{until}: {len(resolutions)} resolutions, "
          f"{len(agenda)} agenda, {len(hot)} hot, {len(spec_changes)} spec changes "
          f"-> {OUT}/{until}.{{json,md}}")


class render_md:
    """Small helper so main() reads top-down; produces the human-readable pack."""

    def __init__(self, pack: dict):
        self.pack = pack

    def write_to(self, path: Path) -> None:
        p = self.pack
        L = [f"# Digest candidates {p['since']}..{p['until']}",
             f"generated_at: {p['generated_at']}", ""]
        L.append(f"## Resolutions ({len(p['resolutions'])})")
        for r in p["resolutions"]:
            feat = f" -> [[{r['feature']}]]" if r["feature"] else ""
            L.append(f"- {r['date']} #{r['issue']} [{','.join(r['labels']) or '-'}]{feat}\n"
                     f"  RESOLVED: {r['resolution']}\n  {r['url']}")
        L.append(f"\n## Agenda+ / Needs Edits ({len(p['agenda'])})")
        for a in p["agenda"]:
            feat = f" -> [[{a['feature']}]]" if a["feature"] else ""
            L.append(f"- #{a['issue']} {a['title']}{feat} ({a['comments_in_window']} comments) {a['url']}")
        L.append(f"\n## Hot discussions ({len(p['hot'])})")
        for h in p["hot"]:
            feat = f" -> [[{h['feature']}]]" if h["feature"] else ""
            L.append(f"- #{h['issue']} {h['title']}{feat} ({h['comments_in_window']} comments) {h['url']}")
        L.append(f"\n## Spec status changes ({len(p['spec_changes'])})")
        for s in p["spec_changes"]:
            L.append(f"- {s['shortname']} -> {s['maturity']} ({s['date']}) {s['url']}")
        path.write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
