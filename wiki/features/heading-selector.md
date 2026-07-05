---
title: ":heading() Selector"
slug: heading-selector
kind: feature
status: specified   # in Selectors 5 (FPWD 2026-02-17, #headings); syntax churned an+b -> integers; still Needs Edits / Needs Testcase
specs: [selectors-5]
spec_history:
  - {spec: selectors-4, from: "2024-05"}   # proposed against L4
  - {spec: selectors-5, from: "2026-05"}   # retagged as L4 stabilizes toward Rec (#12412)
key_people: [keithamus, tabatkins, annevk, lea, astearns, dbaron]
key_issues: [10296, 12599, 12412]
first_seen: "2024-05"   # #10296; the level-selector idea is older (see #351, 2016)
resolutions_count: 3    # 2x #10296 F2F (2025-04-03) + 1x #12599; only #12599 is in resolutions-index (see Resolutions note)
families: []
coverage: {github: full, www-style: n/a, member_era: n/a}   # entirely post-2016 GitHub era
generated_by: llm
---

## Overview

`:heading()` is a proposed structural pseudo-class (Selectors 5) that selects heading
elements by their **computed heading level** rather than by tag name. `:heading(2)` matches
any heading exposed as level 2; the argument-less `:heading` matches all headings. It is a
CSS-side companion to a *host-language* feature, not a standalone idea: it exists because
the WHATWG HTML `headingoffset` attribute ([whatwg/html#5033](https://github.com/whatwg/html/issues/5033))
decouples a heading's level from its element name.

`headingoffset` shifts the heading level a subtree exposes, and it accumulates down a flat-tree
walk: `<div headingoffset=1><h1></h1></div>` is a level-2 heading, and
`<div headingoffset=1><div headingoffset=2><h1></h1></div></div>` is level 4 (1+2+1). Once the
level no longer equals the tag name, `h2 {}` stops reliably meaning "style level-2 headings,"
so [keithamus](../people/keithamus.md) proposed a selector that matches the *offset-adjusted*
level ([#10296](https://github.com/w3c/csswg-drafts/issues/10296)). The proposal deliberately
sidesteps the ghost of the abandoned HTML5 document-outline algorithm: the argument is that
because `headingoffset` is **explicit and opt-in**, styling by computed level does not
reintroduce the outline algorithm's implicitness.

The feature is small in surface but drew three separate fights: how specific the selector
should be, what its argument grammar is, and whether it should follow the accessibility tree.

## Milestones

| date | milestone | source |
|---|---|---|
| 2016-07-28 | Prior art: [Crissov](https://github.com/w3c/csswg-drafts/issues/351) proposes `:level(an+b)` for hierarchical level | [#351](https://github.com/w3c/csswg-drafts/issues/351) |
| 2019-02-02 | Prior art: [tabatkins](../people/tabatkins.md) proposes `:role()` (incl. `role=heading`) | [#3596](https://github.com/w3c/csswg-drafts/issues/3596) |
| 2024-05-08 | [keithamus](../people/keithamus.md) opens [#10296](https://github.com/w3c/csswg-drafts/issues/10296) proposing `:heading(n)` for `headingoffset` | [#10296](https://github.com/w3c/csswg-drafts/issues/10296) |
| 2025-04-03 | F2F resolves to add `:heading()` (comma-separated an+b) with class-level specificity | [resolution](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2775988542) |
| 2025-06-27 | [#10296](https://github.com/w3c/csswg-drafts/issues/10296) and the older [#351](https://github.com/w3c/csswg-drafts/issues/351) closed as work consolidates into the spec | [#10296](https://github.com/w3c/csswg-drafts/issues/10296) |
| 2025-08-13 | [annevk](../people/annevk.md) opens [#12599](https://github.com/w3c/csswg-drafts/issues/12599) "Reconsider `<An+B>#` for :heading" | [#12599](https://github.com/w3c/csswg-drafts/issues/12599) |
| 2025-08-21 | WG reverses the grammar: `:heading()` takes a **list of integers**, not an+b | [resolution](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3209671569) |
| 2026-02-17 | `:heading` / `:heading()` carried in Selectors 5 FPWD (`#headings`) | [WD-selectors-5-20260217](https://www.w3.org/TR/2026/WD-selectors-5-20260217/) |
| 2026-05-27 | Selectors 4 stabilizing toward Rec; the proposal is re-tagged Selectors 5 | [comment](https://github.com/w3c/csswg-drafts/issues/12412#issuecomment-4558711489) |

## Resolutions

Chronological. The first two are quoted verbatim from the css-meeting-bot comment (the primary
source per the source-precedence table); note they are **not** present in
`_generated/resolutions-index.jsonl` — the bot recorded them as a `* ``RESOLVED: …`` `
bullet/back-tick list, a shape the index builder does not capture, which is also why
[#10296](https://github.com/w3c/csswg-drafts/issues/10296) shows `has_resolution: false`.
`/lint` R1 will flag these until the index build handles that shape.

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2025-04-03 | Add `:heading()` that accepts a comma-separated list of an+b expressions | [#10296](https://github.com/w3c/csswg-drafts/issues/10296) | [link](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2775988542) |
| 2025-04-03 | `:heading()` has the expected class-level specificity | [#10296](https://github.com/w3c/csswg-drafts/issues/10296) | [link](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2775988542) |
| 2025-08-21 | change spec to list of integers | [#12599](https://github.com/w3c/csswg-drafts/issues/12599) | [link](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3209671569) |

## Key debates

### Why a selector at all — the `headingoffset` motivation

The whole feature is downstream of `headingoffset`. Its intent, as summarised in
[#12412](https://github.com/w3c/csswg-drafts/issues/12412), is to let the same heading markup
appear at different levels in different contexts. [keithamus](../people/keithamus.md) stresses
a subtlety that shapes everything else: `headingoffset` changes the heading level held as
**element state**, and the accessibility tree merely *reads* that state to expose it to AT APIs
— "the Layout Tree will not influence the Accessibility Tree … and the Accessibility Tree will
not influence the Layout Tree (ever)"
([comment](https://github.com/w3c/csswg-drafts/issues/12412#issuecomment-3015994058)). So
`:heading()` selects on the element's own computed level, and the styling use case (visually
differentiated headings) is itself framed as accessibility, not merely AT ergonomics.

### Class-level vs tag-level specificity

The contested point at the 2025-04-03 F2F. UA stylesheets style headings by tag name, which
carries **tag-level** specificity; a pseudo-class defaults to **class-level**. The minutes
record [tabatkins](../people/tabatkins.md) raising the risk that if UAs migrate `h1…h6 {}` to
`:heading {}`, author styles could be unexpectedly overridden because the new UA rule would win
at class specificity ([minutes](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2775988542)).
Positions the minutes record:

- [kizu](../people/kizu.md): it is "basically an alias to the adjusted tag names," so tag
  specificity makes sense.
- [emilio](../people/emilio.md) and [bramus](../people/bramus.md): a pseudo-class with
  tag specificity is odd; prefer **consistency** (class-level, like attribute selectors)
  "unless we find out it breaks lots of things."
- [dbaron](../people/dbaron.md): this is "adding more magic, and probably isn't worth more
  magic" — the learning/understanding overhead outweighs the benefit. The minutes note the
  sense of the room agreed an exception was not motivated enough.
- [astearns](../people/astearns.md): since class-level "is what falls out of the definition,"
  record it.

**Resolved 2025-04-03:** *"`:heading()` has the expected class-level specificity"*
([resolution](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2775988542)). After
the meeting [lea](../people/lea.md) commented that tag-level *may* be worth the inconsistency
(a weak opinion), but agreed with [astearns](../people/astearns.md) that letting the presence
of an argument switch the specificity "violates the principle of least surprise"
([comment](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2781543700)).

A related thread of confusion: chriskirknielsen and valtlai asked whether an element-level
variant should be spelled `::heading` (a pseudo-*element*, which already has 0,0,1 specificity),
and romainmenke asked whether the discussion had conflated pseudo-element vs pseudo-class.
[astearns](../people/astearns.md) closed this off: the class-level resolution applies to
`:heading` **and** `:heading()`, and he "would object to having a switch that changed the
specificity based on whether arguments were provided"
([comment](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2778703697));
[keithamus](../people/keithamus.md) confirmed class-level for both
([comment](https://github.com/w3c/csswg-drafts/issues/10296#issuecomment-2780371111)).

### `<An+B>#` list vs list of integers — the reversal

The F2F had resolved on a comma-separated list of `an+b` expressions (with `:heading(n)` as a
shorthand). Four months later [annevk](../people/annevk.md) reopened it in
[#12599](https://github.com/w3c/csswg-drafts/issues/12599): a pseudo-class matching at most six
levels (maybe nine soon) does not justify the parsing/serialisation complexity of `<An+B>#`,
and `:heading(1), :heading(2), :heading(3)` works anyway. The debate:

- [tabatkins](../people/tabatkins.md): if forced to choose, prefer `<integer>#` over `<An+B>` —
  `an+b`'s power (even/odd, skipping) is useless for a small fixed set, while the gap between
  `:heading(1, 2, 3)` and `:is(:heading(1), :heading(2), :heading(3))` is large for a common
  case ([comment](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3184324721)).
- [keithamus](../people/keithamus.md): posted Firefox, csskit and Ladybird implementations to
  argue commas are *trivial* added complexity
  ([comment](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3184628491)).
- AtkinsSJ (Sam Atkins), who implemented `<An+B>#` in Ladybird: "didn't find it too bad … but
  it did feel weird to have it be different than the existing pseudo-classes," and later that
  `An+B#` "does feel like overkill for `:heading()`"
  ([comment](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3184123765)).
- [fantasai](../people/fantasai.md), [frivoal](../people/frivoal.md) (florian) and noamr backed
  a list of integers; noamr and [fantasai](../people/fantasai.md) cited precedent for
  comma-separated arguments (`active-view-transition-type()`, `:lang()`, `:not()`).
- [lea](../people/lea.md) argued for **ranges** (a-to-b) instead of bare commas, pointing at the
  long-standing range request [#4140](https://github.com/w3c/csswg-drafts/issues/4140);
  [astearns](../people/astearns.md) ruled ranges out of scope for this issue.

The minutes record a poll landing mostly on option "2" (list of integers), with
[emilio](../people/emilio.md) weakly preferring the `an+b` list and several no-preferences.
**Resolved 2025-08-21:** *"change spec to list of integers"*
([resolution](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3209671569)).

### Should `:heading()` follow the accessibility tree?

From the opening post [keithamus](../people/keithamus.md) held that `aria-level` and
`role=heading` should **not** affect `:heading()` — those are already selectable and ARIA
should not have "that dramatic an impact on other selectors." In
[#12412](https://github.com/w3c/csswg-drafts/issues/12412) extra808 pushed back: if the point
is to align styling with accessibility-tree heading levels, the selector should include *all*
headings in that tree regardless of how they got there (including `role=heading`).
[keithamus](../people/keithamus.md)'s rebuttal
([comment](https://github.com/w3c/csswg-drafts/issues/12412#issuecomment-3015994058)):

- Making `:heading` a shorthand for `h1,…,h6,[role=heading]` would be **wrong**, because it
  would wrongly match elements like `<legend role=heading>`; the real role computation is done
  by the accessibility engine, which is not always running (it has a performance cost).
- Exposing computed roles in CSS generally is what [#3596](https://github.com/w3c/csswg-drafts/issues/3596)
  (`:role()`) tracks, and no implementor has agreed to lift that logic into the main runtime.
- TL;DR: beyond "theoretical purity," the layering and performance complexity make it
  infeasible. This issue is still **open**.

### Prior art and the document-outline ghost

The idea of selecting by hierarchical level predates `headingoffset`.
[Crissov](https://github.com/w3c/csswg-drafts/issues/351)'s `:level(an+b)`
([#351](https://github.com/w3c/csswg-drafts/issues/351), 2016) and
[tabatkins](../people/tabatkins.md)'s `:role()`
([#3596](https://github.com/w3c/csswg-drafts/issues/3596), from a 2014 F2F) are the antecedents.
The [#10296](https://github.com/w3c/csswg-drafts/issues/10296) minutes record
[tabatkins](../people/tabatkins.md) noting an earlier `:heading` idea tied to the outline
algorithm that "eventually got dropped," now "relevant again" because of the HTML attribute —
and stressing that anything done here should be **contingent on the HTML feature actually
happening**. `#351` and `#10296` were both closed on 2025-06-27 as the surviving design moved
into Selectors 5.

## Related features

- **`headingoffset`** — the motivating WHATWG HTML attribute
  ([whatwg/html#5033](https://github.com/whatwg/html/issues/5033)); not a CSSWG deliverable.
- **`:role()`** ([#3596](https://github.com/w3c/csswg-drafts/issues/3596)) and **`:level()`**
  ([#351](https://github.com/w3c/csswg-drafts/issues/351)) — related structural pseudo-classes;
  `:role()` is the tracking issue for exposing the accessibility role in CSS.
- Host module: [Selectors Level 5](../specs/selectors-5.md).

## Sources

Primary (GitHub issue threads, mirrored):

- [#10296 Adding a `:heading()` selector for headingoffset?](../../raw/data/github/csswg-drafts/issues/10xxx/10296.md) — proposal + F2F resolutions.
- [#12599 Reconsider `<An+B>#` for :heading](../../raw/data/github/csswg-drafts/issues/12xxx/12599.md) — the grammar reversal.
- [#12412 :heading() selector and the accessibility tree](../../raw/data/github/csswg-drafts/issues/12xxx/12412.md) — the a11y-tree debate (open).
- [#351 :level(an+b)](../../raw/data/github/csswg-drafts/issues/00xxx/00351.md) and [#3596 :role()](../../raw/data/github/csswg-drafts/issues/03xxx/03596.md) — prior art.

Spec location: Selectors 5 `#headings` (per [Loirooriol](https://github.com/w3c/csswg-drafts/issues/12599#issuecomment-3209652583)),
<https://drafts.csswg.org/selectors-5/#headings>. Status: `raw/data/w3c-api/specifications/selectors-5.json`
(`snapshot_at: 2026-07-04`).

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
