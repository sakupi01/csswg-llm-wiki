---
title: Scroll-driven Animations
slug: scroll-driven-animations
kind: feature
status: shipping    # Chromium shipped 2023; declarative model stable, spec still WD with active edits
specs: [scroll-animations-1]
spec_history:
  - {spec: scroll-animations-1, from: "2019-09"}   # moved from WICG scroll-timeline into csswg-drafts
key_people: [flackr, fantasai, miriam, birtles, majido]
key_issues: [6674, 7047, 7759, 8101, 5321, 13974]
first_seen: "2016-09"
resolutions_count: 88   # resolutions labeled scroll-animations-1 in resolutions-index
families: []
coverage: {github: full, www-style: none, member_era: n/a}   # WICG/GitHub-era feature
generated_by: llm
---

## Overview

Scroll-driven Animations let a CSS animation be driven by scroll position instead of time: as
you scroll, the animation advances. Two timeline kinds exist — a **scroll timeline** (progress
of a scroll container from 0–100%) and a **view timeline** (progress of a *subject element*
through the scrollport). Authors opt in either anonymously via the `scroll()` / `view()`
functions on `animation-timeline`, or by naming a timeline (`scroll-timeline-name` /
`view-timeline-name`) and referencing that name from an animated descendant.

The feature began outside the CSSWG as the Chrome-driven WICG *ScrollTimeline* effort and was
moved into `csswg-drafts` in 2019. Its defining moment came in **2021**, when
[fantasai](../people/fantasai.md) and [miriam](../people/miriam.md) reviewed the Editor's Draft,
found its offset-heavy imperative model hard to author, and proposed a **replacement declarative
syntax** — the `animation-timeline: scroll()` / named-timeline model that ships today. The WG
adopted that direction, added [flackr](../people/flackr.md) as editor, and moved the original
editor [Majid Valipour](../people/majido.md) to Former. The module reached FPWD in October 2022,
was renamed from "Scroll-linked" to "Scroll-driven" Animations soon after, and is implemented in
Chromium (which ran the origin trials that shaped it). The spec remains a Working Draft with
active edits: much of the 2025–2026 work is hardening the object model and aligning timeline-name
lookup with the rest of CSS.

## Milestones

