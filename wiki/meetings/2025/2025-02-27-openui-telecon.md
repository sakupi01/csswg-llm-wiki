---
date: 2025-02-27
group: openui
type: telecon
topics_count: 2
issues: [1133, 1164]
generated_by: llm
---

# Open UI CG telecon — 2025-02-27

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/02/27-openui-minutes.html](https://www.w3.org/2025/02/27-openui-minutes.html) (dated-URL convention for CG minutes).

## [Interest invokers] Keyboard inputs ([openui/open-ui#1133](https://github.com/openui/open-ui/issues/1133))

Continuation of the previous week. The minutes record [masonf](../../people/mfreed7.md) as presenting the revised proposal:
focusing the trigger shows the interest target, but a target shown via keyboard is inert until a
hotkey removes the inertness, requiring a new pseudo-class for the semi-activated state and a
screen-reader hint. [lwarlow](../../people/lukewarlow.md) argued modal dialogs cannot sensibly be interest targets and that the
`has-interest`/partial-interest pseudo-classes belong on the trigger; [keithamus](../../people/keithamus.md) worried about
diverging behaviour between mouse and keyboard when a user employs both at once, proposing that
both modalities get a partial-interest state. sarah1 pushed back on literal `inert` (fully
unfocusable) and suggested keeping content focusable but out of the tab order; nmn clarified
Facebook's implementation uses tabindex -1 rather than true inertness. No resolution was
recorded.

## [Range] Dual Handle Range Input Proposal ([openui/open-ui#1164](https://github.com/openui/open-ui/issues/1164))

[brecht_dr](../../people/brechtDR.md) proposed a dual-handle range input (price ranges, date ranges) via new attributes on
`<input type=range>`. The minutes record [masonf](../../people/mfreed7.md) as supportive of an explainer while flagging
dual vs. n-thumbs and pointing to Ana Tudor's earlier proposals and Apple's `appearance: base`
work; [sorvell](../../people/sorvell.md) warned that customising inputs is a larger can of worms than `<select>` since
inputs can't take children, and asked for a clearly defined scope; [lwarlow](../../people/lukewarlow.md) said the anatomy of
the range input must be standardised first (pointing at the css-forms-1 slider pseudo-elements)
and raised keyboard/focus questions for multiple thumbs.

> RESOLVED: let's start an explainer for all things range

([resolution](https://github.com/openui/open-ui/issues/1164#issuecomment-2688988014))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
