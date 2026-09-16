---
title: Form Controls Styling
slug: form-controls
kind: family
members: [customizable-select]
generated_by: llm
---

# Form Controls Styling

## Overview

The cross-venue effort to make HTML's native form controls fully stylable —
ending the era where every design system re-implemented `<select>` from `<div>`s.
It is unusual among CSSWG topics in spanning **three standards venues**: the
[Open UI Community Group](https://open-ui.org/) incubates control anatomy and
behavior (its resolutions are recorded by css-meeting-bot, same as CSSWG's),
WHATWG HTML owns element semantics, parser changes, and control rendering, and
the CSSWG owns the styling opt-in and pseudo-element vocabulary in
[css-forms-1](../specs/css-forms-1.md).

The architecture that emerged from 2019–2024: authors opt a control into
interoperable, designable rendering with `appearance: base` (all in-page
controls, must ship simultaneously everywhere) or the per-control carve-out
`appearance: base-select`; pickers (the popped-up parts) opt in separately via
`::picker(keyword) { appearance: base }`
([#10440](https://github.com/w3c/csswg-drafts/issues/10440)). Once opted in, a
control stops being a replaced-element black box and exposes real structure:
child elements the author writes (`<button>`, `<selectedcontent>`, `<option>`
with arbitrary content) and part pseudo-elements the UA mints (`::picker()`,
`::picker-icon`, `::checkmark`, `::field-content`, `::slider-*`,
`::color-swatch`, `::clear-icon`, `::reveal-icon`).

## Members

| Feature | Status | One line |
|---|---|---|
| [customizable-select](../features/customizable-select.md) | shipping | The flagship: fully stylable `<select>` via `appearance: base-select`, `<selectedcontent>`, `::picker(select)` |

Not yet written (candidates as the family grows): `appearance-base` (the generic
all-controls opt-in and its UA stylesheet), `control-value()` (function reading a
control's value, [#7869](https://github.com/w3c/csswg-drafts/issues/7869) /
[#14140](https://github.com/w3c/csswg-drafts/issues/14140)), `slider-pseudos`
(`::slider-thumb/track/fill`, [#4410](https://github.com/w3c/csswg-drafts/issues/4410)),
`field-sizing` (css-ui-4, [#7542](https://github.com/w3c/csswg-drafts/issues/7542)),
`accent-color` (css-ui-4, [#5187](https://github.com/w3c/csswg-drafts/issues/5187)),
customizable `<input type=date>` and other picker controls as they arrive.

## Cross-cutting themes

- **The venue relay.** Ideas incubate in Open UI, semantics land in WHATWG,
  styling lands in CSSWG. The customizable `<select>` ran the full relay
  (2019 Open UI survey → 2023 [whatwg/html#9799](https://github.com/whatwg/html/issues/9799)
  → 2024–26 css-forms-1), and set the template later controls are expected to follow
  ([#10804](https://github.com/w3c/csswg-drafts/issues/10804) tracks the rollout plan).
- **CSS opt-in, not HTML attribute.** Twice debated, twice landing on CSS: the CSSWG
  resolved *for* an attribute in 2021 and reversed in 2024 ("use css to opt into
  styleable mode", [#5998](https://github.com/w3c/csswg-drafts/issues/5998));
  Open UI's 2024 attribute resolution ([openui/open-ui#985](https://github.com/openui/open-ui/issues/985))
  was overtaken by WHATWG editors' objections and never shipped.
- **Forwards compatibility as design driver.** `appearance: base` must ship on all
  controls at once; `::picker()` takes a control-type keyword; `base-select` exists
  precisely so `<select>` didn't have to wait
  ([#10440 resolutions](https://github.com/w3c/csswg-drafts/issues/10440#issuecomment-2332063450)).
- **Built-in, not bolted-on.** Recurring fight over whether UA internals should be
  visible web-platform primitives (popover, web components) or implementation
  details — `:popover-open` matching ([#10775](https://github.com/w3c/csswg-drafts/issues/10775)),
  the slots-vs-elements anatomy war ([openui/open-ui#702](https://github.com/openui/open-ui/issues/702)),
  the a11y-tree status of icon pseudos ([#14316](https://github.com/w3c/csswg-drafts/issues/14316)).
- **The UA stylesheet as spec surface.** Since FPWD, much of css-forms-1's work is
  literally writing a UA stylesheet in public, one resolution at a time
  (typography [#14250](https://github.com/w3c/csswg-drafts/issues/14250), overflow
  [#14255](https://github.com/w3c/csswg-drafts/issues/14255), centering
  [#14319](https://github.com/w3c/csswg-drafts/issues/14319), box-sizing
  [#14249](https://github.com/w3c/csswg-drafts/issues/14249)).

## Related families

None yet written. Anchor positioning ([feature page](../features/anchor-positioning.md))
is the key dependency for picker placement.

## Sources

- [_generated/by-spec/css-forms-1.md](../../_generated/by-spec/css-forms-1.md) — chronological digest
- [raw/data/github/open-ui/](../../raw/data/github/open-ui/) — full Open UI mirror
- [raw/data/github/html/](../../raw/data/github/html/) — selective whatwg/html mirror (select-related threads)
- [Open UI customizable select explainer](https://open-ui.org/components/customizableselect/)

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
Working Group. Verify against the linked primary sources.*
