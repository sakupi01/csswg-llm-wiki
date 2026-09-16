---
date: 2026-02-26
group: openui
type: telecon
topics_count: 2
issues: [1375, 1379]
generated_by: llm
---

# Open UI CG telecon — 2026-02-26

Two topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/02/26-openui-minutes.html](https://www.w3.org/2026/02/26-openui-minutes.html) (dated-URL convention for CG minutes).

## Improvements to default style for base select? ([openui/open-ui#1375](https://github.com/openui/open-ui/issues/1375))

On the default `appearance: base` styles for the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [fantasai](../../people/fantasai.md)
as relaying feedback that the current base style looks "weird" — notably a rounded button paired
with a square picker — and arguing the defaults should be coherent even if plain. [masonf](../../people/mfreed7.md) is
recorded as fearing a slippery slope of aesthetic litigation, since the agreed design principles
say functional/recognizable/easy-to-style, not "look nice"; castastrophe countered that documented
design guiderails (e.g. one agreed radius) aid consistency. [keithamus](../../people/keithamus.md) questioned the
border-radius itself: it was meant to distinguish buttons (which act destructively) from inputs,
a rationale that does not apply to `<select>`, and dropping it removes a style rule. The group
resolved to drop the radius and to codify "non-weird" as a criterion.

> RESOLVED: Remove border-radius from <select>.

> RESOLVED: Open issue to add "non-weird" as a criteria.

([resolution](https://github.com/openui/open-ui/issues/1375#issuecomment-3968745890))

## Other topics

- [openui/open-ui#1379](https://github.com/openui/open-ui/pull/1379) — focusgroup pull request extending child role inference to buttons; the group agreed to drop the '-' in modifier names and review/land ([resolution](https://github.com/openui/open-ui/pull/1379#issuecomment-3968781100)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
