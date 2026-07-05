#!/usr/bin/env python3
"""Mirror messages from the public www-style archive (lists.w3.org) into
raw/data/www-style/<YYYYMon>/<NNNN>.md, 1:1 with the archive URLs.

What the archive actually looks like (measured 2026-07):
- Month indexes are single pages even at peak volume (834 msgs); message
  numbers are 4-digit, zero-based, WITH GAPS — enumerate links, never ranges.
- Machine-readable metadata lives in Hypermail 3.0 HTML comments
  (<!-- isosent=... name=... subject=... id=... inreplyto=... charset=... -->);
  In-Reply-To exists ONLY there. Values are entity-obfuscated (html.unescape).
  1995-era pages lack some of these — parse defensively.
- No charset in the HTTP header; decode per-page from <meta charset>
  (ISO-8859-1 pages exist). Bodies are <pre class="body"> (two variants,
  multipart = several parts); rare HTML-only mails get tag-stripped fallback.
- robots.txt allows /Archives/Public/ (only */mboxes/ is disallowed).

Politeness: 1 req/s, contact UA, Retry-After honored, existing files are never
touched (the archive is immutable). Email addresses are NOT republished:
`from` keeps the display name only.

Modes:
  --minutes            [CSSWG] Minutes/Resolutions mails, 2008Jan..2017Jun by
                       default (bot comments duplicate minutes after 2017-04)
  --month 2015Feb      one whole month
  --all                everything since 1995May (~28h; run locally, never CI)
  --incremental        current+previous month; NO-OP until --all has been run
  --dry-run            report what would be fetched

Per-month sidecar .messages.jsonl (rebuilt from local files whenever a month
is touched) is the only thing build_indexes.py reads — not the 90k mirror files.
"""

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://lists.w3.org/Archives/Public/www-style/"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "raw" / "data" / "www-style"
STATE_PATH = OUT / ".scrape-state.json"
UA = "csswg-llm-wiki-mirror/1.0 (archival; contact: https://github.com/sakupi01/csswg-llm-wiki/issues)"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
FIRST_MONTH = (1995, 5)

MINUTES_RE = re.compile(r"^\[CSSWG\]\s+(?:Minutes|Resolutions)\b", re.I)
LINK_RE = re.compile(r'<a\b[^>]*?href="(\d{4})\.html"[^>]*>(.*?)</a>', re.S)
COMMENT_RE = re.compile(r'<!--\s*([a-z]+)="([^"]*)"\s*-->')
CHARSET_RE = re.compile(rb'<meta[^>]+charset=["\']?([A-Za-z0-9_-]+)', re.I)
PRE_BODY_RE = re.compile(r'<pre[^>]*class="body"[^>]*>(.*?)</pre>', re.S)
TAG_RE = re.compile(r"<[^>]+>")

_last_request = 0.0


def log(msg: str) -> None:
    print(f"[scrape_www_style] {msg}", flush=True)


def fetch(url: str, tries: int = 5) -> bytes | None:
    """Throttled GET. Returns None on 404."""
    global _last_request
    for attempt in range(tries):
        wait = 1.0 - (time.monotonic() - _last_request)
        if wait > 0:
            time.sleep(wait)
        _last_request = time.monotonic()
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            retry_after = e.headers.get("Retry-After")
            pause = int(retry_after) if (retry_after or "").isdigit() else 30 * (attempt + 1)
            log(f"HTTP {e.code} on {url}; waiting {pause}s")
            time.sleep(pause)
        except urllib.error.URLError as e:
            pause = 30 * (attempt + 1)
            log(f"{e}; waiting {pause}s")
            time.sleep(pause)
    raise RuntimeError(f"failed after {tries} tries: {url}")


def decode(raw: bytes) -> str:
    m = CHARSET_RE.search(raw[:2048])
    charset = m.group(1).decode("ascii", "replace") if m else "utf-8"
    try:
        return raw.decode(charset, errors="replace")
    except LookupError:
        return raw.decode("utf-8", errors="replace")


def month_name(year: int, month: int) -> str:
    return f"{year}{MONTHS[month - 1]}"


def month_range(start: str, end: str) -> list[str]:
    def parse(s: str) -> tuple[int, int]:
        return int(s[:4]), MONTHS.index(s[4:]) + 1

    (y, m), (ey, em) = parse(start), parse(end)
    out = []
    while (y, m) <= (ey, em):
        out.append(month_name(y, m))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def strip_tags(fragment: str) -> str:
    text = TAG_RE.sub("", fragment)
    text = html.unescape(text)
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_index(month: str) -> list[tuple[str, str]] | None:
    """[(nnnn, subject), ...] from the month's date-view index; None if no month."""
    raw = fetch(f"{BASE}{month}/")
    if raw is None:
        return None
    seen: dict[str, str] = {}
    for nnnn, inner in LINK_RE.findall(decode(raw)):
        if nnnn not in seen:
            subject = " ".join(strip_tags(inner).split())
            seen[nnnn] = subject
    return sorted(seen.items())


