---
date: 2022-06-09
group: openui
type: telecon
topics_count: 2
issues: [420, 540]
generated_by: llm
---

# Open UI CG telecon — 2022-06-09

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-06-09](https://www.w3.org/2022/06/09-openui-minutes.html).

## [Popup] Triggering element support: buttons, text inputs, etc. ([openui/open-ui#420](https://github.com/openui/open-ui/issues/420))

The minutes record [masonf](../../people/mfreed7.md) laying out which elements the invoking attributes (`togglepopup`,
`showpopup`, `hidepopup`) should be usable on: any non-form-submitting button, plus text inputs
for combobox-like cases, where his opinion was the down arrow should open the popup. The minutes
record [bkardell](../../people/bkardell.md) asking how the input case works without a keyboard (touch devices), and [flackr](../../people/flackr.md)
insisting there must be some implicit or element-related trigger; [masonf](../../people/mfreed7.md) compared it to how
`<input>` handles `datalist` and agreed the keyboard/mouse/touch behaviors need more definition.

> RESOLVED: for invoking attributes that point to `popup=auto` popups, we should support the list of elements in this comment: https://github.com/openui/open-ui/issues/420#issuecomment-1135019013

([resolution](https://github.com/openui/open-ui/issues/420#issuecomment-1151449847))

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

First round of a long-running debate. The minutes record [dandclark](../../people/dandclark.md) proposing that interactive
content (form controls, links, `<summary>`/`<details>`, media, `tabindex`-focusable elements)
inside a `<selectmenu>` listbox keep working but trigger a UA developer warning, because the
accessibility model expects only options and groupings there. The minutes record [sarah_higley](../../people/smhigley.md)
arguing that if content can never be made accessible a warning is not sufficient — removal may
be better — while [flackr](../../people/flackr.md) worried about limiting real use cases (e.g. nested pickers) and [masonf](../../people/mfreed7.md)
strongly favored not breaking the control lest developers fall back to divs. A narrowed proposal
covering interactive content *inside options* drew +1s, but [bkardell](../../people/bkardell.md) asked for concrete examples
before resolving, so no resolution was recorded this day. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/540#issuecomment-1151590202))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
