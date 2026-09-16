---
date: 2024-01-25
group: openui
type: telecon
topics_count: 2
issues: [939, 977]
generated_by: llm
---

# Open UI CG telecon — 2024-01-25

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/01/25-openui-minutes.html](https://www.w3.org/2024/01/25-openui-minutes.html)
(dated-URL convention for CG minutes).

## [combobox] Is type="selectlist" correct for the input? ([openui/open-ui#939](https://github.com/openui/open-ui/issues/939))

lukew noted the combobox explainer still used `type=selectlist` on the input, a name that no longer
exists. The minutes record [masonf](../../people/mfreed7.md) as proposing the `<form>` model: the first button implicitly
triggers the picker, and `type=popover` disambiguates when there are several; [scotto](../../people/scottaohara.md) asked whether
`<input list>`/`<datalist>` already covers the case, and lukew worried `type=popover` could confuse
authors given `popovertarget` exists. The group scoped the resolution to `<select>` (a known
quantity) and deferred combobox specifics — see the
[customizable select](../../features/customizable-select.md) feature page.

> RESOLVED: the first button inside <select> triggers the popover. If there is more than one, use <button type=popover> to be the one that triggers the popover.

([resolution](https://github.com/openui/open-ui/issues/939#issuecomment-1910837275))

## stylable select: What should we do about the `multiple` and `size` attributes? ([openui/open-ui#977](https://github.com/openui/open-ui/issues/977))

[jarhar](../../people/josepharhar.md) wanted a plan that lets single stylable [customizable
select](../../features/customizable-select.md) ship first without blocking a future multi-select.
The minutes record [masonf](../../people/mfreed7.md) and [scotto](../../people/scottaohara.md) as liking that `multiple`/`size` falling back to the legacy
rendering doubles as an obvious feature-detect ("give them the old awful until multiple stylable
select is implemented"); lukew and [gregwhitworth](../../people/gregwhitworth.md) agreed `size` need not be carried forward, with a
possible new "inline" attribute later. [flackr](../../people/flackr.md) asked what feature detection would look like; [masonf](../../people/mfreed7.md)
pointed to an example in the issue.

> RESOLVED: multiple and size will not be supported initially  on singled select with datalist. If these attributes are detected the parser uses the original select logic

([resolution](https://github.com/openui/open-ui/issues/977#issuecomment-1910874971))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
