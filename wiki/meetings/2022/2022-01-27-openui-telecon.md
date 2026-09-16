---
date: 2022-01-27
group: openui
type: telecon
topics_count: 1
issues: [447]
generated_by: llm
---

# Open UI CG telecon — 2022-01-27

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2022-01-27](https://www.w3.org/2022/01/27-openui-minutes.html) (dated-URL convention).

## Should `<select multiple>` be part of `<selectmenu>`, or is it a separate control? ([openui/open-ui#447](https://github.com/openui/open-ui/issues/447))

The minutes record [dandclark](../../people/dandclark.md) asking whether multi-select belongs in `<selectmenu>` or in a
separate element, worried about a diverging API surface (`selectedOption` vs an array). The
minutes record [bkardell](../../people/bkardell.md), [masonf](../../people/mfreed7.md), [scotto](../../people/scottaohara.md), davidluhr and [melanierichards](../../people/melanierichards.md) leaning toward two
separate elements — with [melanierichards](../../people/melanierichards.md) urging the group to slow down and document why authors
bypass `<select multiple>` today — while [miriam](../../people/miriam.md) said authors would be fine either way and
[chrisdholt](../../people/chrisdholt.md) found it odd to bake a single-select listbox into `<select>` while a separate
`<listbox>` supported both. [gregwhitworth](../../people/gregwhitworth.md) is recorded steering toward a standalone `<listbox>`
element that could render inline or in the top layer. Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: resolution: we should work on specifying a <listbox> element that supports single and multi-select capability.

([resolution](https://github.com/openui/open-ui/issues/447#issuecomment-1023579279))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
