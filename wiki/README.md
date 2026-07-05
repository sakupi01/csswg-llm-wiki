# CSSWG LLM Wiki — Catalog

> *This wiki is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*

Entry point for every query. One line per page; update on every ingest.

## Features

| Feature | Status | Specs | Summary |
|---|---|---|---|
| [Absolute Lengths & the Pixel Unit](features/absolute-lengths.md) | shipped | css-values-3, css-values-4 | `px` is an angular measure (the reference pixel), not a physical dot; on screen it is the *anchor* and physical units fall out of it — physical-size units repeatedly rejected (#614/#708/#5221) |
| [CSS Nesting](features/css-nesting.md) | shipped | css-nesting-1 | Native nesting of style rules; history dominated by the "syntax wars" (Option 3 + parser lookahead) and the `&`-as-`:is()` specificity tail |
| [CSS Masonry (Grid Lanes)](features/masonry.md) | in-discussion | css-grid-3 | Pinterest-style layout; 5-year debate over Grid-integration vs a separate `display: masonry` settled as `display: grid-lanes` (Nov 2025) — a compromise keeping "grid" in the name |

## Specs

| Spec | Maturity | Features tracked |
|---|---|---|
| [css-nesting-1](specs/css-nesting-1.md) | WD | css-nesting |
| [css-values-3](specs/css-values-3.md) | CRD | absolute-lengths |
| [css-values-4](specs/css-values-4.md) | WD | absolute-lengths |
| [css-grid-3](specs/css-grid-3.md) | WD | masonry |

## Families

| Family | Members | Theme |
|---|---|---|
| *(none yet)* | | |

## Recent meetings

| Date | Type | Summary |
|---|---|---|
| *(none yet)* | | |

## Weekly digests

"This week in CSSWG" — narrative digests published as [RSS/Atom](https://sakupi01.github.io/csswg-llm-wiki/feed.xml)
and [JSON Feed](https://sakupi01.github.io/csswg-llm-wiki/feed.json). Sources in `wiki/digests/`.

| Week | Period |
|---|---|
| *(first digest pending)* | |

## Not yet ingested

Next in the pilot order: `anchor-positioning`, `container-queries`.
Candidates surfaced by `/triage` land here before they get pages.
