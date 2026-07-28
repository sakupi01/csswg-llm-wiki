---
title: The flex Shorthand & its Longhands
slug: flex-shorthand
kind: feature
status: shipped
specs: [css-flexbox-1]
spec_history:
  - {spec: css-flexbox-1, from: "2012-05"}
key_people: [tabatkins, fantasai, dholbert]
key_issues: [2710, 5742, 6639]
first_seen: "2012-05"
resolutions_count: 3
families: []
coverage: {github: partial, www-style: partial, member_era: none}
generated_by: llm
---

# The `flex` Shorthand & its Longhands

## Overview

css-flexbox-1 tells authors, unusually loudly for a CSS spec, to prefer a shorthand
over its own longhands:

> Authors are encouraged to control flexibility using the flex shorthand rather than
> with its longhand properties directly, as the shorthand correctly resets any
> unspecified components to accommodate common uses.
> — [css-flexbox-1 §flex-common (ED)](https://drafts.csswg.org/css-flexbox/#flex-common)

The reason is that the shorthand is deliberately "magic": components omitted from
`flex` get defaults **different from the longhands' initial values**, tuned so that the
common one-liners do the right thing (`flex: 1` → `1 1 0`, absolute flex; `flex: 200px`
→ `1 1 200px`, grow from a basis). Setting a longhand alone (e.g. only `flex-grow: 1`)
leaves the other components at their initial values and silently misses that tuning.

Historically the shorthand came *first*: `flex` began as a single three-component
property, and the longhands were only split out at the Hamburg F2F (2012-05-10), at
Microsoft's request — per [fantasai](../people/fantasai.md), "mainly added to
facilitate scripting" ([#6639](https://github.com/w3c/csswg-drafts/issues/6639#issuecomment-1220029390)).
The "authors are encouraged" sentence has been in the spec since the first CR
(2012-09-18). The magic itself was contested (Alex Mogilevsky argued shorthands should
"set what I specify"), was consciously kept, and still has one live sharp edge: the
omitted-`flex-basis` value, spec'd as `0` but shipped as `0%` ([#5742](https://github.com/w3c/csswg-drafts/issues/5742), open).

## Milestones

| date | milestone | source |
|---|---|---|
| 2012-05-10 | Hamburg F2F splits the single `flex` property into `flex-grow`/`flex-shrink`/`flex-basis`, making `flex` a shorthand; the minutes record the omitted-basis magic (`0px`, not `auto`) as intentional "so that `flex: 1;` continues to do absolute flex" | [www-style 2012May/0520](https://lists.w3.org/Archives/Public/www-style/2012May/0520.html) |
| 2012-06-06 | Telecon straw poll changes the initial value to `0 1 auto` (inflexible for growth, flexible for shrink); omitted `flex-shrink` loses its magic and takes the initial value; Flexbox goes to LC | [www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html) |
| 2012-06-12 | Last Call WD published, per the 2012-06-06 "Publish Flexbox as LC" resolution | [TR dated URL](https://www.w3.org/TR/2012/WD-css3-flexbox-20120612/) |
| 2012-09-18 | First CR carries the recommendation verbatim ("Authors are encouraged to control flexibility using the 'flex' shorthand rather than with component properties…", §Components of Flexibility) | [CR 2012-09-18](https://www.w3.org/TR/2012/CR-css3-flexbox-20120918/) |
| 2018-05-31 | [tabatkins](../people/tabatkins.md) confirms on GitHub that the shorthand/longhand default divergence "is definitely intentional" | [#2710](https://github.com/w3c/csswg-drafts/issues/2710#issuecomment-393703566) |
| 2020-11-24 | [emilio](../people/emilio.md) opens [#5742](https://github.com/w3c/csswg-drafts/issues/5742): spec says omitted basis is `0`, browsers ship `0%` | [#5742](https://github.com/w3c/csswg-drafts/issues/5742) |
| 2022-08-18 | [fantasai](../people/fantasai.md) states the design rationale on the record: longhands were "mainly added to facilitate scripting" and "are more likely to get authors in trouble than using the shorthand" | [#6639](https://github.com/w3c/csswg-drafts/issues/6639#issuecomment-1220029390) |

## Resolutions

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2012-05-10 | RESOLVED: Split flex into flex-grow/flex-shrink/flex-basis | — | [www-style 2012May/0520](https://lists.w3.org/Archives/Public/www-style/2012May/0520.html) |
| 2012-06-06 | RESOLVED: initial value of 'flex' is "0 1 auto", editors to decide details among themselves. | — | [www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html) |
| 2012-06-06 | RESOLVED: Omitted flex-shrink in the flex shorthand always uses the initial value. | — | [www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html) |

All three are **minutes-email** resolutions (scribe record; pre-GitHub era, no issue
numbers). The index also carries the summary-line variant `initial value of 'flex' is
"0 1 auto"` from the same mail.

## Key debates

### Should the shorthand be "magic"? (2012)

When the Hamburg F2F split `flex` into longhands, the shorthand kept special behavior
inherited from the unified property: the minutes record Tab Atkins as explaining that
"there's special behavior in the shorthand: if you leave out flex-basis, it defaults
to '0px' rather than 'auto' (which is the initial value) … This is so that `flex: 1;`
continues to do absolute flex"
([www-style 2012May/0520](https://lists.w3.org/Archives/Public/www-style/2012May/0520.html)).

At the 2012-06-06 telecon the magic itself was challenged
([www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html)):

- **Against (Alex Mogilevsky, Microsoft — minutes nick `alexmog`)**: the minutes record
  him as saying "too much magic makes it difficult to use. I'd much prefer shorthands
  to set what I specify, and use defaults for whatever I don't specify."
- **For ([fantasai](../people/fantasai.md))**: the minutes record her as saying "I like
  the current shorthand behavior … I think this is limited magic. If you set only the
  flex-grow, it gives a special flex-basis. If you set only the flex-basis, it gives a
  special flex-grow. That's it."
- **Outcome**: the magic stayed, but was trimmed — the same meeting resolved that
  omitted `flex-shrink` (unlike grow/basis) always takes its initial value, and a straw
  poll (A: keep `1 1 auto` — sylvaing, [Rossen](../people/atanassov.md), rbetts, alexmog; B: `0 1 auto` —
  [fantasai](../people/fantasai.md), [tabatkins](../people/tabatkins.md), florianr, plus
  Ojan and [dholbert](../people/dholbert.md) on the mailing list; mass abstention)
  settled the initial value as `0 1 auto`.

The initial-value change was itself a reversal: Hamburg had made items flexible by
default (`1 1 auto`), Ojan (minutes nick) objected on www-style, and the `0 1 auto` compromise
(inflexible for growth, flexible for shrink, protecting layouts on narrow screens)
carried ([www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html)).

### Why do the longhand initial values differ from the shorthand's omitted defaults?

The divergence (initial `flex-grow: 0` / `flex-basis: auto`, but omitted-in-shorthand
`1` / `0`) confused enough readers to generate recurring GitHub issues. Both editors
answered on the record:

- [tabatkins](../people/tabatkins.md): "Yes, the different default value is definitely
  intentional; when you set something like `flex: 200px`, you want it to start at 200px
  and grow, so it needs to default to 1. But we want flex items to default to not
  growing at all, for simplicity, so the initial value is `0`"
  ([#2710, 2018-05-31](https://github.com/w3c/csswg-drafts/issues/2710#issuecomment-393703566)).
- The spec itself has carried a note since the 2012 CR: "Note that the initial values
  of 'flex-grow' and 'flex-basis' are different from their defaults when omitted in the
  'flex' shorthand. This so that the 'flex' shorthand can better accommodate the most
  common cases" (typo verbatim,
  [CR 2012-09-18](https://www.w3.org/TR/2012/CR-css3-flexbox-20120918/)). After
  [#6639](https://github.com/w3c/csswg-drafts/issues/6639) the note was moved to the top
  of the section for visibility.

### Where does "authors are encouraged" come from — was it resolved?

No WG resolution mints the sentence itself; it is editorial prose that entered between
the Hamburg split (2012-05) and the first CR (2012-09-18), where it reads: "Authors are
encouraged to control flexibility using the 'flex' shorthand rather than with component
properties, as the shorthand correctly resets any unspecified components to accommodate
common uses" ([CR §Components of Flexibility](https://www.w3.org/TR/2012/CR-css3-flexbox-20120918/)).
What *was* resolved is the divergence the sentence warns about (see Resolutions).
[fantasai](../people/fantasai.md) later made the intent explicit: "we wanted to strongly
recommend that authors use the shorthand rather than the longhands. (The longhands were
mainly added to facilitate scripting, and because of the way they are defaulted, are
more likely to get authors in trouble than using the shorthand.)"
([#6639, 2022-08-18](https://github.com/w3c/csswg-drafts/issues/6639#issuecomment-1220029390)).

### The live sharp edge: omitted `flex-basis` — `0` or `0%`? ([#5742](https://github.com/w3c/csswg-drafts/issues/5742), open)

A 2015 substantive spec change made the omitted basis unitless `0`; browsers never
followed and still ship `0%` — which behaves differently when the container's main size
is indefinite (`0%` can resolve to `content`, `0` collapses the item).
[dholbert](../people/dholbert.md) posted testcases showing content disappearing if
browsers adopted the spec'd `0`
([#5742, 2023-04-18](https://github.com/w3c/csswg-drafts/issues/5742#issuecomment-1513651204)),
and [bfgeek](../people/bfgeek.md) concluded "Fwiw - this likely isn't web compatible
anymore. Spec should be changed back to reflect reality"
([#5742, 2024-08-27](https://github.com/w3c/csswg-drafts/issues/5742#issuecomment-2311482423)).
The issue remains open (`Target Revision: Next`). It is exactly the class of trap the
shorthand recommendation exists to keep authors away from: the difference is invisible
in the `flex` one-liners and only bites when mixing longhands or edge values
(`flex: 0 0` parses the second `0` as `flex-shrink`, not a basis).

## Related features

- Not yet ingested: `flexbox` (the layout model itself — algorithm, `order`,
  alignment), `css-align-3` interactions.
- The `grid` shorthand later faced its own reset-vs-set debates (see resolutions index,
  2016).

## Sources

- Minutes emails:
  [www-style 2012May/0520](https://lists.w3.org/Archives/Public/www-style/2012May/0520.html)
  (Hamburg F2F Part I, mirror [../../raw/data/www-style/2012May/0520.md](../../raw/data/www-style/2012May/0520.md)),
  [www-style 2012Jun/0105](https://lists.w3.org/Archives/Public/www-style/2012Jun/0105.html)
  (telecon 2012-06-06, mirror [../../raw/data/www-style/2012Jun/0105.md](../../raw/data/www-style/2012Jun/0105.md)).
- Issues: [#2710](https://github.com/w3c/csswg-drafts/issues/2710)
  ([mirror](../../raw/data/github/csswg-drafts/issues/02xxx/02710.md)),
  [#5742](https://github.com/w3c/csswg-drafts/issues/5742)
  ([mirror](../../raw/data/github/csswg-drafts/issues/05xxx/05742.md)),
  [#6639](https://github.com/w3c/csswg-drafts/issues/6639)
  ([mirror](../../raw/data/github/csswg-drafts/issues/06xxx/06639.md)).
- Spec: [css-flexbox-1 §flex-common (ED)](https://drafts.csswg.org/css-flexbox/#flex-common),
  [CR 2012-09-18](https://www.w3.org/TR/2012/CR-css3-flexbox-20120918/)
  ([css-flexbox-1](../specs/css-flexbox-1.md)).

**Coverage note**: three GitHub issues and two minutes emails are deep-read; the wider
flexbox issue backlog is not (`github: partial`). The pre-2012 unified-`flex` era
(2009–2012 WDs, and the XUL/`box-flex` ancestry) is cited only through the 2012 minutes'
own account, not reconstructed (`www-style: partial`). The exact editorial commit that
introduced the "authors are encouraged" sentence falls in the pre-GitHub hg era and was
not traced; the sentence is bounded to 2012-05 – 2012-09 by the CR text.

---

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
