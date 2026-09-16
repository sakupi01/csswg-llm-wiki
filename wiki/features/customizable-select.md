---
title: Customizable <select>
slug: customizable-select
kind: feature
status: shipping   # Chrome 135 (2025-04) + Edge 135 shipped; Safari 27 beta (WWDC26); Firefox positive, in development
specs: [css-forms-1]
spec_history:
  - {spec: css-forms-1, from: "2024-09"}   # module adopted 2024-09-19 (#10866); before that: Open UI explainer + whatwg/html
key_people: [gregwhitworth, josepharhar, mfreed7, annevk, fantasai, nt1m, una, lukewarlow, dandclark, domenic, scottaohara, jakearchibald]
key_issues: [5998, 10440, 10758, 10775, 10908, 10028, 12468, 13738, 14172, 14255]
first_seen: "2019-08"   # openui/open-ui#3 (domenic), citing gregwhitworth's 2019-07 survey
resolutions_count: 78   # labeled css-forms-1 in resolutions-index; +74 more select-labeled in openui/open-ui
families: [form-controls]
coverage: {github: full, www-style: n/a, member_era: n/a}   # entirely post-2019; venues: openui/open-ui + whatwg/html + csswg-drafts, all mirrored
generated_by: llm
---

# Customizable `<select>`

## Overview

Customizable `<select>` lets authors fully restyle the native select element —
button, dropdown ("picker"), options, icons — with plain CSS and a little extra
HTML, keeping the built-in keyboard, form, and accessibility behavior that
`<div>`-based replacements lose. The author-facing surface: opt in with
`appearance: base-select` on the `<select>` and on `::picker(select)`; put
arbitrary non-interactive content inside `<option>`; mirror the selected
option's content into the button with `<selectedcontent>`; style the parts via
`::picker(select)`, `::picker-icon`, `::checkmark`, `::field-content`, and
pseudo-classes like `:open` and `:checked`. The picker is a popover in the top
layer, anchor-positioned to the select.

