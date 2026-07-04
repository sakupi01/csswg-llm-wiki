#!/usr/bin/env python3
"""Auto-link known people in wiki prose to their people pages.

Conservative by design:
- only wiki/{features,specs,families,history,meetings}/ are processed
- fenced code blocks, inline code, blockquote lines (verbatim quotations!) and
  already-linked tokens are left untouched
- only exact, case-sensitive whole-word matches of `@github`, github login, or
  IRC nicks (length >= 4) are linked
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from extract_people import load_people  # noqa: E402

DIRS = ["features", "specs", "families", "history", "meetings"]


def build_tokens() -> dict[str, str]:
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


def link_line(line: str, tokens: dict[str, str], depth: int) -> str:
    if line.lstrip().startswith(">"):
        return line  # never touch quotations
    # protect inline code and existing links from substitution
    protected = re.split(r"(`[^`]*`|\[[^\]]*\]\([^)]*\))", line)
    rel = "../" * depth + "people/"
    for i, part in enumerate(protected):
        if i % 2 == 1:
            continue
        for token, slug in tokens.items():
            part = re.sub(
                rf"(?<![\w@\[/.-]){re.escape(token)}(?![\w\]/-])",
                f"[{token}]({rel}{slug}.md)",
                part,
            )
        protected[i] = part
    return "".join(protected)


def process(path: Path, tokens: dict[str, str]) -> bool:
    depth = len(path.relative_to(ROOT / "wiki").parts) - 1
    out, in_fence, in_frontmatter = [], False, False
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
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
        out.append(line if in_fence else link_line(line, tokens, depth))
    new = "\n".join(out) + "\n"
    if new != path.read_text():
        path.write_text(new)
        return True
    return False


def main() -> None:
    tokens = build_tokens()
    changed = 0
    for d in DIRS:
        for f in (ROOT / "wiki" / d).rglob("*.md"):
            changed += process(f, tokens)
    print(f"[link_people] {changed} files updated")


if __name__ == "__main__":
    main()
