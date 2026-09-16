---
date: 2022-06-02
group: openui
type: telecon
topics_count: 2
issues: [335, 531]
generated_by: llm
---

# Open UI CG telecon — 2022-06-02

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-06-02](https://www.w3.org/2022/06/02-openui-minutes.html).

## [selectmenu] Reconsider requiring `<listbox>` as a prerequisite for `<selectmenu>` ([openui/open-ui#531](https://github.com/openui/open-ui/issues/531))

The minutes record [dandclark](../../people/dandclark.md) asking the group to reconsider the 2022-01-27 resolution on
[openui/open-ui#447](https://github.com/openui/open-ui/issues/447) that made a standalone
`<listbox>` element a prerequisite: a full `<listbox>` needs its own events, validation, form
involvement and attributes, doubling the surface and creating a "priority inversion" that
delays the `<selectmenu>` developers actually asked for. The minutes record [masonf](../../people/mfreed7.md) +1ing with a
tweak to make clear both efforts matter but the group wants to iterate on the simpler element
first; [scotto](../../people/scottaohara.md) and una agreed, with una insisting the resolution say the group *will* (not "may")
work on `<listbox>` later. [gregwhitworth](../../people/gregwhitworth.md) is recorded adding that interoperably stylable
controls still need UA-defined default styles ([openui/open-ui#536](https://github.com/openui/open-ui/issues/536)).
Part of the [customizable select](../../features/customizable-select.md) history.

> RESOLVED: <listbox> and multi-select are worthwhile and we'll eventually work on them, but the V1 of <selectmenu> will not use a <listbox> element and will not support multi-select.

([resolution](https://github.com/openui/open-ui/issues/531#issuecomment-1145170806))

## Other topics

- [openui/open-ui#335](https://github.com/openui/open-ui/issues/335) — supporting transitions and animations on popup open and dismiss.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