| date | milestone | source |
|---|---|---|
| 2016-09-12 | Earliest tracked issue — scroll-timeline use-case rework, from the pre-CSSWG WICG effort | [#4354](https://github.com/w3c/csswg-drafts/issues/4354) |
| 2019-09-17 | `scroll-timeline` moved into `csswg-drafts` | [resolution](https://github.com/w3c/csswg-drafts/issues/4337#issuecomment-532120609) |
| 2021-09-29 | Declarative syntax rebooted: WG adopts fantasai/Miriam's direction; [flackr](../people/flackr.md) added as editor, [Majid](../people/majido.md) → Former | [resolution](https://github.com/w3c/csswg-drafts/issues/6674#issuecomment-930334244) |
| 2022-08-03 | Core named-timeline model resolved (scope = preceding siblings + ancestors; `scroll()` loses its container-name arg) | [#7047 res](https://github.com/w3c/csswg-drafts/issues/7047#issuecomment-1203984802), [#7046 res](https://github.com/w3c/csswg-drafts/issues/7046#issuecomment-1204014693) |
| 2022-10-25 | First Public Working Draft published | [WD-scroll-animations-1-20221025](https://www.w3.org/TR/2022/WD-scroll-animations-1-20221025/) |
| 2022-12-23 | Renamed "Scroll-linked" → "Scroll-driven" Animations | [resolution](https://github.com/w3c/csswg-drafts/issues/8101#issuecomment-1364275851) |
| 2023-05-17 | `scroll/view-timeline-attachment` removed in favor of `timeline-scope` | [resolution](https://github.com/w3c/csswg-drafts/issues/7759#issuecomment-1551709286) |
| 2023-06-06 | Latest Working Draft published | [WD-scroll-animations-1-20230606](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/) |
| 2026-06-10 | Timeline-name lookup made **loosely-matched** (aligns with view-transition / anchor scoping) | [resolution](https://github.com/w3c/csswg-drafts/issues/13974#issuecomment-4672119742) |

## Resolutions

Chronological; a curated set of the narrative-carrying resolutions (the spec has 88 resolutions
in the index). Text is verbatim from `_generated/resolutions-index.jsonl`.

| date | resolution (verbatim) | issue | permalink |
|---|---|---|---|
| 2019-09-17 | moved scroll-timeline into csswg-drafts | [#4337](https://github.com/w3c/csswg-drafts/issues/4337) | [link](https://github.com/w3c/csswg-drafts/issues/4337#issuecomment-532120609) |
| 2021-09-02 | We are going to start specifying a no motion at all mode that makes motion inducing animations discrete between keyframes where keyframes are sufficiently separated in time | [#5321](https://github.com/w3c/csswg-drafts/issues/5321) | [link](https://github.com/w3c/csswg-drafts/issues/5321#issuecomment-910924409) |
| 2021-09-29 | Adopt fantasai/miriam's new direction for the declarative side of scroll-linked animations | [#6674](https://github.com/w3c/csswg-drafts/issues/6674) | [link](https://github.com/w3c/csswg-drafts/issues/6674#issuecomment-930334244) |
| 2021-09-29 | Add [flackr](../people/flackr.md) as editor to scroll-animations, move Majid to Former | [#6674](https://github.com/w3c/csswg-drafts/issues/6674) | [link](https://github.com/w3c/csswg-drafts/issues/6674#issuecomment-930334244) |
| 2022-03-30 | Use percentages for scroll-timeline values | [#7045](https://github.com/w3c/csswg-drafts/issues/7045) | [link](https://github.com/w3c/csswg-drafts/issues/7045#issuecomment-1083384745) |
| 2022-08-03 | remove the container name argument from the scroll() function | [#7046](https://github.com/w3c/csswg-drafts/issues/7046) | [link](https://github.com/w3c/csswg-drafts/issues/7046#issuecomment-1204014693) |
| 2022-08-03 | scope of named timelines is across flattened tree | [#7047](https://github.com/w3c/csswg-drafts/issues/7047) | [link](https://github.com/w3c/csswg-drafts/issues/7047#issuecomment-1203984802) |
| 2022-08-03 | timeline search looks at preceding siblings and ancestors, recursively | [#7047](https://github.com/w3c/csswg-drafts/issues/7047) | [link](https://github.com/w3c/csswg-drafts/issues/7047#issuecomment-1203984802) |
| 2022-12-23 | Change “Scroll-linked Animations” to “Scroll-driven Animations” in scroll-animations-1 | [#8101](https://github.com/w3c/csswg-drafts/issues/8101) | [link](https://github.com/w3c/csswg-drafts/issues/8101#issuecomment-1364275851) |
| 2023-05-17 | remove scroll/view-timeline-attachment, add timeline-scope, which accepts a list of timeline names and raises their scope | [#7759](https://github.com/w3c/csswg-drafts/issues/7759) | [link](https://github.com/w3c/csswg-drafts/issues/7759#issuecomment-1551709286) |
| 2023-05-17 | Switch timeline names to <dashed-ident> | [#8746](https://github.com/w3c/csswg-drafts/issues/8746) | [link](https://github.com/w3c/csswg-drafts/issues/8746#issuecomment-1551701139) |
| 2025-04-03 | View timelines whose subject is the root element are always inactive (with the expectation we'll give them more behavior later) | [#4344](https://github.com/w3c/csswg-drafts/issues/4344) | [link](https://github.com/w3c/csswg-drafts/issues/4344#issuecomment-2776836246) |
| 2026-01-28 | name lookup for timeline-name, anchor-name, etc. walks up the ancestor chain (up to stopping point) first, then looks for last-defined within scope | [#13364](https://github.com/w3c/csswg-drafts/issues/13364) | [link](https://github.com/w3c/csswg-drafts/issues/13364#issuecomment-3812817974) |
| 2026-05-06 | unresolved timelines are represented in the OM as null | [#13807](https://github.com/w3c/csswg-drafts/issues/13807) | [link](https://github.com/w3c/csswg-drafts/issues/13807#issuecomment-4390005560) |
| 2026-05-27 | Scroll and view timelines don't become inactive when there's no scroll range | [#9256](https://github.com/w3c/csswg-drafts/issues/9256) | [link](https://github.com/w3c/csswg-drafts/issues/9256#issuecomment-4556112966) |
| 2026-06-03 | changes to scroll timeline source happen async | [#13480](https://github.com/w3c/csswg-drafts/issues/13480) | [link](https://github.com/w3c/csswg-drafts/issues/13480#issuecomment-4614087368) |
| 2026-06-03 | when VT is on fragmented subjects, it includes boudning box of fragmetns (matching INtersectionObserver) | [#13818](https://github.com/w3c/csswg-drafts/issues/13818) | [link](https://github.com/w3c/csswg-drafts/issues/13818#issuecomment-4614144930) |
| 2026-06-03 | start/endOffset are nullable | [#13844](https://github.com/w3c/csswg-drafts/issues/13844) | [link](https://github.com/w3c/csswg-drafts/issues/13844#issuecomment-4614158334) |
| 2026-06-10 | Make scroll timeline names loosely-matched | [#13974](https://github.com/w3c/csswg-drafts/issues/13974) | [link](https://github.com/w3c/csswg-drafts/issues/13974#issuecomment-4672119742) |

## Key debates

### The 2021 declarative reboot: element positions over explicit offsets

The single most consequential turn in this feature's history. In
[#6674](https://github.com/w3c/csswg-drafts/issues/6674) (2021-09),
[fantasai](../people/fantasai.md) and [miriam](../people/miriam.md) reviewed the existing
Scroll-linked Animations ED and raised two authoring concerns, explicitly analogising to Robert
O'Callahan's critique of the original CSS Snap Points that became CSS Scroll Snap:

- the model "seems to rely a lot on explicit offsets, rather than on element positions" —
  yet the reason authors reach for offsets is usually to line up with elements;
- element-based offsets existed but relied on **ID selectors**, which "are not particularly
  portable across pages" and prevent reusing styles in multiple places.

Their counter-proposal split scroll-linked timelines into two kinds and introduced the inline
functional notation still in use — `animation-timeline: scroll(<axis>? <scroller>?)` for the
nearest/root/named scroller, plus named `scroll-timeline-*` properties for the reusable,
indirect case ([proposal](https://github.com/w3c/csswg-drafts/issues/6674)). It was framed as
part of a larger "timelines" rethink on the CSSWG wiki. **Resolved 2021-09-29**: *"Adopt
fantasai/miriam's new direction for the declarative side of scroll-linked animations"*, with a
companion resolution adding [flackr](../people/flackr.md) as editor and moving
[Majid Valipour](../people/majido.md) to Former
([resolution](https://github.com/w3c/csswg-drafts/issues/6674#issuecomment-930334244)). This is
why today's syntax is declarative and element-oriented rather than offset-and-ID based.

### Naming timelines: how far does a name reach?

Once timelines could be *named*, the group had to define how a `animation-timeline: --foo`
reference finds its `--foo`. This has been reopened repeatedly, and the scope has narrowed and
re-widened over four years:

- **2022-08-03 ([#7047](https://github.com/w3c/csswg-drafts/issues/7047)):** the original model —
  *"scope of named timelines is across flattened tree"*, where *"timeline search looks at
  preceding siblings and ancestors, recursively"*
  ([resolution](https://github.com/w3c/csswg-drafts/issues/7047#issuecomment-1203984802)). At the
  same meeting `scroll()` lost its container-name argument
  ([#7046](https://github.com/w3c/csswg-drafts/issues/7046#issuecomment-1204014693)).
- **2023 ([#7759](https://github.com/w3c/csswg-drafts/issues/7759)):** an explicit
  `scroll-timeline-attachment` / `view-timeline-attachment` mechanism was first added, then
  **removed** and replaced by `timeline-scope`, "which accepts a list of timeline names and
  raises their scope"
  ([resolution](https://github.com/w3c/csswg-drafts/issues/7759#issuecomment-1551709286)). Timeline
  names were also switched to `<dashed-ident>`
  ([#8746](https://github.com/w3c/csswg-drafts/issues/8746#issuecomment-1551701139)).
- **2026 ([#13974](https://github.com/w3c/csswg-drafts/issues/13974)):** [dshin-moz](https://github.com/dshin-moz)
  observed that with a later `#13364` resolution making names visible to ancestors *without*
  `timeline-scope`, the still-present flat-tree wording meant a shadow tree's timeline reference
  could "suddenly attach to another shadow tree's scroll timeline" purely by flat-tree order — an
  encapsulation leak. The minutes record [emilio](../people/emilio.md) proposing to *"make it a
  loosely matched scoped name (so, what view transitions do)"*. **Resolved 2026-06-10**: *"Make
  scroll timeline names loosely-matched"*
  ([resolution](https://github.com/w3c/csswg-drafts/issues/13974#issuecomment-4672119742)) —
  bringing timeline scoping into line with view transitions and anchor positioning rather than
  keeping a bespoke flat-tree rule.

### "Scroll-linked" vs "Scroll-driven"

A small but deliberate rename. [fantasai](../people/fantasai.md) opened
[#8101](https://github.com/w3c/csswg-drafts/issues/8101) (2022-11) arguing "driven" is clearer
because it avoids confusion with *scroll-triggered* animations (which merely start on scroll).
The minutes/thread record [birtles](../people/birtles.md) noting the group had originally
considered "scroll-driven" but chose "linked" as friendlier and more "encompassing" — back when
the design still included scroll *triggers* and hand-off between scroll- and time-based
animations. With those broader ambitions gone, [bramus](../people/bramus.md) and others favoured
"driven" since scroll-driven and scroll-triggered are both "linked" to scroll. **Resolved
2022-12-23**: rename to *"Scroll-driven Animations"*
([resolution](https://github.com/w3c/csswg-drafts/issues/8101#issuecomment-1364275851)).

### Accessibility: reduced motion

[#5321](https://github.com/w3c/csswg-drafts/issues/5321) (TAG feedback) raised the interaction
with `prefers-reduced-motion`. **Resolved 2021-09-02** to *"start specifying a no motion at all
mode that makes motion inducing animations discrete between keyframes where keyframes are
sufficiently separated in time"*
([resolution](https://github.com/w3c/csswg-drafts/issues/5321#issuecomment-910924409)) — i.e. a
mode that snaps between keyframes rather than smoothly interpolating, so a scroll-driven effect
does not become an involuntary motion source for users who opted out.

### Inactive timelines and the 2025–2026 object-model hardening

Much recent work pins down edge cases in the timeline lifecycle and its Web Animations / CSSOM
surface, several of which are author-visible:

- **Root-subject view timelines** are *"always inactive"*
  ([#4344](https://github.com/w3c/csswg-drafts/issues/4344#issuecomment-2776836246), 2025-04).
- **No scroll range** — timelines *don't* become inactive merely because there is no scrollable
  range ([#9256](https://github.com/w3c/csswg-drafts/issues/9256#issuecomment-4556112966),
  2026-05), and an unresolved timeline is *"represented in the OM as null"*
  ([#13807](https://github.com/w3c/csswg-drafts/issues/13807#issuecomment-4390005560), 2026-05).
- **Async source changes** — *"changes to scroll timeline source happen async"*
  ([#13480](https://github.com/w3c/csswg-drafts/issues/13480#issuecomment-4614087368), 2026-06).
- **Fragmented subjects** — a view timeline on a fragmented subject uses the bounding box of the
  fragments, *"matching INtersectionObserver"* [sic]
  ([#13818](https://github.com/w3c/csswg-drafts/issues/13818#issuecomment-4614144930), 2026-06),
  and `start/endOffset` become nullable
  ([#13844](https://github.com/w3c/csswg-drafts/issues/13844#issuecomment-4614158334), 2026-06).

## Related features

- Host module: [Scroll-driven Animations (scroll-animations-1)](../specs/scroll-animations-1.md).
- Deeply entwined with **Web Animations** (`web-animations-1/2`) and **CSS Animations 2**
  (`css-animations-2`): `animation-timeline`, `animation-range*`, and the `CSSNumberish`
  time model are defined jointly across those modules.
- Timeline-name scoping was aligned with **View Transitions** (`css-view-transitions-2`) and
  **Anchor Positioning** (`css-anchor-position-1`) name lookup (see [#13974](https://github.com/w3c/csswg-drafts/issues/13974), [#13364](https://github.com/w3c/csswg-drafts/issues/13364)).

## Sources

Primary (GitHub issue threads, mirrored):

- [#6674 Rethinking declarative syntax](../../raw/data/github/csswg-drafts/issues/06xxx/06674.md) — the 2021 declarative reboot.
- [#7047 named-timeline scope](../../raw/data/github/csswg-drafts/issues/07xxx/07047.md) / [#7759 timeline-scope](../../raw/data/github/csswg-drafts/issues/07xxx/07759.md) — scoping model.
- [#8101 rename to Scroll-driven](../../raw/data/github/csswg-drafts/issues/08xxx/08101.md).
- [#5321 prefers-reduced-motion](../../raw/data/github/csswg-drafts/issues/05xxx/05321.md).
- [#13974 loosely-matched names](../../raw/data/github/csswg-drafts/issues/13xxx/13974.md) — 2026 scoping alignment.

Status: `raw/data/w3c-api/specifications/scroll-animations-1.json` (`snapshot_at: 2026-07-04`);
Editor's Draft <https://drafts.csswg.org/scroll-animations-1/>.

> *This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*