def parse_message(url: str, raw: bytes) -> dict:
    page = decode(raw)
    meta = {}
    for key, value in COMMENT_RE.findall(page):
        if key not in meta and value:
            meta[key] = html.unescape(value)

    name = meta.get("name", "")
    if "@" in name:  # 1995-era pages put the address in name=; do not republish
        name = name.split("@", 1)[0] + "@…"

    date = None
    for key in ("isosent", "isoreceived"):
        v = meta.get(key, "")
        if re.fullmatch(r"\d{14}", v):
            date = f"{v[:4]}-{v[4:6]}-{v[6:8]}T{v[8:10]}:{v[10:12]}:{v[12:14]}Z"
            break

    parts = PRE_BODY_RE.findall(page)
    if parts:
        body = "\n\n".join(strip_tags(p).strip("\n") for p in parts)
        body_format = "text"
    else:
        m = re.search(r'<section class="message-body-part">(.*?)</section>', page, re.S)
        body = strip_tags(m.group(1) if m else page).strip("\n")
        body_format = "html"

    return {
        "subject": meta.get("subject") or "",
        "from": name,
        "date": date,
        "message_id": meta.get("id") or None,
        "in_reply_to": meta.get("inreplyto") or None,
        "archived_at": url,
        "charset": meta.get("charset") or None,
        "body_format": body_format,
        "body": body,
    }


def write_message(month: str, nnnn: str, msg: dict) -> None:
    path = OUT / month / f"{nnnn}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = ["subject", "from", "date", "message_id", "in_reply_to",
            "archived_at", "charset", "body_format", "scraped_at"]
    msg = dict(msg)
    msg["scraped_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fm = "\n".join(f"{k}: {json.dumps(msg.get(k))}" for k in keys)
    path.write_text(f"---\n{fm}\n---\n\n{msg['body'].rstrip()}\n")


def rebuild_sidecar(month: str) -> int:
    """Deterministic per-month index of locally mirrored messages."""
    mdir = OUT / month
    rows = []
    for f in sorted(mdir.glob("[0-9][0-9][0-9][0-9].md")):
        head = f.read_text().split("\n---\n", 1)[0]
        row = {"nnnn": f.stem}
        for line in head.splitlines():
            k, _, v = line.partition(":")
            if k in ("subject", "from", "date", "message_id", "in_reply_to", "archived_at"):
                row[k] = json.loads(v.strip())
        rows.append(row)
    (mdir / ".messages.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    )
    return len(rows)


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"months": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def process_month(month: str, state: dict, only_minutes: bool, dry_run: bool) -> tuple[int, int]:
    """Fetch (a subset of) one month. Returns (fetched, skipped_existing)."""
    entries = parse_index(month)
    if entries is None:
        log(f"{month}: no archive page")
        return 0, 0
    mstate = state["months"].setdefault(month, {})
    mstate["expected"] = [n for n, _ in entries]
    missing = set(mstate.get("missing", []))

    if only_minutes:
        wanted = [(n, s) for n, s in entries
                  if MINUTES_RE.match(s) and not re.match(r"(?i)^\s*re:", s)]
    else:
        wanted = entries

    fetched = skipped = 0
    for nnnn, subject in wanted:
        path = OUT / month / f"{nnnn}.md"
        if path.exists() or nnnn in missing:
            skipped += 1
            continue
        if dry_run:
            log(f"  would fetch {month}/{nnnn}: {subject[:70]}")
            fetched += 1
            continue
        url = f"{BASE}{month}/{nnnn}.html"
        raw = fetch(url)
        if raw is None:
            missing.add(nnnn)
            log(f"  404 {month}/{nnnn}")
            continue
        msg = parse_message(url, raw)
        if not msg["subject"]:
            msg["subject"] = subject
        write_message(month, nnnn, msg)
        fetched += 1

    mstate["missing"] = sorted(missing)
    if not dry_run:
        have = {f.stem for f in (OUT / month).glob("[0-9][0-9][0-9][0-9].md")} if (OUT / month).exists() else set()
        mstate["complete"] = set(mstate["expected"]) - missing <= have
        if fetched:
            rebuild_sidecar(month)
        save_state(state)
    return fetched, skipped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--minutes", action="store_true")
    mode.add_argument("--month")
    mode.add_argument("--all", action="store_true")
    mode.add_argument("--incremental", action="store_true")
    ap.add_argument("--from", dest="from_month", default="2008Jan")
    ap.add_argument("--to", dest="to_month", default="2017Jun")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = load_state()
    now = datetime.now(timezone.utc)
    if args.month:
        months, only_minutes = [args.month], False
    elif args.minutes:
        months, only_minutes = month_range(args.from_month, args.to_month), True
    elif args.all:
        months = month_range(month_name(*FIRST_MONTH), month_name(now.year, now.month))
        only_minutes = False
    else:  # --incremental
        if not any(m.get("complete") for m in state["months"].values()):
            log("no fully-mirrored months yet; --incremental is a no-op until --all")
            return
        prev = (now.year, now.month - 1) if now.month > 1 else (now.year - 1, 12)
        months = [month_name(*prev), month_name(now.year, now.month)]
        months = [m for m in months if not state["months"].get(m, {}).get("complete")
                  or m == month_name(now.year, now.month)]
        only_minutes = False

    total_f = total_s = 0
    for month in months:
        f, s = process_month(month, state, only_minutes, args.dry_run)
        total_f += f
        total_s += s
        if f:
            log(f"{month}: +{f} (skipped {s})")
    log(f"done: {total_f} fetched, {total_s} already mirrored")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("interrupted; state saved, rerun to resume")
        sys.exit(130)
