---
title: Absolute Lengths & the Pixel Unit
slug: absolute-lengths
kind: feature
status: shipped
specs: [css-values-3, css-values-4]
spec_history:
  - {spec: css-values-3, from: "2001-07"}
  - {spec: css-values-4, from: "2018-08"}
key_people: [fantasai, frivoal, tabatkins, patrickhlauke, nicksherman]
key_issues: [614, 708, 5221]
first_seen: "2008-04"
resolutions_count: 3
families: []
coverage: {github: full, www-style: partial, member_era: none}
generated_by: llm
---

# Absolute Lengths & the Pixel Unit

## Overview

CSS's "absolute" length units (`px`, `in`, `cm`, `mm`, `pt`, `pc`, `Q`) form **one
system tied together by fixed ratios** — `1in = 96px = 2.54cm`, etc. They are
"absolute" only in the sense of being fixed *relative to each other*; the system as a
whole is anchored to physical reality through exactly **one** of them, the *anchor
unit*, and every other unit is derived from it. Which unit is the anchor depends on
the medium, and this is where the common intuition ("`px` is a physical dot on screen,
`cm` is a real centimetre") breaks down.

On **screen media the `px` is the anchor**, and it is defined not as a physical length
but as an approximation of a **visual angle** — the *reference pixel*, the angle
subtended by one pixel on a 96 dpi display viewed at arm's length (≈ 0.0213°). The
physical units then fall out of `px` at the fixed ratio, so on screen it is `cm` and
`in` that are *non-physical*. On **print / high-resolution media the physical unit is
the anchor** (an inch is a real inch) and `px` falls out as `1/96in`. Contrary to a
widespread belief, `px` was **never** defined as "one device pixel": it has been an
angular measure since CSS1 (see [Key debates](#key-debates)).

This arrangement is a deliberate, if reluctant, compromise. Making the physical units
follow `px` on screen (rather than being physically accurate) was forced by web
compatibility around 2009–2010, and repeated requests to introduce genuinely physical
units have been rejected as unimplementable and harmful to zoom/accessibility.

## Milestones

| date | milestone | source |
|---|---|---|
| 1996–1998 | `px` defined relative to a **viewing angle** since CSS1 / early CSS2 — never as a device or physical pixel | [fantasai](../people/fantasai.md), [#5221 (2020-07-23)](https://github.com/w3c/csswg-drafts/issues/5221#issuecomment-663282588) |
| 2008-04-09 | CSS2.1 wording: the pixel unit refers to the whole number of device pixels that best approximates the reference pixel | [www-style 2008Apr/0229](https://lists.w3.org/Archives/Public/www-style/2008Apr/0229.html) |
| 2010-06-23 | CSS2.1 Issue 149 resolved — `px` and physical units tied by a **fixed ratio** (`96px = 1in`) for web-compat; physical units stop being independently physical on screen | [www-style 2010Jun/0582](https://lists.w3.org/Archives/Public/www-style/2010Jun/0582.html) |
| 2016-10-17 | [#614](https://github.com/w3c/csswg-drafts/issues/614) filed: request for a way to address *actual physical size* | [#614](https://github.com/w3c/csswg-drafts/issues/614) |
| 2016-11-14 | [#708](https://github.com/w3c/csswg-drafts/issues/708) filed: spec should admit that high-dpi screens also anchor on `px`, not physical units | [#708](https://github.com/w3c/csswg-drafts/issues/708) |
| 2017-05-24 | [#708](https://github.com/w3c/csswg-drafts/issues/708) resolved — absolute-lengths section reworded so screen media (incl. high-resolution) anchor on `px` | [#708 bot](https://github.com/w3c/csswg-drafts/issues/708#issuecomment-303779713) |
| 2018-06-21 | [#614](https://github.com/w3c/csswg-drafts/issues/614) closed `Wontfix` — new physical-size units rejected | [#614](https://github.com/w3c/csswg-drafts/issues/614#issuecomment-254403012) |
| 2020-07-31 | [#5221](https://github.com/w3c/csswg-drafts/issues/5221) closed `Invalid` — the reference-pixel-as-visual-angle definition upheld | [#5221 (tabatkins)](https://github.com/w3c/csswg-drafts/issues/5221#issuecomment-666813821) |

## Resolutions

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2008-04-09 | RESOLVED: For (CSS2.1) ISSUE-1 http://www.w3.org/Style/CSS/Tracker/issues/1 Second wording proposal accepted: Insert before "It is recommended that the reference pixel be..." the sentence "It is recommended that the pixel unit refer to the whole number of device pixels that best approximates the reference pixel." | CSS2.1 ISSUE-1 | [www-style 2008Apr/0229](https://lists.w3.org/Archives/Public/www-style/2008Apr/0229.html) |
| 2010-06-23 | RESOLVED: Proposal accepted for CSS2.1 Issue 149 (Definitions of px and physical units) | CSS2.1 Issue 149 | [www-style 2010Jun/0582](https://lists.w3.org/Archives/Public/www-style/2010Jun/0582.html) |
| 2017-05-24 | RESOLVED: Move the close parens afte r"including high-resolution devices" | [#708](https://github.com/w3c/csswg-drafts/issues/708) | [permalink](https://github.com/w3c/csswg-drafts/issues/708#issuecomment-303779713) |

The 2008 and 2010 rows are **minutes-email** resolutions (scribe paraphrase, weaker than
bot comments); the 2017 row is a css-meeting-bot resolution. The `afte r"including` text
is verbatim from the bot, typo included.

## Key debates

### Is `px` a physical length or an angular measure?

The recurring confusion is whether `px` is "one dot on the display". It is not.

- **The spec position**: `px` is anchored to the *reference pixel*, "the visual angle of
  one pixel on a device with a pixel density of 96dpi and a distance from the reader of
  an arm's length". In [#5221](https://github.com/w3c/csswg-drafts/issues/5221) a
  commenter argued this is mathematically flawed because "an angle is not a length".
  [tabatkins](../people/tabatkins.md) closed it `Invalid`: the reference pixel *is* a
  viewing angle, and "when compared to lengths on a perpendicular surface … it
  represents the length that angle subtends on the surface, given the surface's viewing
  distance" — a common, unambiguous shorthand ([#5221, 2020-07-31](https://github.com/w3c/csswg-drafts/issues/5221#issuecomment-666813821)).
- **"px was always angular"**: [fantasai](../people/fantasai.md) rejected the premise
  that `px` used to mean one device pixel — "The pixel has always been defined relative
  to a viewing angle. See the definitions of length units in CSS1 and earlier (pre-2010)
  versions of CSS2" ([#5221, 2020-07-23](https://github.com/w3c/csswg-drafts/issues/5221#issuecomment-663282588)).
- **What changed in 2010 was the *physical* units, not `px`**: originally `px` and the
  physical units were independent (physical units physically accurate, `px` angular);
  too much content assumed 96 dpi, so the WG fixed the `96px = 1in` ratio, coupling the
  two. "None of us were pleased with the situation … but we were constrained by reality.
  The current spec is the compromise we ended up with"
  ([fantasai, #5221](https://github.com/w3c/csswg-drafts/issues/5221#issuecomment-663282588); history thread [www-style 2010Jan/0058](https://lists.w3.org/Archives/Public/www-style/2010Jan/0058.html)).

### Which unit is the anchor — screen vs print?

- [fantasai](../people/fantasai.md) summarised the two-category model in telecon:
  "css is based on 96 DPI and px is viewing angle … used to be independent but changed
  due to web compat … when you print, 12pt is actually 12pt … on screen we do the 96DPI
  thing and round to actual pixels to make it look nice"
  ([#708 IRC log, 2017-05-24](https://github.com/w3c/csswg-drafts/issues/708#issuecomment-303779713)).
  *(Minutes are a scribe paraphrase.)*
- [patrickhlauke](../people/patrickhlauke.md) filed [#708](https://github.com/w3c/csswg-drafts/issues/708)
  because the spec implied only "low-resolution / unusual viewing distance" screens
  anchor on `px`, whereas in reality *all* screens (incl. high-dpi phones, laptops) do —
  the physical units are the ones that don't map to real millimetres on screen.
  [frivoal](../people/frivoal.md) agreed: "what browsers do today is the right thing to
  do" ([#708, 2016-11-15](https://github.com/w3c/csswg-drafts/issues/708#issuecomment-260529072)).
- The contested edge case was **print at unusual viewing distances** (billboards,
  signage): should "12pt" be a physical 12pt, or scale with distance? The WG kept it a
  `should` (recommendation, not requirement) and merely moved a parenthesis so the
  categories read cleanly, leaving UAs latitude
  ([#708 bot, 2017-05-24](https://github.com/w3c/csswg-drafts/issues/708#issuecomment-303779713)).

### Should CSS get genuinely physical-size units?

- [nicksherman](../people/nicksherman.md) opened [#614](https://github.com/w3c/csswg-drafts/issues/614)
  arguing the inability to address physical size is a "glaring issue", proposing *new*
  units (not redefining `in`/`cm`) that map to real-world size.
- [frivoal](../people/frivoal.md) laid out the standing rejection rationale
  ([#614, 2016-10-18](https://github.com/w3c/csswg-drafts/issues/614#issuecomment-254403012)):
  (1) the current definitions are intentional, not an accident; (2) "small or large is
  mostly not a question of physical size, but rather … the percentage of the field of
  vision", which the angular `px` already captures; (3) real physical units would
  **break zoom** (zooming would no longer resize them, or users lose zoom); (4) browsers
  generally **don't know** the display's physical size (a moved projector changes it,
  and the OS can't report it). Closed `Wontfix` in 2018.

## Related features

- Depends on the same anchoring model as media features such as `resolution` and
  `device-pixel-ratio` (see resolutions in `_generated/resolutions-index.md`).
- Not yet ingested: `viewport-units`, `font-relative-lengths`.

## Sources

- Issues: [#614](https://github.com/w3c/csswg-drafts/issues/614),
  [#708](https://github.com/w3c/csswg-drafts/issues/708),
  [#5221](https://github.com/w3c/csswg-drafts/issues/5221)
  (mirrors under `raw/data/github/csswg-drafts/issues/`).
- Minutes emails: [www-style 2008Apr/0229](https://lists.w3.org/Archives/Public/www-style/2008Apr/0229.html),
  [www-style 2010Jun/0582](https://lists.w3.org/Archives/Public/www-style/2010Jun/0582.html),
  history thread [www-style 2010Jan/0058](https://lists.w3.org/Archives/Public/www-style/2010Jan/0058.html).
- Spec: [css-values-4 §absolute-lengths](https://drafts.csswg.org/css-values-4/#absolute-lengths)
  ([css-values-3](../specs/css-values-3.md), [css-values-4](../specs/css-values-4.md)).

**Coverage note**: GitHub-era discussion is fully read; the pre-2010 www-style threads
are cited from the minutes index but not deep-read (`www-style: partial`). The CSS1/CSS2
*deliberation* over the original `px` definition falls in the member-confidential minutes
era and is **not reconstructed** here (`member_era: none`) — the CSS1 origin is stated on
the authority of [fantasai](../people/fantasai.md)'s account, not primary minutes.

---

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
