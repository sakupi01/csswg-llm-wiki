---
date: 2024-04-18
group: openui
type: telecon
topics_count: 2
issues: [939, 1033]
generated_by: llm
---

# Open UI CG telecon — 2024-04-18

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/04/18-openui-minutes.html](https://www.w3.org/2024/04/18-openui-minutes.html)
(dated-URL convention for CG minutes).

## [combobox] Is type="selectlist" correct for the input? ([openui/open-ui#939](https://github.com/openui/open-ui/issues/939))

Returning to the combobox anatomy, [gregwhitworth](../../people/gregwhitworth.md) reported that many real comboboxes (Facebook,
Gmail search) have no visible trigger button — the text input itself opens the popup. The minutes
record [keithamus](../../people/keithamus.md) as pushing back that those examples are autocompletes closer to `<input>` +
`<datalist>` than a bounded select, and [scotto](../../people/scottaohara.md) as asking why the invoker must be on the input at
all when a default button (hideable by authors) would be better for accessibility. The group
resolved on a default button plus a programmatic escape hatch, extending `showPicker()` to
`<datalist>`.

> RESOLVED: A combobox will have a button so that the datalist is shown. Extend datalist to have programmatic support for showPicker() to allow for hiding of the button when desired.

([resolution](https://github.com/openui/open-ui/issues/939#issuecomment-2064923649))

## Other topics

- [openui/open-ui#1033](https://github.com/openui/open-ui/issues/1033) — should events trigger when
  invoking ([resolution](https://github.com/openui/open-ui/issues/1033#issuecomment-2064811267)):

> RESOLVED: dispatch change events when an invoker changes an input value

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
