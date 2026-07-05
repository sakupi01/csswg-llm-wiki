#!/usr/bin/env python3
"""Build the RSS delivery from wiki/digests/*.md into docs/ (GitHub Pages). stdlib only.

Outputs docs/feed.xml (Atom 1.0), docs/feed.json (JSON Feed 1.1), docs/index.html.
One feed item per digest page (weekly `YYYY-Www` and monthly `YYYY-MM` alike).

Accuracy gate (mirrors R1/R4): every csswg-drafts / lists.w3.org / w3.org-TR link in
a digest body must appear in that digest's candidate pack. The pack is named by the
digest's `pack:` frontmatter field, else `<until>.json` (weekly default). A link that
isn't a gathered fact fails the build — the digest may select and explain, never
fabricate a source.
"""

import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "wiki" / "digests"
CANDIDATES = ROOT / "_generated" / "digest-candidates"
DOCS = ROOT / "docs"
SITE = "https://sakupi01.github.io/csswg-llm-wiki"
FEED_TITLE = "This week in CSSWG"
FEED_DESC = "Context-rich weekly and monthly digests of CSS Working Group discussions — an unofficial, LLM-maintained companion to the csswg-llm-wiki."

FM_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.S)
URL_RE = re.compile(r"https?://[^\s)\]<>\"']+")
# links whose facts must be traceable to the candidate pack
GATED_HOST_RE = re.compile(r"https?://(github\.com/w3c/|lists\.w3\.org/|www\.w3\.org/TR/)")


