---
title: CSS Grid Layout Module Level 3
slug: css-grid-3
kind: spec
series: css-grid
level: 3
maturity: WD
status_verbatim: "Working Draft"
first_published: "2024-09-19"
latest_version: "2026-01-21"
ed_url: https://drafts.csswg.org/css-grid-3/
tr_url: https://www.w3.org/TR/css-grid-3/
github_label: css-grid-3
features: [masonry]
generated_by: llm
---

# CSS Grid Layout Module Level 3

Grid Level 3 is, in practice, the **masonry** module — it defines masonry (a.k.a. waterfall /
brick) layout as an extension of Grid, switched on by `display: grid-lanes`. It is the spec
vehicle for the [masonry](../features/masonry.md) feature. A 2026-01-29 resolution kept masonry
in this module rather than spinning out a separate `css-masonry`
([#13115](https://github.com/w3c/csswg-drafts/issues/13115#issuecomment-3820644949)).

## Status history

From `raw/data/w3c-api/specifications/css-grid-3.json` (snapshot 2026-07-04):

| Date | Status | TR version |
|---|---|---|
| 2024-09-19 | First Public Working Draft | https://www.w3.org/TR/2024/WD-css-grid-3-20240919/ |
| 2024-10-03 | Working Draft | https://www.w3.org/TR/2024/WD-css-grid-3-20241003/ |
| 2025-02-07 | Working Draft | https://www.w3.org/TR/2025/WD-css-grid-3-20250207/ |
| 2025-09-17 | Working Draft | https://www.w3.org/TR/2025/WD-css-grid-3-20250917/ |
| 2025-12-16 | Working Draft | https://www.w3.org/TR/2025/WD-css-grid-3-20251216/ |
| 2025-12-23 | Working Draft | https://www.w3.org/TR/2025/WD-css-grid-3-20251223/ |
| 2026-01-21 | Working Draft | https://www.w3.org/TR/2026/WD-css-grid-3-20260121/ |

```mermaid
xychart-beta
    title "css-grid-3 maturity over time"
    x-axis ["2024-09", "2024-10", "2025-02", "2025-09", "2025-12", "2026-01"]
    y-axis "0=ED 1=FPWD 2=WD 3=CR 4=PR 5=REC" 0 --> 5
    line [1, 2, 2, 2, 2, 2]
```

The spec debuted at FPWD in September 2024 and moved to Working Draft within weeks; it has
re-published as WD repeatedly since (six WD versions through 2026-01), reflecting the still-active
syntax churn rather than any maturity advance.

## Features tracked here

- [masonry](../features/masonry.md) — masonry / `display: grid-lanes` layout.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