It is the single largest form-control effort of the 2020s and the prototype of a
three-venue pipeline: anatomy and behavior were incubated in the
[Open UI CG](https://open-ui.org/components/customizableselect/) (2019–2024,
resolutions recorded by css-meeting-bot), element semantics and parser changes
landed in WHATWG HTML ([whatwg/html#9799](https://github.com/whatwg/html/issues/9799),
spec PR merged 2025-07-22), and the styling model lives in the CSSWG's
[css-forms-1](../specs/css-forms-1.md) (adopted 2024-09, FPWD 2025-03-25). The
project's shape changed twice, dramatically: a purpose-built `<selectmenu>` /
`<selectlist>` element with a web-components anatomy (slots, parts, `behavior`
attributes) was rebuilt on plain child elements after WHATWG-editor objections
([openui/open-ui#702](https://github.com/openui/open-ui/issues/702)), then
abandoned entirely in favor of retrofitting `<select>` itself, following Apple
feedback ([openui/open-ui#970](https://github.com/openui/open-ui/issues/970)).
Chrome shipped in 135 (2025-04); Safari 27 announced support at WWDC26.

## Current status

As of 2026-08-27:

- **Model settled.** CSS opt-in (not an HTML attribute); `appearance: base` for
  all in-page controls must ship everywhere simultaneously, `base-select` is the
  select-only carve-out that shipped first; pickers opt in per control type via
  `::picker(keyword)` ([#10440](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450)).
- **HTML merged.** Parser relaxation (arbitrary content in `<select>`),
  `<selectedcontent>` (clone-on-select, no mutation tracking), content model,
  and base UA rendering merged as [whatwg/html#10548](https://github.com/whatwg/html/pull/10548)
  (2025-07-22). Multi-select support and clone edge cases are the active WHATWG
  front ([whatwg/html#12430](https://github.com/whatwg/html/pull/12430)).
- **Implementations.** Chrome/Edge 135 shipped 2025-04
  ([Chrome 135 release notes](https://developer.chrome.com/release-notes/135));
  listbox-mode `base-select` in Chromium 145
  ([#12468](https://github.com/w3c/csswg-drafts/issues/12468#issuecomment-3804966240)).
  Safari 27 beta added support (announced WWDC26,
  [WebKit blog](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/)).
  Firefox: positive position, implementation in progress
  ([web-features entry](https://web-platform-dx.github.io/web-features-explorer/features/customizable-select/)).
  Generic `appearance: base` ships nowhere yet — by resolution it requires all
  controls at once.
- **2026 workstream.** css-forms-1 is building out the base UA stylesheet
  resolution by resolution — August 2026 alone settled picker default sizing
  ([#14172](https://github.com/w3c/csswg-drafts/issues/14172)), typography
  inheritance ([#14250](https://github.com/w3c/csswg-drafts/issues/14250)),
  button overflow ([#14255](https://github.com/w3c/csswg-drafts/issues/14255)),
  and the a11y-tree status of icon pseudos
  ([#14316](https://github.com/w3c/csswg-drafts/issues/14316)).
- **Still contested:** whether `::picker(select):popover-open` matches
  ([#10775](https://github.com/w3c/csswg-drafts/issues/10775) — Chromium ships
  matching, WebKit disputes); the `:hover`-stops-at-top-layer rule
  ([#14143](https://github.com/w3c/csswg-drafts/issues/14143)); searchable
  select ([openui/open-ui#847](https://github.com/openui/open-ui/issues/847));
  `::field-content` in `appearance: auto`
  ([#14323](https://github.com/w3c/csswg-drafts/issues/14323), Agenda+).

## Milestones

| Date | Milestone | Source |
|---|---|---|
| 2019-08 | Open UI opens the `<select>` question: incremental fixes vs a new element, citing [gregwhitworth](../people/gregwhitworth.md)'s survey showing select is the control developers most re-create | [openui/open-ui#3](https://github.com/openui/open-ui/issues/3) |
| 2021-02 | `appearance: base` proposed to CSSWG as the styling opt-in | [#5998](https://github.com/w3c/csswg-drafts/issues/5998) |
| 2021-04 | `<selectmenu>` prototype era begins in Open UI (tag name in use) | [openui/open-ui#240](https://github.com/openui/open-ui/issues/240#issuecomment-818125648) |
| 2022-06-02 | V1 scoped: no `<listbox>`, no multi-select | [resolution](https://github.com/openui/open-ui/issues/531#issuecomment-1145170806) |
| 2023-08-03 | Rename to `<selectlist>`; slots/parts anatomy abandoned for child elements | [openui/open-ui#773](https://github.com/openui/open-ui/issues/773#issuecomment-1664421419), [openui/open-ui#702](https://github.com/openui/open-ui/issues/702#issuecomment-1664464531) |
| 2023-09-26 | WHATWG venue opens: [whatwg/html#9799](https://github.com/whatwg/html/issues/9799) "Customizable `<select>` element" | [whatwg/html#9799](https://github.com/whatwg/html/issues/9799) |
| 2023-12-07 | **The pivot**: reuse `<select>` itself instead of `<selectlist>`, after Apple feedback | [resolution](https://github.com/openui/open-ui/issues/970#issuecomment-1846026582) |
| 2024-05-23 | CSSWG reverses its 2021 attribute decision: opt-in is CSS | [resolution](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-2127527423) |
| 2024-08-22 | `::picker(select)` resolved (replacing Chromium's `::select-fallback-datalist`) | [resolution](https://github.com/w3c/csswg-drafts/issues/10758#issuecomment-2305056084) |
| 2024-09-05 | Three-part opt-in architecture: `base` / `::picker(keyword)` / `base-select` carve-out | [resolution](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450) |
| 2024-09-19 | css-forms-1 adopted as a module; [fantasai](../people/fantasai.md) + [nt1m](../people/nt1m.md) editors | [resolution](https://github.com/w3c/csswg-drafts/issues/10866#issuecomment-2361365895) |
| 2024-10-31 | `<selectedoption>` renamed `<selectedcontent>`; mutation-tracking dropped a week earlier | [openui/open-ui#1112](https://github.com/openui/open-ui/issues/1112#issuecomment-2450527487), [openui/open-ui#825](https://github.com/openui/open-ui/issues/825#issuecomment-2436124668) |
| 2025-03-25 | css-forms-1 FPWD | [TR](https://www.w3.org/TR/2025/WD-css-forms-1-20250325/) |
| 2025-04-01 | **Ships in Chrome 135** (Edge 135 follows 04-04) | [Chrome 135 release notes](https://developer.chrome.com/release-notes/135) |
| 2025-07-22 | WHATWG HTML spec PR merged | [whatwg/html#10548](https://github.com/whatwg/html/pull/10548) |
| 2026-06 | Safari 27 beta ships customizable select (WWDC26) | [WebKit blog](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/) |

## Resolutions

A curated set of the narrative-carrying resolutions; text is verbatim from
`_generated/resolutions-index.jsonl` (78 carry the `css-forms-1` label; 74 more
are select-labeled in openui/open-ui; WHATWG has no resolution bot — its
decisions are cited by PR merge in the debates below).

| Date | Resolution (verbatim) | Issue | Permalink |
|---|---|---|---|
| 2022-01-27 | resolution: we should work on specifying a <listbox> element that supports single and multi-select capability. | [openui/open-ui#447](https://github.com/openui/open-ui/issues/447) | [link](https://github.com/openui/open-ui/issues/447#issuecomment-1023579279) |
| 2022-06-02 | <listbox> and multi-select are worthwhile and we'll eventually work on them, but the V1 of <selectmenu> will not use a <listbox> element and will not support multi-select. | [openui/open-ui#531](https://github.com/openui/open-ui/issues/531) | [link](https://github.com/openui/open-ui/issues/531#issuecomment-1145170806) |
| 2023-08-03 | rename `<selectmenu>` to `<selectlist>`. | [openui/open-ui#773](https://github.com/openui/open-ui/issues/773) | [link](https://github.com/openui/open-ui/issues/773#issuecomment-1664421419) |
| 2023-08-03 | move forward with the "elements" approach for `<selectlist>`, abandoning the "slots" approach. Open fresh issues for any new questions. | [openui/open-ui#702](https://github.com/openui/open-ui/issues/702) | [link](https://github.com/openui/open-ui/issues/702#issuecomment-1664464531) |
| 2023-12-07 | Reuse the select element instead of creating the selectlist element and reuse the datalist element for selectlist/select instead of using a new listbox element for it | [openui/open-ui#970](https://github.com/openui/open-ui/issues/970) | [link](https://github.com/openui/open-ui/issues/970#issuecomment-1846026582) |
| 2024-02-01 | trigger for dom structure and behavior should be independent from the trigger for interoperable styles | [openui/open-ui#985](https://github.com/openui/open-ui/issues/985) | [link](https://github.com/openui/open-ui/issues/985#issuecomment-1922141513) |
| 2024-02-01 | the opt-in for interoperable styling should be a new value for the `appearance` property, such as `base-select` or maybe `base`. | [openui/open-ui#985](https://github.com/openui/open-ui/issues/985) | [link](https://github.com/openui/open-ui/issues/985#issuecomment-1922141513) |
| 2024-05-23 | use css to opt into styleable mode | [#5998](https://github.com/w3c/csswg-drafts/issues/5998) | [link](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-2127527423) |
| 2024-06-27 | user agent styles can depend on appearance:base. Aim for eventual interoperability across all values of the property. | [#10028](https://github.com/w3c/csswg-drafts/issues/10028) | [link](https://github.com/w3c/csswg-drafts/issues/10028#issuecomment-2195094693) |
| 2024-08-15 | remove <datalist> from the content model as an element that the author can provide in a <select> because it doesn't provide any useful capabilities yet | [openui/open-ui#1082](https://github.com/openui/open-ui/issues/1082) | [link](https://github.com/openui/open-ui/issues/1082#issuecomment-2291908722) |
| 2024-08-22 | ::picker(select) is a part-like pseudo-element which applies to select elements which are in base appearance mode. It maps to the popover element inside the select's UA shadowroot. | [#10758](https://github.com/w3c/csswg-drafts/issues/10758) | [link](https://github.com/w3c/csswg-drafts/issues/10758#issuecomment-2305056084) |
| 2024-09-05 | `appearance:base` will apply to the in-page parts (only) of all form controls (including `<select>`), and, to avoid forwards-compat problems, must ship simultaneously on all form controls. | [#10440](https://github.com/w3c/csswg-drafts/issues/10440) | [link](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450) |
| 2024-09-05 | `::picker(keyword) { appearance: base }` will apply to form control pickers as an opt-in to styleable pickers of the named control type, with the control-type keyword allowing per-control-type incremental shipping of styleable pickers. To avoid forwards-compat problems, we will consider a keywordless variant only once all form controls can be opted in. | [#10440](https://github.com/w3c/csswg-drafts/issues/10440) | [link](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450) |
| 2024-09-05 | If appearance: base on all in-page controls is not ready in time for <select>, we may add appearance: base-select whose behavior is equivalent to appearance: base, but only applies to <select> and its picker (::picker(select)), individually. | [#10440](https://github.com/w3c/csswg-drafts/issues/10440) | [link](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450) |
| 2024-09-05 | don't create a special exception to not parse :popover-open on ::picker(select) | [#10775](https://github.com/w3c/csswg-drafts/issues/10775) | [link](https://github.com/w3c/csswg-drafts/issues/10775#issuecomment-2332100031) |
| 2024-09-24 | create new pseudo elements for checkmark and dropdown icon for base appearance select instead of using ::before and ::after in the UA stylesheet | [#10908](https://github.com/w3c/csswg-drafts/issues/10908) | [link](https://github.com/w3c/csswg-drafts/issues/10908#issuecomment-2371836734) |
| 2024-10-24 | dont observe mutations in option elements. only clone into selectedoption during parsing and when a new option becomes selected | [openui/open-ui#825](https://github.com/openui/open-ui/issues/825) | [link](https://github.com/openui/open-ui/issues/825#issuecomment-2436124668) |
| 2024-10-31 | rename the selectedoption element to selectedcontent | [openui/open-ui#1112](https://github.com/openui/open-ui/issues/1112) | [link](https://github.com/openui/open-ui/issues/1112#issuecomment-2450527487) |
| 2024-11-20 | Name the pseudo-element ::checkmark | [#10908](https://github.com/w3c/csswg-drafts/issues/10908) | [link](https://github.com/w3c/csswg-drafts/issues/10908#issuecomment-2489173316) |
| 2024-11-20 | go with ::picker-icon | [#10908](https://github.com/w3c/csswg-drafts/issues/10908) | [link](https://github.com/w3c/csswg-drafts/issues/10908#issuecomment-2489173316) |
| 2025-03-19 | Publish FPWD of CSS Forms | [#6900](https://github.com/w3c/csswg-drafts/issues/6900) | [link](https://github.com/w3c/csswg-drafts/issues/6900#issuecomment-2737246908) |
| 2025-07-16 | appearance: base-select can be used to opt listbox selects into base appearance. control of listbox and multiple rendering will be improved in html | [#12468](https://github.com/w3c/csswg-drafts/issues/12468) | [link](https://github.com/w3c/csswg-drafts/issues/12468#issuecomment-3079365750) |
| 2026-01-08 | Don't add buttons in default pickers. | [openui/open-ui#1217](https://github.com/openui/open-ui/issues/1217) | [link](https://github.com/openui/open-ui/issues/1217#issuecomment-3725472817) |
| 2026-04-01 | Change select picker positioning (position-area + try fallbacks) to use self-block-start / self-inline-start rather than block-start / inline-start | [#13738](https://github.com/w3c/csswg-drafts/issues/13738) | [link](https://github.com/w3c/csswg-drafts/issues/13738#issuecomment-4173520723) |
| 2026-07-01 | Use these values for ::picker(select) | [#14062](https://github.com/w3c/csswg-drafts/issues/14062) | [link](https://github.com/w3c/csswg-drafts/issues/14062#issuecomment-4857805306) |
| 2026-08-05 | For ::picker(), apply `box-sizing: border-box`, no minimum size, change `max-block-size` from `stretch` to `100dvb`, and apply `safe` overflow alignment (with the meaning that it keeps the popover in the viewport if possible). Debate whether to add `box-sizing: margin-box` / whether to change `100dvb` to a smaller size later. | [#14172](https://github.com/w3c/csswg-drafts/issues/14172) | [link](https://github.com/w3c/csswg-drafts/issues/14172#issuecomment-5190247826) |
| 2026-08-26 | ::Picker-icon and ::checkmark are not in the a11y tree | [#14316](https://github.com/w3c/csswg-drafts/issues/14316) | [link](https://github.com/w3c/csswg-drafts/issues/14316#issuecomment-5427379486) |

## Key debates

### New element vs fixing `<select>` — the founding question that reversed itself

- In [openui/open-ui#3](https://github.com/openui/open-ui/issues/3) (2019-08),
  [domenic](../people/domenic.md) laid out an incremental path (more stylable properties, small
  extensions) against a clean-slate `<superselect>`; [gregwhitworth](../people/gregwhitworth.md) argued the
  clean-slate advantages "encapsulate why I think we have to have `<superselect>`
  or similar as our north star"
  ([permalink](https://github.com/openui/open-ui/issues/3#issuecomment-518411145)).
  The new-element path won and produced `<selectmenu>` → `<selectlist>`.
- The reversal seed: the 2023-07-13 minutes record [annevk](../people/annevk.md) (Apple) asking "is it
  explained in more detail anywhere why we can't extend `<select>` further?"
  ([permalink](https://github.com/openui/open-ui/issues/773#issuecomment-1634706660)).
  After [josepharhar](../people/josepharhar.md) opened [whatwg/html#9799](https://github.com/whatwg/html/issues/9799)
  and negotiated with [annevk](../people/annevk.md), Open UI resolved on 2023-12-07 to reuse `<select>`
  (and `<datalist>` — later removed again in
  [openui/open-ui#1082](https://github.com/openui/open-ui/issues/1082)). The
  minutes record [masonf](../people/mfreed7.md) as saying he "was against it initially … but it turns
  out there is a lot of parser behaviour that helps us a lot" — old parsers
  discard unknown `<select>` children, giving graceful degradation
  ([permalink](https://github.com/openui/open-ui/issues/970#issuecomment-1846026582)).
  The project thus ended at the incremental pole it had rejected in 2019.

### Web-components anatomy vs child elements ([openui/open-ui#702](https://github.com/openui/open-ui/issues/702))

- The original design filled parts with `slot=button` / `slot=listbox`, attached
  behavior via a `behavior` attribute, and styled via `::part()`. [domenic](../people/domenic.md)
  (WHATWG editor) objected in 2023-03 that `slot=""`/`::part()` belong to
  author-created shadow DOM and that a semi-generic `behavior=""` attribute "is
  not idiomatic to HTML" ([openui/open-ui#702](https://github.com/openui/open-ui/issues/702)).
  [mfreed7](../people/mfreed7.md) defended slotting as genuine composition — a semantically appropriate
  `<button>` can fill a part
  ([permalink](https://github.com/openui/open-ui/issues/702#issuecomment-1650786841)).
- Notable dissent when elements won: [dbaron](../people/dbaron.md) wrote he was "pretty sad about the
  conclusion that we're not going to use Web Components technologies to describe
  pieces of the web that are implemented in browsers"
  ([permalink](https://github.com/openui/open-ui/issues/702#issuecomment-1654235474));
  [gregwhitworth](../people/gregwhitworth.md) vented that the feedback arrived three years into the design
  ([permalink](https://github.com/openui/open-ui/issues/702#issuecomment-1656537875)).
  [josepharhar](../people/josepharhar.md) drafted the new-elements anatomy and the group resolved for it on
  2023-08-03 ([permalink](https://github.com/openui/open-ui/issues/702#issuecomment-1664464531)).

### Opt-in mechanism: HTML attribute vs CSS (2021 → 2024, reversed)

- The CSSWG's 2021 answer was an attribute: the minutes record [emilio](../people/emilio.md) arguing
  changing shadow DOM from a CSS computed value is conceptually wrong, and hober
  not wanting CSS to generate DOM
  ([#5998 resolution](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-816302367)).
  Open UI's 2024-02 resolution likewise wanted "a new attribute (name TBD)"
  ([openui/open-ui#985](https://github.com/openui/open-ui/issues/985#issuecomment-1922141513))
  — the minutes record [jarhar](../people/josepharhar.md) predicting "my spidey senses there will be
  pushback" from WHATWG.
- [annevk](../people/annevk.md) rejected the attribute as mixing styling into semantics
  ([permalink](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-1880923043)),
  and [josepharhar](../people/josepharhar.md)'s Chromium implementation showed the switch needs only
  layout-tree changes, not DOM changes
  ([permalink](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-2086113395)),
  removing the 2021 objection's basis. Resolved 2024-05-23: "use css to opt into
  styleable mode" ([permalink](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-2127527423)).
  The attribute never shipped; `appearance: base-select` became the sole opt-in.
  A side effect settled in [#10028](https://github.com/w3c/csswg-drafts/issues/10028):
  UA styles may depend on computed `appearance` (via a `light-dark()`-style
  internal function, avoiding two-pass style computation)
  ([permalink](https://github.com/w3c/csswg-drafts/issues/10028#issuecomment-2047865990)).

### Generic `base` vs per-control `base-select` ([#10440](https://github.com/w3c/csswg-drafts/issues/10440))

- Forwards compatibility vs developer ergonomics. [mfreed7](../people/mfreed7.md) (Google) argued from
  the 2020 Chromium form-controls-refresh compat scars that `* { appearance: base }`
  would break future controls
  ([permalink](https://github.com/w3c/csswg-drafts/issues/5998#issuecomment-2101509763));
  fantasai/annevk (Apple) wanted a single `base` for in-page parts plus
  per-control picker opt-ins, arguing pickers are "a multi year project"
  ([permalink](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2276231894));
  una pushed back on the double opt-in's developer burden
  ([permalink](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2237160607)).
- The 2024-09-05 three-part resolution is a genuine synthesis: `base` = all
  in-page controls, simultaneous shipping; `::picker(keyword)` = per-control
  picker opt-in; `base-select` = an explicitly *temporary* carve-out so select
  didn't wait ([permalink](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450)).
  [mfreed7](../people/mfreed7.md) conceded the separate picker opt-in "even in the case of `<select>`"
  ([permalink](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2307593411)).
  Rejected: `base-listbox` (new values frozen,
  [#12468](https://github.com/w3c/csswg-drafts/issues/12468#issuecomment-3103250104)).

### `<selectedcontent>` cloning ([whatwg/html#10520](https://github.com/whatwg/html/issues/10520), [openui/open-ui#825](https://github.com/openui/open-ui/issues/825))

- The button's mirror of the selected option went through three designs. First
  live mutation-tracking (resolved for, 2024-04-25,
  [permalink](https://github.com/openui/open-ui/issues/825#issuecomment-2077912960));
  [smaug](../people/smaug.md) (Mozilla) objected that microtask timing gives observably stale values
  ([permalink](https://github.com/whatwg/html/issues/10520#issuecomment-2325039676)),
  esprehn argued full-subtree cloning is unpolyfillable and breaks canvas/custom
  elements ([permalink](https://github.com/whatwg/html/issues/10520#issuecomment-2417825526)),
  and [jakearchibald](../people/jakearchibald.md)'s comparison matrix proposed clone-once-on-select
  ([permalink](https://github.com/whatwg/html/issues/10520#issuecomment-2418959922)).
- Open UI reversed on 2024-10-24 — clone only at parse time and on selection
  change ([permalink](https://github.com/openui/open-ui/issues/825#issuecomment-2436124668))
  — and that design merged in [whatwg/html#10548](https://github.com/whatwg/html/pull/10548).
  [LeaVerou](../people/lea.md)'s 2025 counter-proposal to replace cloning with `<use>`-style
  mirroring was closed by [annevk](../people/annevk.md) as "too complex"
  ([whatwg/html#11463](https://github.com/whatwg/html/issues/11463#issuecomment-4625939676)).
  The element was also renamed twice for clarity, ending at `<selectedcontent>`
  ([openui/open-ui#1112](https://github.com/openui/open-ui/issues/1112)).

### Parser relaxation and accessibility ([whatwg/html#10310](https://github.com/whatwg/html/issues/10310), [#10317](https://github.com/w3c/csswg-drafts/issues/10317))

- How much arbitrary content should `<select>` accept? [hsivonen](../people/hsivonen.md) (Mozilla)
  initially favored the conservative option, fearing parser-change fallout
  ([permalink](https://github.com/whatwg/html/issues/10310#issuecomment-2138986436));
  [LeaVerou](../people/lea.md), wearing the TAG hat, argued an opt-in-gated parser is
  author-hostile ([permalink](https://github.com/whatwg/html/issues/10310#issuecomment-2100966788)).
  The permissive option won (the "in select" insertion mode was removed for all
  `<select>`s, independent of appearance), surviving a 2025-02 fragment-parsing
  compat regression ([permalink](https://github.com/whatwg/html/issues/10310#issuecomment-2660181590)).
- aardrian pressed the a11y consequences of "anything goes"; [scottaohara](../people/scottaohara.md)'s
  [whatwg/html#10317](https://github.com/whatwg/html/issues/10317) fixed the
  content model (non-interactive palpable content inside `<option>`), and a
  2025-02 WHATNOT meeting settled that `<img alt>` inside options feeds
  rendering and accessible names but not `option.value`/`.label`/`.text` —
  [domenic](../people/domenic.md), [scottaohara](../people/scottaohara.md), and [aleventhal](../people/aleventhal.md) argued mixing a11y strings into machine
  values would corrupt both
  ([permalink](https://github.com/whatwg/html/issues/10317#issuecomment-2657306389)).

### Is the picker *a popover* or does it merely use one? ([#10775](https://github.com/w3c/csswg-drafts/issues/10775), [#14143](https://github.com/w3c/csswg-drafts/issues/14143))

- `::picker(select)` maps to a real popover in the UA shadow root, in the top
  layer, with light dismiss (which commits the selection —
  [openui/open-ui#1217](https://github.com/openui/open-ui/issues/1217) also
  removed default OK/Cancel buttons after a 2026 reversal). The philosophical
  fight is whether that implementation is *observable*: should
  `::picker(select):popover-open` match? Pro ([tabatkins](../people/tabatkins.md): "if we use popover,
  we're stuck with popover… we should expose that it's a popover",
  [permalink](https://github.com/w3c/csswg-drafts/issues/10775#issuecomment-4101363570);
  [dbaron](../people/dbaron.md) framed it as the decades-old plan of exposing built-ins as platform
  primitives, [permalink](https://github.com/w3c/csswg-drafts/issues/10775#issuecomment-2327704994)).
  Contra ([annevk](../people/annevk.md): popover is an implementation detail and `select:open` covers
  the use case, [permalink](https://github.com/w3c/csswg-drafts/issues/10775#issuecomment-2328068716);
  the 2024-08-22 minutes record [fantasai](../people/fantasai.md): "we want form controls to act like
  they're built into the language, not built out of author facilities in the
  language"). Only *parsing* was resolved (2024-09-05); matching was
  re-litigated at the [2026-03-19 telecon](https://github.com/w3c/csswg-drafts/issues/10775#issuecomment-4091259351)
  with Chromium having shipped matching. **Open.**
- The related `:hover`-propagation rule — hover stops at the first top-layer
  element, so hovering the picker doesn't keep the select `:hover`
  ([#11185](https://github.com/w3c/csswg-drafts/issues/11185#issuecomment-2769962819),
  source: manual minutes) — was reopened by [emilio](../people/emilio.md) in
  [#14143](https://github.com/w3c/csswg-drafts/issues/14143) as inconsistent
  with pointer events; [jakearchibald](../people/jakearchibald.md) traced the awkwardness to "we're trying to
  pretend the select & picker are siblings, even though they're not"
  ([permalink](https://github.com/w3c/csswg-drafts/issues/14143#issuecomment-4926932535)).
  **Open**, awaiting a concrete proposal.

### Picker placement and sizing — the anchor-positioning integration

- The picker is anchor-positioned to the select, and its UA defaults evolved in
  three steps during 2026: writing-mode correctness (`self-*` keywords, fixing
  RTL selects in LTR pages, [#13738](https://github.com/w3c/csswg-drafts/issues/13738)),
  replacing explicit fallback areas with `flip-*` tactics so author margins
  mirror automatically ([#13541](https://github.com/w3c/csswg-drafts/issues/13541)),
  then `flip-self-*` variants resolved specifically for `::picker(select)`
  ([#14062](https://github.com/w3c/csswg-drafts/issues/14062)). The mechanics
  live in [anchor-positioning](anchor-positioning.md).
- Default sizing was settled at the 2026-08-05 F2F after [jakearchibald](../people/jakearchibald.md) showed
  the picker could collapse to ~0 or grow viewport-tall: [fantasai](../people/fantasai.md)'s no-magic-
  numbers model won (border-box, no min size, `max-block-size: 100dvb`, `safe`
  overflow alignment) over `calc-size()` formulas, with [TabAtkins](../people/tabatkins.md) objecting
  that viewport-filling pickers match no OS convention
  ([#14172](https://github.com/w3c/csswg-drafts/issues/14172#issuecomment-5190247826)).

### Naming sagas

- The element: `<selectmenu>` → `<selectbox>` proposed (jelbourn: "menu" wrongly
  invokes the ARIA menu pattern) → una's `<selectlist>` won a straw poll →
  obsolete once `<select>` itself was reused
  ([openui/open-ui#773](https://github.com/openui/open-ui/issues/773#issuecomment-1644889075)).
- The mirror element: `behavior=selected-value` → `<selectedvalue>` →
  `<selectedoption>` → `<selectedcontent>`, the last because [jakearchibald](../people/jakearchibald.md)
  noted "the `<selectedoption>`" and "the selected `<option>`" are verbally
  indistinguishable ([openui/open-ui#1112](https://github.com/openui/open-ui/issues/1112)).
- The icon pseudos: ~18 candidates; straw polls picked `::checkmark` and
  `::picker-icon` (decoration inside the button that opens the `::picker()` —
  the prefix is deliberate)
  ([#10908](https://github.com/w3c/csswg-drafts/issues/10908#issuecomment-2489173316)).
  The 2026 follow-ups: writing-mode-aware rotatable glyph keywords (names still
  open, [#14317](https://github.com/w3c/csswg-drafts/issues/14317)), `font: 100%
  system-ui` so icons don't inherit "random symbol glyphs from random fonts"
  ([#14250](https://github.com/w3c/csswg-drafts/issues/14250#issuecomment-5358336573)),
  and exclusion from the a11y tree — [lukewarlow](../people/lukewarlow.md)'s footgun argument (authors
  overriding `content` would forget empty alt) beat [fantasai](../people/fantasai.md)'s empty-alt-text
  proposal ([#14316](https://github.com/w3c/csswg-drafts/issues/14316#issuecomment-5427379486)).

## Related features

- [anchor-positioning](anchor-positioning.md) — picker placement (`position-area`,
  `flip-self-*` fallbacks, top-layer interaction)
- Family: [form-controls](../families/form-controls.md) — the venue pipeline,
  `appearance: base`, and the sibling primitives (`control-value()`, slider
  pseudos, `::color-swatch`)

## Sources

- Mirrors: [raw/data/github/open-ui/](../../raw/data/github/open-ui/) (full),
  [raw/data/github/html/](../../raw/data/github/html/) (selective, select-related),
  `raw/data/github/csswg-drafts/` issues 5998, 10028, 10440, 10758, 10775, 10908,
  12468, 13541, 13738, 14062, 14143, 14172, 14250, 14255, 14316, 14317
- Indexes: [_generated/by-spec/css-forms-1.md](../../_generated/by-spec/css-forms-1.md)
- Spec: [css-forms-1 ED](https://drafts.csswg.org/css-forms-1/) /
  [FPWD](https://www.w3.org/TR/2025/WD-css-forms-1-20250325/)
- Explainer: [Open UI customizable select](https://open-ui.org/components/customizableselect/)
- WHATWG: [whatwg/html#9799](https://github.com/whatwg/html/issues/9799) (tracking),
  [whatwg/html#10548](https://github.com/whatwg/html/pull/10548) (merged spec PR)

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
Working Group. Verify against the linked primary sources.*
