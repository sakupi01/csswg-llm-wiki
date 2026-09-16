---
date: 2021-12-09
group: openui
type: telecon
topics_count: 2
issues: [424, 429]
generated_by: llm
---

# Open UI CG telecon — 2021-12-09

Two topics, no bot-recorded resolutions (the IRC log records a "resolved" line on
[openui/open-ui#429](https://github.com/openui/open-ui/issues/429) that the bot did not surface
as a resolution bullet). Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2021-12-09](https://www.w3.org/2021/12/09-openui-minutes.html).

## `<selectmenu>` input/change events and the value property ([openui/open-ui#429](https://github.com/openui/open-ui/issues/429))

The minutes record [dandclark](../../people/dandclark.md) observing that the old `<select>`'s input/change event behavior is
consistent across Chrome and Firefox but inconsistent with other input types: text inputs fire
`input` per keystroke and `change` on commit, whereas `<select>` fires both once. He proposed
that `<selectmenu>` fire `input` (and update `value`) as the user arrow-keys through open
options, and fire `change` on close only if the selection differs. The minutes record [flackr](../../people/flackr.md) and
[gregwhitworth](../../people/gregwhitworth.md) supporting alignment with other inputs, una arguing old implementations shouldn't
prevent forward thinking, and [scottohara](../../people/scottaohara.md) raising the concern of divergence between two similar
controls that cannot be reconciled for web-compat reasons. The scribe recorded a resolution
adopting the diverging behavior; it does not appear in the resolutions index because the bot
comment did not record it as a resolution bullet. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/429#issuecomment-990165098))

## Other topics

- [openui/open-ui#424](https://github.com/openui/open-ui/issues/424) — meta discussion on incorporating "cowpaths" research into Open UI's work.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
