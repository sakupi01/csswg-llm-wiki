---
title: Container Queries
slug: container-queries
kind: feature
status: shipped    # size queries interoperable since 2023; style + scroll-state queries newer/partial
specs: [css-conditional-5]
spec_history:
  - {spec: css-contain-3, from: "2021-02", to: "2024-06"}   # incubated in Containment L3
  - {spec: css-conditional-5, from: "2024-06"}              # moved out to Conditional Rules L5 (#10433)
key_people: [miriam, fantasai, tabatkins, frivoal, una]
key_issues: [5796, 6644, 6870, 10433, 5888, 11182]
first_seen: "2021-02"   # first WG resolution defining them; the demand (element queries) is far older
resolutions_count: 48   # css-conditional-5 (current host); +53 more under css-contain-3 (2021–2024 incubation)
families: []
coverage: {github: full, www-style: none, member_era: n/a}
generated_by: llm
---

## Overview

Container Queries let a style rule respond to the size or computed style of an **ancestor
container** rather than the viewport — the piece long missing from responsive design. An element
declares itself a container with `container-type` (`size` / `inline-size`) and optionally
`container-name`; descendants then match `@container (inline-size > 30rem) { … }`, and can use
container-relative length units (`cqw`, `cqh`, `cqi`, `cqb`).

The feature was the web platform's most-requested for roughly a decade, blocked by a genuine
circularity: if an element's styles depend on its own size, and its size depends on its styles,
layout loops. The resolution — worked out when the CSSWG picked the problem back up in 2021 with
[Miriam Suzanne](../people/miriam.md) added as editor — is to query a *different* element (an
ancestor) and require that container to have **containment** so its size does not depend on its
contents. Size container queries reached cross-browser support in 2023. Two further kinds grew
from the same `@container` machinery: **style queries** (`@container style(--theme: dark)`) and,
more recently, **scroll-state queries** (`@container scroll-state(stuck: top)`).

