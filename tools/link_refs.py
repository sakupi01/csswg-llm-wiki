#!/usr/bin/env python3
"""Auto-link referenceable entities in wiki prose. Idempotent; run at ingest and lint.

Three kinds of links are inserted:
- People: `@github`, github login, or IRC nick (length >= 4) -> wiki/people/<slug>.md
- Issue/PR numbers: `#<N>` -> https://github.com/w3c/csswg-drafts/issues/<N>
  (GitHub redirects /issues/<N> to the PR when <N> is a PR, so one form covers both)
- Qualified cross-repo refs: `<owner>/<name>#<N>` for the other mirrored repos
  (openui/open-ui, whatwg/html) -> that repo's issue URL

Conservative by design — never touches:
- YAML frontmatter, fenced code blocks, inline code, bare URLs, existing links
- blockquote lines (`>`), which hold verbatim IRC-minutes quotations

Note on verbatim (AGENTS.md R1): a RESOLVED quotation may gain a `#<N>` link in a
non-blockquote table cell. That wraps but does not alter the text — R1's verbatim
check strips markdown link syntax before comparing.

Bare `#<N>` scope is w3c/csswg-drafts. Houdini/FXTF/open-ui/whatwg issue numbers
would mislink as bare refs; always write them qualified (`openui/open-ui#<N>`).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from extract_people import load_people  # noqa: E402

DIRS = ["features", "specs", "families", "history", "meetings", "digests"]
ISSUES_URL = "https://github.com/w3c/csswg-drafts/issues/"
# `#` not preceded by a word char or another `#` (so `#708` in `#614/#708` links,
# but `##2` headings and `foo#2` do not), followed by digits and a word boundary.
ISSUE_RE = re.compile(r"(?<![\w#])#(\d+)\b")
# qualified refs to the other mirrored repos (bare #N stays csswg-drafts)
QUALIFIED_REPOS = ["openui/open-ui", "whatwg/html"]
QUALIFIED_RE = re.compile(
    r"(?<![\w/])(" + "|".join(re.escape(r) for r in QUALIFIED_REPOS) + r")#(\d+)\b"
)
# segments to leave untouched: inline code, existing markdown links, bare URLs
PROTECT_RE = re.compile(r"(`[^`]*`|\[[^\]]*\]\([^)]*\)|https?://\S+)")


def build_people_tokens() -> dict[str, str]:
    tokens = {}
    for p in load_people():
        slug = p["slug"]
        gh = p.get("github")
        if gh:
            tokens[f"@{gh}"] = slug
            if len(gh) >= 4:
                tokens[gh] = slug
        for nick in p.get("irc_nicks", []):
            if len(nick) >= 4:
                tokens[nick] = slug
    return tokens


def link_line(line: str, people: dict[str, str], depth: int) -> str:
    if line.lstrip().startswith(">"):
        return line  # never touch quotations
    rel = "../" * depth + "people/"
    parts = PROTECT_RE.split(line)
    for i, part in enumerate(parts):
        if i % 2 == 1:  # protected segment
            continue
        part = QUALIFIED_RE.sub(r"[\1#\2](https://github.com/\1/issues/\2)", part)
        part = ISSUE_RE.sub(rf"[#\1]({ISSUES_URL}\1)", part)
        for token, slug in people.items():
            part = re.sub(
                rf"(?<![\w@\[/.-]){re.escape(token)}(?![\w\]/-])",
                f"[{token}]({rel}{slug}.md)",
                part,
            )
        parts[i] = part
    return "".join(parts)


def process(path: Path, people: dict[str, str]) -> bool:
    depth = len(path.relative_to(ROOT / "wiki").parts) - 1
    out, in_fence, in_frontmatter = [], False, False
    original = path.read_text()
    for i, line in enumerate(original.splitlines()):
        if i == 0 and line == "---":
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            if line == "---":
                in_frontmatter = False
            continue
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(line if in_fence else link_line(line, people, depth))
    new = "\n".join(out) + "\n"
    if new != original:
        path.write_text(new)
        return True
    return False


def main() -> None:
    people = build_people_tokens()
    changed = 0
    for d in DIRS:
        for f in (ROOT / "wiki" / d).rglob("*.md"):
            changed += process(f, people)
    print(f"[link_refs] {changed} files updated")


if __name__ == "__main__":
    main()