def parse_digest(path: Path) -> dict:
    m = FM_RE.match(path.read_text())
    if not m:
        raise ValueError(f"{path}: missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    meta["body"] = m.group(2).strip("\n")
    meta["path"] = path
    return meta


def validate_links(meta: dict) -> None:
    pack_name = meta.get("pack") or f"{meta.get('until')}.json"
    pack_path = CANDIDATES / pack_name
    if not pack_path.exists():
        raise SystemExit(f"[build_feed] {meta['path'].name}: no candidate pack {pack_name}")
    pack_text = pack_path.read_text()
    for url in URL_RE.findall(meta["body"]):
        if GATED_HOST_RE.match(url) and url.rstrip("/") not in pack_text:
            raise SystemExit(
                f"[build_feed] {meta['path'].name}: link not in candidate pack "
                f"(fabricated source?): {url}"
            )


# ---- minimal, self-contained markdown -> HTML (covers the /digest page format)
def md_to_html(md: str) -> str:
    """Render the subset used by digest/feature pages: h2/h3, ul with multi-line
    items, and paragraphs. Hard-wrapped continuation lines join their block."""
    out, items, para = [], [], []
    block = None  # None | "ul" | "p"

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                   lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        return s

    def flush():
        nonlocal block
        if block == "ul":
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            items.clear()
        elif block == "p" and para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        block = None

    for line in md.splitlines():
        if line.startswith(("## ", "### ")):
            flush()
            lvl, txt = ("h3", line[4:]) if line.startswith("### ") else ("h2", line[3:])
            out.append(f"<{lvl}>{inline(txt)}</{lvl}>")
        elif line.startswith("- "):
            if block != "ul":
                flush(); block = "ul"
            items.append(line[2:].strip())
        elif not line.strip():
            flush()
        elif line[0].isspace() and block == "ul" and items:
            items[-1] += " " + line.strip()  # continuation of the current <li>
        else:
            if block != "p":
                flush(); block = "p"
            para.append(line.strip())
    flush()
    return "\n".join(out)


def rfc3339(date_or_ts: str) -> str:
    if "T" in date_or_ts:
        return date_or_ts
    return f"{date_or_ts}T00:00:00Z"


def atom(items: list) -> str:
    updated = items[0]["generated_at"] if items else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    e = [f'<?xml version="1.0" encoding="utf-8"?>',
         '<feed xmlns="http://www.w3.org/2005/Atom">',
         f"<title>{html.escape(FEED_TITLE)}</title>",
         f"<subtitle>{html.escape(FEED_DESC)}</subtitle>",
         f'<link href="{SITE}/feed.xml" rel="self"/>',
         f'<link href="{SITE}/"/>',
         f"<id>{SITE}/</id>",
         f"<updated>{rfc3339(updated)}</updated>"]
    for it in items:
        e += [f"<entry>",
              f"<title>{html.escape(it['title'])}</title>",
              f'<link href="{it['url']}"/>',
              f"<id>{it['url']}</id>",
              f"<updated>{rfc3339(it['generated_at'])}</updated>",
              f"<published>{rfc3339(it['generated_at'])}</published>",
              f'<content type="html">{html.escape(it["html"])}</content>',
              "</entry>"]
    e.append("</feed>")
    return "\n".join(e) + "\n"


def json_feed(items: list) -> str:
    feed = {"version": "https://jsonfeed.org/version/1.1", "title": FEED_TITLE,
            "description": FEED_DESC, "home_page_url": f"{SITE}/",
            "feed_url": f"{SITE}/feed.json",
            "items": [{"id": it["url"], "url": it["url"], "title": it["title"],
                       "content_html": it["html"],
                       "date_published": rfc3339(it["generated_at"])} for it in items]}
    return json.dumps(feed, indent=2, ensure_ascii=False) + "\n"


def index_html(items: list) -> str:
    lis = "\n".join(
        f'<li><a href="{it["url"]}">{html.escape(it["title"])}</a> '
        f'<small>({it["since"]}–{it["until"]})</small></li>' for it in items)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{FEED_TITLE}</title>
<link rel="alternate" type="application/atom+xml" href="feed.xml" title="{FEED_TITLE}">
<link rel="alternate" type="application/feed+json" href="feed.json" title="{FEED_TITLE}">
<style>body{{max-width:42rem;margin:2rem auto;padding:0 1rem;font:16px/1.6 system-ui,sans-serif}}small{{color:#666}}</style>
</head><body>
<h1>{FEED_TITLE}</h1>
<p>{FEED_DESC}</p>
<p>Subscribe: <a href="feed.xml">Atom</a> · <a href="feed.json">JSON Feed</a></p>
<h2>Recent digests</h2>
<ul>
{lis}
</ul>
<p><small>Unofficial, LLM-maintained. Not a product of the CSS Working Group.
Source: <a href="https://github.com/sakupi01/csswg-llm-wiki">csswg-llm-wiki</a>.</small></p>
</body></html>
"""


def main() -> None:
    pages = sorted(DIGESTS.glob("*.md")) if DIGESTS.exists() else []
    if not pages:
        print("[build_feed] no digest pages yet"); return
    items = []
    for p in pages:
        meta = parse_digest(p)
        validate_links(meta)
        week = meta.get("week") or p.stem
        items.append({
            "title": meta.get("title") or f"This week in CSSWG ({meta.get('until')})",
            "url": f"{SITE}/digests/{week}.html",
            "since": meta.get("since"), "until": meta.get("until"),
            "generated_at": meta.get("generated_at") or rfc3339(meta.get("until", "")),
            "html": md_to_html(meta["body"]),
        })
    items.sort(key=lambda i: i["generated_at"], reverse=True)

    DOCS.mkdir(exist_ok=True)
    (DOCS / "digests").mkdir(exist_ok=True)
    (DOCS / "feed.xml").write_text(atom(items))
    (DOCS / "feed.json").write_text(json_feed(items))
    (DOCS / "index.html").write_text(index_html(items))
    for it in items:
        week = it["url"].rsplit("/", 1)[1]
        (DOCS / "digests" / week).write_text(
            f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(it["title"])}</title>'
            f'<style>body{{max-width:42rem;margin:2rem auto;padding:0 1rem;'
            f'font:16px/1.6 system-ui,sans-serif}}</style></head><body>'
            f'<p><a href="../">&larr; all digests</a></p>{it["html"]}</body></html>\n')
    print(f"[build_feed] {len(items)} digest(s) -> docs/{{feed.xml,feed.json,index.html}}")


if __name__ == "__main__":
    main()
