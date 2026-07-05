# CSSWG LLM Wiki — Catalog

> *This wiki is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*

Entry point for every query. One line per page; update on every ingest.

## Features

| Feature | Status | Specs | Summary |
|---|---|---|---|
| [Absolute Lengths & the Pixel Unit](features/absolute-lengths.md) | shipped | css-values-3, css-values-4 | `px` is an angular measure (the reference pixel), not a physical dot; on screen it is the *anchor* and physical units fall out of it — physical-size units repeatedly rejected (#614/#708/#5221) |
| [CSS Nesting](features/css-nesting.md) | shipped | css-nesting-1 | Native nesting of style rules; history dominated by the "syntax wars" (Option 3 + parser lookahead) and the `&`-as-`:is()` specificity tail |

## Specs

| Spec | Maturity | Features tracked |
|---|---|---|
| [css-nesting-1](specs/css-nesting-1.md) | WD | css-nesting |
| [css-values-3](specs/css-values-3.md) | CRD | absolute-lengths |
| [css-values-4](specs/css-values-4.md) | WD | absolute-lengths |

## Families

| Family | Members | Theme |
|---|---|---|
| *(none yet)* | | |

## Recent meetings

| Date | Type | Summary |
|---|---|---|
| *(none yet)* | | |

## Not yet ingested

Next in the pilot order: `anchor-positioning`, `container-queries`.
Candidates surfaced by `/triage` land here before they get pages.