The spec has changed homes: container queries were **incubated in CSS Containment Level 3**
(`css-contain-3`) and then **moved to CSS Conditional Rules Level 5** (`css-conditional-5`) in
2024, on the grounds that they *use* containment but are not *about* defining it
([#10433](https://github.com/w3c/csswg-drafts/issues/10433#issuecomment-2165558965)).

## Milestones

| date | milestone | source |
|---|---|---|
| 2021-02-11 | Container queries adopted for `css-contain-3`; [Miriam](../people/miriam.md) added as editor alongside the Containment L2 editors | [resolution](https://github.com/w3c/csswg-drafts/issues/5796#issuecomment-777846985) |
| 2021-05-26 | Containers opt in via an independent property (the future `container-type`) | [resolution](https://github.com/w3c/csswg-drafts/issues/6174#issuecomment-848948519) |
| 2021-10-06 | `cq` chosen as the container-unit prefix (`cqw`/`cqh`/`cqi`/`cqb`) | [resolution](https://github.com/w3c/csswg-drafts/issues/5888#issuecomment-937291693) |
| 2021-12-08 | First Public Working Draft of CSS Containment Level 3 | [resolution](https://github.com/w3c/csswg-drafts/issues/6426#issuecomment-988998375) |
| 2022-01-26 | Size queries drop the function syntax; the `style()` function is reserved for style queries | [resolution](https://github.com/w3c/csswg-drafts/issues/6870#issuecomment-1022430911) |
| 2022-02-09 | The `@container` rule picks its container **from the queries themselves**; `container-type` removed from the preamble | [resolution](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1034036418) |
| 2024-05-15 | Container queries and units resolved to use the **flat tree** | [resolution](https://github.com/w3c/csswg-drafts/issues/5984#issuecomment-2112977366) |
| 2024-06-13 | Container queries **moved** from `css-contain-3` to `css-conditional-5` | [resolution](https://github.com/w3c/csswg-drafts/issues/10433#issuecomment-2165558965) |
| 2024-11-20 | Scroll-state query keyword `overflowing` renamed to `scrollable` | [resolution](https://github.com/w3c/csswg-drafts/issues/11182#issuecomment-2489232115) |

## Resolutions

Chronological; a curated set of the narrative-carrying resolutions. Container queries have ~53
resolutions under `css-contain-3` (incubation) and are now hosted in `css-conditional-5` (48
resolutions, not all about container queries). Text is verbatim from
`_generated/resolutions-index.jsonl`.

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2021-02-11 | Define container queries in css-contain-3, editors L2 editors + Miriam | [#5796](https://github.com/w3c/csswg-drafts/issues/5796) | [link](https://github.com/w3c/csswg-drafts/issues/5796#issuecomment-777846985) |
| 2021-05-12 | Style containment will be required in order to establish a queryable container | [#6213](https://github.com/w3c/csswg-drafts/issues/6213) | [link](https://github.com/w3c/csswg-drafts/issues/6213#issuecomment-839919034) |
| 2021-05-26 | Container queries are triggered by independent property (name to be bikeshed) | [#6174](https://github.com/w3c/csswg-drafts/issues/6174) | [link](https://github.com/w3c/csswg-drafts/issues/6174#issuecomment-848948519) |
| 2021-10-06 | Use cq as the prefix | [#5888](https://github.com/w3c/csswg-drafts/issues/5888) | [link](https://github.com/w3c/csswg-drafts/issues/5888#issuecomment-937291693) |
| 2022-01-26 | drop the function syntax for querying sizes, but keep the function syntax for querying styles | [#6870](https://github.com/w3c/csswg-drafts/issues/6870) | [link](https://github.com/w3c/csswg-drafts/issues/6870#issuecomment-1022430911) |
| 2022-02-09 | when we select a container, we determine which container by looking at the actual queries and finding an appropriate container for the questions being asked | [#6644](https://github.com/w3c/csswg-drafts/issues/6644) | [link](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1034036418) |
| 2022-02-09 | remove the container-type syntax from the preamble of the @container rule | [#6644](https://github.com/w3c/csswg-drafts/issues/6644) | [link](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1034036418) |
| 2022-02-16 | Keep style queries in level 3. | [#7020](https://github.com/w3c/csswg-drafts/issues/7020) | [link](https://github.com/w3c/csswg-drafts/issues/7020#issuecomment-1041944310) |
| 2022-06-22 | All elements are style containers by default. | [#7066](https://github.com/w3c/csswg-drafts/issues/7066) | [link](https://github.com/w3c/csswg-drafts/issues/7066#issuecomment-1163348533) |
| 2022-06-29 | Change initial value of 'container-type' to "normal" | [#7402](https://github.com/w3c/csswg-drafts/issues/7402) | [link](https://github.com/w3c/csswg-drafts/issues/7402#issuecomment-1170195051) |
| 2023-03-22 | style queries can accept properties in boolean context; false if matches initial value, true otherwise | [#8127](https://github.com/w3c/csswg-drafts/issues/8127) | [link](https://github.com/w3c/csswg-drafts/issues/8127#issuecomment-1479871971) |
| 2024-05-15 | Container queries and units use the flat tree | [#5984](https://github.com/w3c/csswg-drafts/issues/5984) | [link](https://github.com/w3c/csswg-drafts/issues/5984#issuecomment-2112977366) |
| 2024-06-13 | Move CQs from contain-3 to conditional-5 | [#10433](https://github.com/w3c/csswg-drafts/issues/10433) | [link](https://github.com/w3c/csswg-drafts/issues/10433#issuecomment-2165558965) |
| 2024-07-24 | container-type does not force layout containment, but does force an independent formatting context | [#10544](https://github.com/w3c/csswg-drafts/issues/10544) | [link](https://github.com/w3c/csswg-drafts/issues/10544#issuecomment-2248438355) |
| 2024-11-20 | Rename "overflowing" to "scrollable" | [#11182](https://github.com/w3c/csswg-drafts/issues/11182) | [link](https://github.com/w3c/csswg-drafts/issues/11182#issuecomment-2489232115) |
| 2025-08-20 | Container names are not tree-scoped | [#12090](https://github.com/w3c/csswg-drafts/issues/12090) | [link](https://github.com/w3c/csswg-drafts/issues/12090#issuecomment-3204775586) |
| 2026-03-31 | style() and transitions use the same color comparison method | [#13157](https://github.com/w3c/csswg-drafts/issues/13157) | [link](https://github.com/w3c/csswg-drafts/issues/13157#issuecomment-4165667681) |

## Key debates

### Breaking the circularity: query the container, require containment

The reason container queries took a decade was not syntax but a layout hazard: a rule that sizes
an element from its own size is circular. The design that shipped sidesteps it — you never query
the element being styled, you query an **ancestor container**, and that container must establish
containment so its size is independent of the descendants reading it. The early rule was strict —
*"Style containment will be required in order to establish a queryable container"*
([#6213](https://github.com/w3c/csswg-drafts/issues/6213#issuecomment-839919034)) — and opting in
was made an *independent property* (the future `container-type`) rather than overloading `contain`
([#6174](https://github.com/w3c/csswg-drafts/issues/6174#issuecomment-848948519)). A later
correction clarified the exact guarantee: *"container-type does not force layout containment, but
does force an independent formatting context"*
([#10544](https://github.com/w3c/csswg-drafts/issues/10544#issuecomment-2248438355)).

### How `@container` finds its container — and the "everything is a style container" tension

Once *style* queries entered the picture, a design question surfaced (raised by
[fantasai](../people/fantasai.md) in [#6644](https://github.com/w3c/csswg-drafts/issues/6644)): if
any element can be a style container, an intervening style container would *shadow* an element's
size container and silently break its size queries. Two shapes were debated:

- [andruud](../people/andruud.md) proposed **name-only** explicit selection with "nearest
  compatible container" as the default — `@container <name>? <query>`, no container-type in the
  rule ([comment](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1011415715)).
- [una](../people/una.md) argued the opposite instinct — that *requiring* explicit container
  typing is a better developer experience than "everything-is-a-container," which "can create
  unintended confusion"
  ([comment](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1012451010)).

The group took the container-selection-by-query route. **Resolved 2022-02-09**: *"when we select
a container, we determine which container by looking at the actual queries and finding an
appropriate container for the questions being asked,"* and correspondingly *"remove the
container-type syntax from the preamble of the @container rule"*
([resolution](https://github.com/w3c/csswg-drafts/issues/6644#issuecomment-1034036418)). This is
why `@container` today takes an optional *name* and a query, but never a type.

### Size queries vs style queries: one `@container`, two mechanisms

Container queries fork into two things that share a rule. **Resolved 2022-01-26**: *"drop the
function syntax for querying sizes, but keep the function syntax for querying styles"*
([#6870](https://github.com/w3c/csswg-drafts/issues/6870#issuecomment-1022430911)) — so a size
query is bare (`@container (inline-size > 30rem)`) while a style query is wrapped
(`@container style(--x: y)`). Style queries were kept in the module rather than deferred
([#7020](https://github.com/w3c/csswg-drafts/issues/7020#issuecomment-1041944310)), *"All elements
are style containers by default"*
([#7066](https://github.com/w3c/csswg-drafts/issues/7066#issuecomment-1163348533)), and a property
used in boolean context is *"false if [it] matches initial value, true otherwise"*
([#8127](https://github.com/w3c/csswg-drafts/issues/8127#issuecomment-1479871971)). The newest
refinement pins down `style()` equality: *"style() and transitions use the same color comparison
method"* — oklab with an epsilon
([#13157](https://github.com/w3c/csswg-drafts/issues/13157#issuecomment-4165667681)).

### Splitting the spec: containment vs the queries built on it

By 2024 the module structure had drifted — container queries were Level 3 of a *Containment*
spec they merely depended on. [frivoal](../people/frivoal.md) proposed the reorganization in
[#10433](https://github.com/w3c/csswg-drafts/issues/10433): container queries "would be more
suited to be a standalone spec … has significant normative dependencies onto CSS-Contain, but
isn't about defining containment itself," and `inline-size` containment should move *back* to
Containment Level 2. [miriam](../people/miriam.md) agreed it was "strange that we are alternating
levels for fairly distinct features." **Resolved 2024-06-13**: *"Move CQs from contain-3 to
conditional-5"* and *"move contain-inline-size from contain-3 back to contain-2 to join its
family"* ([resolution](https://github.com/w3c/csswg-drafts/issues/10433#issuecomment-2165558965)).
The same thread notes a prior (2023-11) decision to spin **state/scroll-state container queries**
into their own level once the move landed.

### Scoping and the flat tree

Named containers and container units interact with shadow DOM. **Resolved 2024-05-15**:
*"Container queries and units use the flat tree"*
([#5984](https://github.com/w3c/csswg-drafts/issues/5984#issuecomment-2112977366)), and later
*"Container names are not tree-scoped"*
([#12090](https://github.com/w3c/csswg-drafts/issues/12090#issuecomment-3204775586)) — a
deliberately *different* choice from the tree-scoped naming used by, e.g., scroll timelines and
anchors.

## Related features

- Host module: [CSS Conditional Rules Module Level 5 (css-conditional-5)](../specs/css-conditional-5.md);
  incubated in CSS Containment Level 3 (`css-contain-3`).
- Built on **CSS Containment** (`css-contain-1/2`): `container-type` reuses the containment
  machinery (`contain: inline-size` etc.).
- **Scroll-state queries** (`@container scroll-state(...)`) extend the same rule and are slated
  for their own level; see [#11182](https://github.com/w3c/csswg-drafts/issues/11182),
  [#11542](https://github.com/w3c/csswg-drafts/issues/11542).

## Sources

Primary (GitHub issue threads, mirrored):

- [#5796 define container queries](../../raw/data/github/csswg-drafts/issues/05xxx/05796.md) — adoption + Miriam as editor.
- [#6644 container selection from the query](../../raw/data/github/csswg-drafts/issues/06xxx/06644.md) — the `@container` design.
- [#6870 size vs style function syntax](../../raw/data/github/csswg-drafts/issues/06xxx/06870.md).
- [#10433 reorganizing the Containment specs](../../raw/data/github/csswg-drafts/issues/10xxx/10433.md) — the module move.
- [#5888 `cq` unit prefix](../../raw/data/github/csswg-drafts/issues/05xxx/05888.md).

Status: `raw/data/w3c-api/specifications/css-conditional-5.json` and `css-contain-3.json`
(`snapshot_at: 2026-07-04`); Editor's Draft <https://drafts.csswg.org/css-conditional-5/>.

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
