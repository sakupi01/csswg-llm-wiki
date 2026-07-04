#!/usr/bin/env python3
"""Snapshot CSSWG specification status history from the public W3C API.

- Lists deliverables via /groups/wg/css/specifications (paginated).
- For each spec, fetches /specifications/{shortname}/versions; the list carries
  only href+title, so each *unseen* version resource is fetched individually.
- Writes raw/data/w3c-api/specifications/<shortname>.json with a normalized
  `maturity` code per version and a `snapshot_at` stamp.
- Also snapshots the group's charters and participations (yearly is enough).

No auth required. Rate limit 6,000 req / 10 min; we sleep 0.15s per request.
"""

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.w3.org"
GROUP = "/groups/wg/css"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "raw" / "data" / "w3c-api"
UA = "csswg-llm-wiki sync (https://github.com/sakupi01/csswg-llm-wiki)"

# Verbatim W3C status string -> normalized code (chart ordinal in AGENTS.md).
MATURITY = {
    "Recommendation": "REC",
    "Proposed Recommendation": "PR",
    "Proposed Edited Recommendation": "PER",
    "Candidate Recommendation": "CR",
    "Candidate Recommendation Snapshot": "CR",
    "Candidate Recommendation Draft": "CRD",
    "Last Call Working Draft": "LCWD",
    "Working Draft": "WD",
    "First Public Working Draft": "FPWD",
    "Group Note": "NOTE",
    "Working Group Note": "NOTE",
    "Note": "NOTE",
    "Group Draft Note": "DNOTE",
    "Draft Note": "DNOTE",
    "Retired": "RETIRED",
    "Superseded Recommendation": "SUPERSEDED",
    "Discontinued Draft": "DISCONTINUED",
}


def log(msg: str) -> None:
    print(f"[sync_w3c] {msg}", flush=True)


def get(path_or_url: str, tries: int = 4) -> dict:
    url = path_or_url if path_or_url.startswith("http") else API + path_or_url
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(0.15)
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            wait = 30 * (attempt + 1)
            log(f"HTTP {e.code} on {url}; retry in {wait}s")
            time.sleep(wait)
        except urllib.error.URLError as e:
            wait = 30 * (attempt + 1)
            log(f"{e}; retry in {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"failed after {tries} tries: {url}")


def links(obj: dict, key: str) -> list:
    v = (obj.get("_links") or {}).get(key) or []
    return v if isinstance(v, list) else [v]


def paged(path: str, key: str):
    url = API + path + ("&" if "?" in path else "?") + "items=100"
    while url:
        obj = get(url)
        yield from links(obj, key)
        nxt = (obj.get("_links") or {}).get("next")
        url = nxt["href"] if nxt else None


def sync_spec(href: str) -> bool:
    """Fetch one spec's version history; return True if the file changed."""
    spec = get(href)
    shortname = spec["shortname"]
    out_path = OUT / "specifications" / f"{shortname}.json"
    existing = json.loads(out_path.read_text()) if out_path.exists() else {}
    known = {v["uri"] for v in existing.get("versions", [])}

    versions = list(existing.get("versions", []))
    for vlink in paged(f"/specifications/{shortname}/versions", "version-history"):
        v = get(vlink["href"])
        if v.get("uri") in known:
            continue
        status = v.get("status") or ""
        versions.append(
            {
                "date": v.get("date"),
                "status": status,
                "maturity": MATURITY.get(status, "OTHER"),
                "uri": v.get("uri"),
                "editor_draft": v.get("editor-draft"),
            }
        )
    versions.sort(key=lambda v: (v["date"] or "", v["uri"] or ""))

    doc = {
        "shortname": shortname,
        "title": spec.get("title"),
        "shortlink": spec.get("shortlink"),
        "series": (spec.get("series-version") or None) and spec.get("shortname"),
        "snapshot_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "versions": versions,
    }
    new_text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    if out_path.exists():
        old = json.loads(out_path.read_text())
        if old.get("versions") == versions:
            return False  # keep old snapshot_at; nothing new
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text)
    return True


def sync_group() -> None:
    gdir = OUT / "group" / "css"
    gdir.mkdir(parents=True, exist_ok=True)
    charters = [
        {"href": c["href"], "title": c.get("title")}
        for c in paged(f"{GROUP}/charters", "charters")
    ]
    participations = [
        {"title": p.get("title"), "href": p["href"]}
        for p in paged(f"{GROUP}/participations", "participations")
    ]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (gdir / "charters.json").write_text(
        json.dumps({"snapshot_at": stamp, "charters": charters}, indent=2) + "\n"
    )
    (gdir / "participants.json").write_text(
        json.dumps({"snapshot_at": stamp, "participations": participations}, indent=2) + "\n"
    )
    log(f"group: {len(charters)} charters, {len(participations)} participations")


def main() -> None:
    spec_links = list(paged(f"{GROUP}/specifications", "specifications"))
    log(f"{len(spec_links)} specifications listed for the CSS WG")
    changed = 0
    for i, s in enumerate(spec_links, 1):
        try:
            if sync_spec(s["href"]):
                changed += 1
        except Exception as e:  # keep going; report at the end
            log(f"ERROR on {s.get('href')}: {e}")
        if i % 25 == 0:
            log(f"  {i}/{len(spec_links)} specs…")
    sync_group()
    log(f"done: {changed} spec files updated")


if __name__ == "__main__":
    main()
    sys.exit(0)
