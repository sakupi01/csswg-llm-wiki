---
title: "Text Fitting (`text-fit`)"
slug: text-fit
kind: feature
status: in-discussion
specs: [css-text-5]
spec_history:
  - {spec: css-fonts-5, from: "2025-04", to: "2025-11"}
  - {spec: css-text-5, from: "2025-11"}
key_people: [kizu, tkent-google, astearns, patrickhlauke, bfgeek, fantasai, frivoal, miriam, emilio, tabatkins]
key_issues: [2528, 12885, 12886, 12887, 12888]
first_seen: "2018-04"
resolutions_count: 5
families: []
coverage: {github: full, www-style: none, member_era: n/a}
generated_by: llm
---

## Overview

`text-fit` scales inline text after wrapping so that it fills the available inline size of its
line box. The current [CSS Text Level 5 Editor's Draft](https://drafts.csswg.org/css-text-5/#text-fit-property)
combines the direction (`grow` or `shrink`), the scope (`consistent`, `per-line`, or
`per-line-all`), and an optional percentage limit in one property. For example,
`text-fit: grow per-line 200%` grows each eligible line independently, but by no more than
twice its original used font size.

The API is deliberately provisional. The Working Group's naming resolution was “use text-fit
for now”; browser-zoom behavior remains unresolved in [#12886](https://github.com/w3c/csswg-drafts/issues/12886),
and the draft has no test coverage. The first proposal adopted for incubation in April 2025 was
grow-only: the declared `font-size` acted as a readable lower bound and fitting only used
otherwise-empty space. A Chrome prototype subsequently demonstrated both growing and shrinking,
which triggered the central API debate: two property families (`text-grow` / `text-shrink`) or
one `text-fit` property with mutually exclusive direction keywords.

This feature changes **text to fit a box**. The separate 2026
[`max-content-sizing: shrink-to-fit`](https://github.com/w3c/csswg-drafts/issues/191#issuecomment-5042121341)
proposal changes **a box to fit already-wrapped text**; it is related but not a mode of
`text-fit`.

## Milestones

| date | milestone | source |
|---|---|---|
| 2018-04-11 | Tobi Reif opens the request; early syntax explores `font-size: fit(8px, 48px)` and a separate fitting property | [#2528](https://github.com/w3c/csswg-drafts/issues/2528) |
| 2023-03-23 | Roman Komarov revives the design around containment, a dedicated property, min/max sizing, and multiline fitting | [comment](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-1481913805) |
| 2025-04-01 | CSSWG starts incubation in Fonts 5 and appoints Roman as co-editor; the presented API is grow-only | [resolution and minutes](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512) |
| 2025-04-24 | Chrome announces an intent to prototype fit-width text | [CSSWG comment](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2828002305) |
| 2025-09-26 | Chrome reports prototype findings and proposes separate `text-grow` / `text-shrink` shorthand families | [prototype feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019) |
| 2025-11-13 | CSSWG moves the feature from Fonts 5 to CSS Text 5 | [#12885 resolution](https://github.com/w3c/csswg-drafts/issues/12885#issuecomment-3524545760) |
| 2025-11-13 | CSSWG provisionally chooses one `text-fit` property | [#12887 resolution](https://github.com/w3c/csswg-drafts/issues/12887#issuecomment-3524628665) |
| 2025-11-13 | CSSWG initially limits scaling to text (“option B”) | [#12888 resolution](https://github.com/w3c/csswg-drafts/issues/12888#issuecomment-3524706648) |
| 2026-01-27 | Chrome Canary 146 updates its prototype from two properties to `text-fit` | [comment](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3803229009) |
| 2026-04-20 | The first `text-fit` specification text merges into the CSS Text Level 5 Editor's Draft | [PR #13616](https://github.com/w3c/csswg-drafts/pull/13616) |
| 2026-04-28 | The original issue closes as the core feature is in the draft; implementation problems move to follow-up issues | [closing comment](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-4336977663) |

## Resolutions

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2025-04-01 | Roman as co-editor for Fonts 5 | [#2528](https://github.com/w3c/csswg-drafts/issues/2528) | [resolution](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512) |
| 2025-04-01 | Start work on this in Fonts 5 and begin incubating. | [#2528](https://github.com/w3c/csswg-drafts/issues/2528) | [resolution](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512) |
| 2025-11-13 | This will be using CSS Text level 5 | [#12885](https://github.com/w3c/csswg-drafts/issues/12885) | [resolution](https://github.com/w3c/csswg-drafts/issues/12885#issuecomment-3524545760) |
| 2025-11-13 | use text-fit for now | [#12887](https://github.com/w3c/csswg-drafts/issues/12887) | [resolution](https://github.com/w3c/csswg-drafts/issues/12887#issuecomment-3524628665) |
| 2025-11-13 | start only with B, only text is scaled | [#12888](https://github.com/w3c/csswg-drafts/issues/12888) | [resolution](https://github.com/w3c/csswg-drafts/issues/12888#issuecomment-3524706648) |

## Key debates

### A `font-size` function or a separate fitting control?

The 2018 thread first considered `font-size: fit(8px, 48px)` or
`fit-width(8px, 48px)`. That shape naturally expresses lower and upper font-size bounds, but
Sergey Malkin pointed out that fitting can also vary `font-stretch`, a variable-font width
axis, or spacing. A control tied to `font-size` would prematurely make one fitting mechanism
the API itself ([early exchange](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-380541029)).

By 2023 Roman favored a dedicated property for three reasons: it exposes the expensive fitting
intent directly, falls back cleanly to the ordinary `font-size` if fitting is unsupported, and
leaves room for methods other than changing font size
([proposal](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-1481913805)). The April
2025 presentation consequently used `text-grow`, with the existing `font-size` as the minimum
and an optional maximum
([minutes](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512)).

### Grow-only, two property families, or one `text-fit`

The April proposal intentionally started with growth. Using the declared `font-size` as a floor
gave readable fallback behavior and avoided fitting text downward into illegibility. Ian
Kilpatrick nevertheless recorded a real shrink use case: authors often start from a preferred
large size, then need long content or translations to contract into a constrained area
([F2F minutes](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512)).

Chrome's prototype therefore proposed parallel APIs:

- `text-grow-target` / `text-grow-limit` / `text-grow`, because growth consumes free space
  ([Chrome feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019)).
- `text-shrink-target` / `text-shrink-limit` / `text-shrink`, because shrinking handles
  overflowing content and needs its own lower bound
  ([Chrome feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019)).

Roman first argued that shrinking was behaviorally redundant—authors could choose a small base
size and grow—but accepted that this inverted the natural authoring model for important cases.
His alternative kept both capabilities while making direction a required keyword:
`text-fit: grow` or `text-fit: shrink`
([#12887](https://github.com/w3c/csswg-drafts/issues/12887)). A single property avoided
duplicating target, limit, and future fitting-method controls, and made grow and shrink
mutually exclusive rather than two interacting adjustments.

The room was not unanimous. The minutes record [fantasai](../people/fantasai.md) preferring two
properties plus a shorthand, while [frivoal](../people/frivoal.md) argued that a single property
could rule out nonsensical combinations and better accommodate later controls. Miriam Suzanne
and Emilio Cobos Alvarez stressed that unbounded shrinking could become user-hostile
([discussion](https://github.com/w3c/csswg-drafts/issues/12887#issuecomment-3524628665)).
The resulting resolution was explicitly provisional: **“use text-fit for now”**.

### Why a 200% default limit was proposed—and why it is not the default

Full-page zoom can reduce the CSS viewport width. If text fitting responds by reducing its
font size to keep occupying the same physical-width container, it can cancel the user's attempt
to enlarge the text. Patrick H. Lauke demonstrated this and tied it to WCAG 2.2 SC 1.4.4
([demonstration](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2770253414)).

Roman proposed limiting fitting growth to 200% of the unfitted `font-size`. The arithmetic was
intended to let browser zoom “catch up”: if fitting can enlarge text by at most 2× and a browser
can zoom to at least 4×, the worst-case final enlargement relative to the initially fitted text
can still reach 2× (`4 / 2 = 2`)
([proposal](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2784658224)). The limit
would be a soft default, not a cap on browser zoom.

The proposal remains disputed in [#12886](https://github.com/w3c/csswg-drafts/issues/12886):

- Kent Tamura showed that ordinary zoom steps can reduce the fitting factor before reaching the
  cap, so the cap does not make text grow continuously with zoom
  ([comment](https://github.com/w3c/csswg-drafts/issues/12886#issuecomment-3573573251)).
- Accessibility reviewers objected that 200% is a conformance threshold, not a maximum user
  need, and that a 500% browser setting should not yield only 200% apparent growth
  ([comment](https://github.com/w3c/csswg-drafts/issues/12886#issuecomment-3629143152)).
- Chrome proposed preserving at least the 100%-zoom fitted physical size during later zoomed
  layouts, but that requires extra layout and raises questions about rewrapping, overflow,
  reload stability, CSS `zoom`, and performance
  ([F2F discussion](https://github.com/w3c/csswg-drafts/issues/12886#issuecomment-3814480919)).

The current draft therefore only provides an **optional** percentage clamp: for `grow`, a
percentage at or above 100% is a maximum factor; for `shrink`, a percentage from 0% through
100% is a minimum factor. Omitting it means no limit. The draft explicitly says there is no
agreement yet on browser zoom
([Editor's Draft](https://drafts.csswg.org/css-text-5/#text-fit-property)).

### What scales: font-dependent layout or only text?

Roman wanted font-relative descendants and decorations to follow the fitted font size: an icon
sized in `em`, optical sizing, spacing, padding, and margins should not visually detach from the
text. Chrome explained that fitting runs after style computation and line breaking, when engines
generally retain resolved lengths but not whether they came from `em`, `px`, or a mixed
`calc()`. Recomputing styles could be costly and can become non-linear
([#12888](https://github.com/w3c/csswg-drafts/issues/12888)).

The implementation-oriented compromise was a used-value operation:

- Do not change the exposed computed `font-size`; work during layout
  ([Kent's analysis](https://github.com/w3c/csswg-drafts/issues/12888#issuecomment-3383952254)).
- Make an approximate font-size/shaping pass and finish with geometric scaling rather than
  iterating without a bound
  ([Tab Atkins's shaping explanation](https://github.com/w3c/csswg-drafts/issues/12888#issuecomment-3412949937)).
- Initially scale only text (“option B”), leaving more ambitious font-relative recomputation
  for later
  ([resolution](https://github.com/w3c/csswg-drafts/issues/12888#issuecomment-3524706648)).

The draft now includes text and spacing whose inline size is proportional to the **used**
font-size among its scalable parts, but excludes atomic inlines and inline padding, border, and
margin ([Editor's Draft](https://drafts.csswg.org/css-text-5/#text-fit-property)).

### `consistent`, `per-line`, and the last line

Two visual goals competed from the first serious design: preserve one typographic size across a
block, or make every line independently fill its width. The former is cheaper and calmer;
the latter enables poster-like typography after responsive wrapping
([April 2025 minutes](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-2769621512)).

Chrome's prototype found a further distinction necessary:

- `consistent` uses one factor for all lines
  ([prototype feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019)).
- `per-line` independently fits ordinary lines but leaves the last and forced-break lines
  alone, avoiding a short final word becoming enormous
  ([prototype feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019)).
- `per-line-all` fits every line when that effect is intentional
  ([prototype feedback](https://github.com/w3c/csswg-drafts/issues/2528#issuecomment-3336857019)).

All three survived into the current grammar; `consistent` is assumed when no scope keyword is
given ([Editor's Draft](https://drafts.csswg.org/css-text-5/#text-fit-property)).

### Why the feature moved from Fonts 5 to Text 5

The April 2025 meeting initially chose Fonts 5 because changing font size and variable-font
axes dominated the discussion. After implementation work, Chrome argued that fitting consumes
shaping results but adjusts layout after line breaking; it does not primarily define font
selection or rendering. That made it analogous to `text-align` and a better fit for CSS Text
([#12885](https://github.com/w3c/csswg-drafts/issues/12885)).

[Dominik Röttsches](https://github.com/drott) and
[Chris Lilley](../people/svgeesus.md) supported the move, and the Working Group resolved on
2025-11-13 that it would use CSS Text Level 5
([discussion and resolution](https://github.com/w3c/csswg-drafts/issues/12885#issuecomment-3524545760)).

## Related features

- **Shrink-to-fit container sizing** — the inverse operation: change a container's intrinsic
  inline size to the widest already-wrapped line rather than changing text size. Chrome's
  `max-content-sizing: shrink-to-fit` explainer is an early sketch attached to
  [#191](https://github.com/w3c/csswg-drafts/issues/191), with no CSSWG resolution yet.
- **Text justification** — `text-align: justify` fills line width by changing spacing;
  `text-fit` changes the used font size and runs before justification
  ([Editor's Draft](https://drafts.csswg.org/css-text-5/#text-fit-property)).
- **Vertical fitting** — fitting text to a constrained block size or line count is requested
  separately in [#5515](https://github.com/w3c/csswg-drafts/issues/5515); the current feature
  fits the inline axis.
- Host module: [CSS Text Module Level 5](../specs/css-text-5.md).

## Sources

Primary GitHub threads (local mirror + public issue):

- [#2528 Feature for making text always fit the width of its parent](../../raw/data/github/csswg-drafts/issues/02xxx/02528.md)
  ([GitHub](https://github.com/w3c/csswg-drafts/issues/2528)) — original request, incubation,
  accessibility debate, Chrome feedback, and prototype reports.
- [#12885 Which spec?](../../raw/data/github/csswg-drafts/issues/12xxx/12885.md)
  ([GitHub](https://github.com/w3c/csswg-drafts/issues/12885)).
- [#12886 Default scaling limit](../../raw/data/github/csswg-drafts/issues/12xxx/12886.md)
  ([GitHub](https://github.com/w3c/csswg-drafts/issues/12886), open).
- [#12887 Shrinking and growing](../../raw/data/github/csswg-drafts/issues/12xxx/12887.md)
  ([GitHub](https://github.com/w3c/csswg-drafts/issues/12887)).
- [#12888 Scaling font-dependent things](../../raw/data/github/csswg-drafts/issues/12xxx/12888.md)
  ([GitHub](https://github.com/w3c/csswg-drafts/issues/12888)).

Specification: [CSS Text Level 5 Editor's Draft, `text-fit`](https://drafts.csswg.org/css-text-5/#text-fit-property).
Level 5 has not yet had a W3C TR publication and therefore has no
`raw/data/w3c-api/specifications/css-text-5.json` snapshot.

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
