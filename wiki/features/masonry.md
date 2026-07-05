---
title: CSS Masonry (Grid Lanes)
slug: masonry
kind: feature
status: in-discussion   # adopted 2020, core switch syntax resolved 2025-11; spec still WD with many open issues
specs: [css-grid-3]
spec_history:
  - {spec: css-grid-3, from: "2020-01"}   # considered as its own module (#13115) but kept in Grid
key_people: [fantasai, tabatkins, jensimmons, bfgeek, alisonmaher, rachelandrew, astearns]
key_issues: [4650, 9041, 11243, 12022, 9733, 5675]
first_seen: "2020-01"
resolutions_count: 67   # resolutions labeled css-grid-3 in resolutions-index (Grid 3 == the masonry module)
families: []
coverage: {github: full, www-style: n/a, member_era: n/a}   # entirely post-2020 GitHub era
generated_by: llm
---

## Overview

Masonry is the "Pinterest-style" layout where items pack into columns (or rows) of a fixed
track set, but flow freely in the other axis so that items of unequal size sit flush against
whatever is above them instead of aligning into rigid grid rows. The CSSWG adopted it in 2020
as an extension of CSS Grid, triggered by `grid-template-rows: masonry` / `grid-template-columns:
masonry`. After five years of debate over whether masonry belongs *inside* Grid or should be a
*separate* layout, and over what to call it, the group resolved in November 2025 that the switch
is a **new display type named `display: grid-lanes`** — not `display: masonry`.

