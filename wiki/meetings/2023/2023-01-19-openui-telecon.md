---
date: 2023-01-19
group: openui
type: telecon
topics_count: 2
issues: [639, 646]
generated_by: llm
---

# Open UI CG telecon — 2023-01-19

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/01/19-openui-minutes.html](https://www.w3.org/2023/01/19-openui-minutes.html) (dated-URL convention for CG minutes).

## Should the button part of a SelectMenu toggle or show the listbox? ([openui/open-ui#639](https://github.com/openui/open-ui/issues/639))

An interaction question for `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [jhey](../../people/jhey.md) as
having surveyed component libraries, where the trigger button commonly toggles the listbox, and
[masonf](../../people/mfreed7.md) as separating a light-dismiss implementation bug from the design question: clicking the
open button must not count as a light-dismiss click that immediately reopens (a flicker).
[sarah_higley](../../people/smhigley.md) is recorded as arguing against "click does nothing" — zoomed-in users cannot be
assumed to have space to click outside the listbox — and [scotto](../../people/scottaohara.md) noted classic `<select>` behavior
already differs between browsers (Edge toggles). [flackr](../../people/flackr.md) observed the classic control's
click-outside behavior also varies by platform. The group settled on toggle semantics,
overridable by explicit popover attributes on the button.

> RESOLVED: clicking a selectmenu button opens the listbox popover. Clicking it again hides the listbox (potentially via a hide animation). No flickering or light dismiss behavior should happen in this scenario. This should be overridable via explicit attributes on the button.

([resolution](https://github.com/openui/open-ui/issues/639#issuecomment-1397496409))

## Other topics

- [openui/open-ui#646](https://github.com/openui/open-ui/issues/646) — agreed to leave the `popovershowtarget`/`popoverhidetarget` part of the API as-is ([resolution](https://github.com/openui/open-ui/issues/646#issuecomment-1397476289)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