The name is the visible tip of a deeper decision. Two camps disagreed for years: Google/Chrome
argued masonry is a distinct layout that can't cleanly share Grid's algorithm and should be
`display: masonry`; the original editors (Apple/WebKit) argued it's a variation of Grid that
should reuse Grid's syntax and stay teachable as "Grid you already know." The `grid-lanes`
outcome is the compromise: masonry gets its own `display` value (Chrome's position on the
*trigger*) but the value carries the word **grid**, reuses Grid's templating/placement
properties, and lives in the Grid spec (the editors' position on *consistency and branding*).

## Milestones

| date | milestone | source |
|---|---|---|
| 2020-01-06 | Masonry first proposed as a Grid extension (`grid-template-*: masonry`) — issue [#4650](https://github.com/w3c/csswg-drafts/issues/4650) opened | [#4650](https://github.com/w3c/csswg-drafts/issues/4650) |
| 2020-01-23 | WG adopts the proposal; [fantasai](../people/fantasai.md) & Tab Atkins named editors | [resolution](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-577614598) |
| 2020-10-20 | Mats Palmgren's (Firefox) draft adopted as the Editor's Draft | [resolution](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-713128263) |
| 2023-07-06 | Google (Ian Kilpatrick) opens "Alternative masonry path forward" proposing a separate `display: masonry` | [#9041](https://github.com/w3c/csswg-drafts/issues/9041) |
| 2024-09-19 | FPWD of *CSS Grid Layout Module Level 3*, carrying both competing syntaxes | [WD-css-grid-3-20240919](https://www.w3.org/TR/2024/WD-css-grid-3-20240919/) |
| 2025-01-31 | WG resolves to reuse Grid templating & placement properties for masonry | [resolution](https://github.com/w3c/csswg-drafts/issues/11243#issuecomment-2627998471) |
| 2025-08-19 | WG resolves the switch is a new display type whose name must contain "grid" | [resolution](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3200131437) |
| 2025-11-13 | Name resolved by poll: `display: grid-lanes` (over `masonry-grid`) | [resolution](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3525043825) |
| 2026-01-29 | `grid-lanes` kept in the Grid spec (not a separate module); grand `item-flow` theory abandoned | [#13115 res](https://github.com/w3c/csswg-drafts/issues/13115#issuecomment-3820644949), [#11480 res](https://github.com/w3c/csswg-drafts/issues/11480#issuecomment-3820776942) |

## Resolutions

Chronological; a curated set of the narrative-carrying resolutions (Grid 3 has 67 resolutions
in total in the index). Text is verbatim from `_generated/resolutions-index.jsonl`.

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2020-01-23 | Adopt Masonry layout proposal, editors [fantasai](../people/fantasai.md) and Tab, Mats if he's convinceable, Jen Simmons if she's able | [#4650](https://github.com/w3c/csswg-drafts/issues/4650) | [link](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-577614598) |
| 2020-10-20 | Adopt Mats's draft as ED | [#4650](https://github.com/w3c/csswg-drafts/issues/4650) | [link](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-713128263) |
| 2023-10-04 | Drop align-tracks, justify-tracks from Masonry spec | [#8207](https://github.com/w3c/csswg-drafts/issues/8207) | [link](https://github.com/w3c/csswg-drafts/issues/8207#issuecomment-1747805578) |
| 2024-09-11 | FPWD for Grid 3 | [#8195](https://github.com/w3c/csswg-drafts/issues/8195) | [link](https://github.com/w3c/csswg-drafts/issues/8195#issuecomment-2344098078) |
| 2025-01-31 | Re-use grid templating and placement properties for masonry layout | [#11243](https://github.com/w3c/csswg-drafts/issues/11243) | [link](https://github.com/w3c/csswg-drafts/issues/11243#issuecomment-2627998471) |
| 2025-04-02 | Masonry reading order operates more like grid than flex | [#5675](https://github.com/w3c/csswg-drafts/issues/5675) | [link](https://github.com/w3c/csswg-drafts/issues/5675#issuecomment-2773715622) |
| 2025-08-19 | Switch for masonry will be a new display type. Display type must include the word grid in the name. We will open an issue for the exact name. | [#12022](https://github.com/w3c/csswg-drafts/issues/12022) | [link](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3200131437) |
| 2025-08-19 | Design Principle - Keep masonry consistent with grid wherever practical: deviations need to be strongly justified by the inherent differences between grid vs masonry layout | [#12022](https://github.com/w3c/csswg-drafts/issues/12022) | [link](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3201014167) |
| 2025-11-13 | masonry switch will be display: grid-lanes | [#12022](https://github.com/w3c/csswg-drafts/issues/12022) | [link](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3525043825) |
| 2025-12-12 | Use `display: grid-lanes`. https://github.com/w3c/csswg-drafts/issues/12022 | [#9733](https://github.com/w3c/csswg-drafts/issues/9733) | [link](https://github.com/w3c/csswg-drafts/issues/9733#issuecomment-3644327877) |
| 2026-01-29 | Integrate the diff spec with grid | [#13115](https://github.com/w3c/csswg-drafts/issues/13115) | [link](https://github.com/w3c/csswg-drafts/issues/13115#issuecomment-3820644949) |
| 2026-01-29 | Abandon grand item-flow theory in favor of smaller targeted unification attempts | [#11480](https://github.com/w3c/csswg-drafts/issues/11480) | [link](https://github.com/w3c/csswg-drafts/issues/11480#issuecomment-3820776942) |
| 2026-01-29 | Add inline-grid-lanes, and remove indication that inline- syntaxes are legacy or otherwise inferior. | [#10961](https://github.com/w3c/csswg-drafts/issues/10961) | [link](https://github.com/w3c/csswg-drafts/issues/10961#issuecomment-3820508516) |

## Key debates

### Part of Grid, or its own layout mode?

This is the foundational disagreement, and it ran largely along vendor lines.

- **Origin (2020):** masonry was adopted as an *extension of Grid* — you opt in with
  `grid-template-rows: masonry` (or `-columns`), reusing Grid's track machinery. Mats Palmgren's
  Firefox prototype became the Editor's Draft.
  ([#4650 adoption](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-577614598),
  [ED adoption](https://github.com/w3c/csswg-drafts/issues/4650#issuecomment-713128263))
- **Google's counter-proposal (2023, [#9041](https://github.com/w3c/csswg-drafts/issues/9041)):**
  [bfgeek](../people/bfgeek.md) (Ian Kilpatrick) opened "Alternative masonry path forward"
  proposing a *separate* `display: masonry` with dedicated `masonry-*` properties. Two arguments:
  (1) **performance** — masonry sizes tracks *first* then places items ("works in reverse"), so a
  Grid-based implementation "can't correctly size the rows/columns" or the container; Chrome
  called the Grid-based spec "unshippable" and "more or less unfixable while the two layout modes
  are entwined." (2) **design** — the two modes "fundamentally don't and can't share a layout
  algorithm," and merging them repeats the block/multicol mistake: "If we had defined
  `display: multicol` back in the day, many issues would have been avoided."
- **The editors' rebuttal:** the minutes record [jensimmons](../people/jensimmons.md) and
  [fantasai](../people/fantasai.md) defending integration on **teachability** and to avoid
  property duplication — the framing being that if masonry is part of Grid, "most of what you just
  learned [about Grid] applies," rather than shipping a parallel `masonry-*` vocabulary
  ([#11243](https://github.com/w3c/csswg-drafts/issues/11243)). The FPWD shipped with *both*
  syntaxes side by side, and the question went to a TAG review plus dueling Chrome and WebKit
  blog posts in 2024 (linked from [#11243](https://github.com/w3c/csswg-drafts/issues/11243)).

### Reuse Grid's properties, dedicated `masonry-*` properties, or `item-flow`?

With the performance concerns largely resolved, [fantasai](../people/fantasai.md) reopened the
question as a pure **syntax** debate in [#11243](https://github.com/w3c/csswg-drafts/issues/11243)
(2024-11).

- WebKit floated **`item-flow`** — generalizing item flow across Grid/Flex/masonry into
  `item-direction` / `item-wrap` / `item-pack` / `item-slack`, per TAG feedback.
- The minutes record [alisonmaher](../people/alisonmaher.md) (Microsoft) concluding masonry should
  be a separate display type because "several properties behave differently in each, or don't
  apply."
- **Resolved 2025-01-31:** *"Re-use grid templating and placement properties for masonry layout"* —
  a win for the integration side on syntax: masonry uses `grid-template-columns/rows` and Grid
  placement, not a parallel property set
  ([resolution](https://github.com/w3c/csswg-drafts/issues/11243#issuecomment-2627998471)).

### How to switch masonry on — and why the name *must* contain "grid"

Even with Grid's properties reused, the group still needed a trigger. Three candidates survived
into [#12022](https://github.com/w3c/csswg-drafts/issues/12022) (2025): `grid-template-*: masonry`,
`item-flow: collapse`, or a new `display` type.

- [alisonmaher](../people/alisonmaher.md)'s writeup argued for a **display type**: per the
  css-display definition, a display type "defines the kind of formatting context it generates,"
  and masonry's placement algorithm, track sizing, subgrid behaviour and alignment all differ
  from Grid — so it is a distinct mode. She also noted `grid-template-columns/rows: masonry` is
  unintuitive about *which axis* the direction applies to
  ([comment](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3196597076)).
- The minutes record broad support for a separate display type, but with a hard constraint —
  [florian](../people/frivoal.md): "+1 ... -1 to `display: [something that doesn't include the word grid]`", and
  [astearns](../people/astearns.md) noting the group wanted "grid in value name."
- **Resolved 2025-08-19:** the switch is *"a new display type. Display type must include the word
  grid in the name"*, paired with a design principle to *"Keep masonry consistent with grid
  wherever practical"*
  ([switch resolution](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3200131437),
  [design principle](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3201014167)).
  This is the compromise: Chrome's *separate display type* won the trigger; the editors' *stay
  consistent with / branded as Grid* won the constraint. This is the direct reason it is **not**
  bare `display: masonry`.

### Choosing the name: `grid-lanes` vs `masonry-grid`

Two threads fed the name. [#9733](https://github.com/w3c/csswg-drafts/issues/9733) (opened
2023-12) questioned the word "masonry" itself: the thread records that non-native English speakers
find "masonry" hard (yisibl), that "waterfall" only fits the vertical case (jfkthame), and — on
the other side — desandro, author of the original *Masonry* JS library, recommending the group
keep "masonry" as an established term since 2009. [jensimmons](../people/jensimmons.md) reframed
masonry as simply *turning off* Grid's row-alignment.

Once "must contain grid" was fixed, a naming poll drew 300+ responses. Per the
[2025-11-13 minutes](https://github.com/w3c/csswg-drafts/issues/12022#issuecomment-3525043825):

- `grid-stack` / `stack` was dropped — confused with **stacking context**.
- `grid-pack` / `pack` was dropped — confused with **density** (dense packing).
- The final head-to-head was `grid-lanes` vs `masonry-grid`. The minutes record
  [alisonmaher](../people/alisonmaher.md) and kbabbitt preferring `masonry-grid` (an established
  term since 2009), but `grid-lanes` polled ~14:8 (about 3:2) and "didn't have downsides," and
  composes into a future shorthand (`grid-lanes: column repeat(3, auto)`).
- **Resolved 2025-11-13:** *"masonry switch will be display: grid-lanes"*; the rename issue
  [#9733](https://github.com/w3c/csswg-drafts/issues/9733) closed 2025-12-12 confirming it.

"lanes" is also neutral across the two visual variants: [#12803](https://github.com/w3c/csswg-drafts/issues/12803)
resolved that the orientation defaults to **waterfall** or **brick** layout depending on whether
`grid-template-columns` or `grid-template-rows` was set
([resolution](https://github.com/w3c/csswg-drafts/issues/12803#issuecomment-3607869618)).

### Accessibility: reading order

- [#5675](https://github.com/w3c/csswg-drafts/issues/5675) (2020-10) raised that masonry can
  divorce reading order from visual order. Resolved 2025-04-02 that *"Masonry reading order
  operates more like grid than flex"*
  ([resolution](https://github.com/w3c/csswg-drafts/issues/5675#issuecomment-2773715622)).
- `align-tracks` / `justify-tracks` were dropped in 2023 partly over accessibility concerns
  ([#8207 resolution](https://github.com/w3c/csswg-drafts/issues/8207#issuecomment-1747805578)).

### Aftermath (2026)

- `grid-lanes` stays **in the Grid spec** rather than a standalone `css-masonry` module
  ([#13115 resolution](https://github.com/w3c/csswg-drafts/issues/13115#issuecomment-3820644949)).
- The sweeping `item-flow` unification was scaled back — *"Abandon grand item-flow theory in favor
  of smaller targeted unification attempts"*
  ([#11480 resolution](https://github.com/w3c/csswg-drafts/issues/11480#issuecomment-3820776942)).
- `inline-grid-lanes` was added, dropping the framing that `inline-` syntaxes are legacy
  ([#10961 resolution](https://github.com/w3c/csswg-drafts/issues/10961#issuecomment-3820508516)).

## Related features

- Host module: [CSS Grid Layout Module Level 3](../specs/css-grid-3.md).
- Closely tied to Grid track sizing, subgrid, and alignment (`css-grid-1/2`, `css-align-3`), and
  to the abandoned `item-flow` unification with Flexbox (`css-flexbox-2`).

## Sources

Primary (GitHub issue threads, mirrored):

- [#4650 Masonry layout](../../raw/data/github/csswg-drafts/issues/04xxx/04650.md) — original adoption.
- [#9041 Alternative masonry path forward](../../raw/data/github/csswg-drafts/issues/09xxx/09041.md) — Google's separate-display proposal.
- [#11243 Masonry Syntax Debate](../../raw/data/github/csswg-drafts/issues/11xxx/11243.md) — reuse-vs-dedicated syntax.
- [#12022 Masonry Switch Syntax](../../raw/data/github/csswg-drafts/issues/12xxx/12022.md) — display type + `grid-lanes` name.
- [#9733 Renaming `masonry` keyword](../../raw/data/github/csswg-drafts/issues/09xxx/09733.md) — the naming debate.
- [#5675 accessibility / reading order](../../raw/data/github/csswg-drafts/issues/05xxx/05675.md).

Status: `raw/data/w3c-api/specifications/css-grid-3.json` (`snapshot_at: 2026-07-04`);
Editor's Draft <https://drafts.csswg.org/css-grid-3/>.

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
