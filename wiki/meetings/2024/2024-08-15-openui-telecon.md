---
date: 2024-08-15
group: openui
type: telecon
topics_count: 1
issues: [1082]
generated_by: llm
---

# Open UI CG telecon — 2024-08-15

One topic; one resolution, logged twice by two scribes with slightly different punctuation (both
quoted below for fidelity). Minutes recorded by the CSS meeting bot on the linked issue. Official
minutes: [2024/08/15-openui-minutes.html](https://www.w3.org/2024/08/15-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] Removing the capability for the author to provide a datalist element ([openui/open-ui#1082](https://github.com/openui/open-ui/issues/1082))

[jarhar](../../people/josepharhar.md) proposed dropping author-provided `<datalist>` from the [customizable
select](../../features/customizable-select.md) content model: with the parser changes, the
UA-shadow fallback popover plus a targetable pseudo-element covers the use cases, and allowing both
author and fallback datalists adds machinery like a popover-without-popover-attribute. The minutes
record una as supportive after probing how the parser distinguishes wrapper divs, [masonf](../../people/mfreed7.md) as +1
while suggesting a UA rule could keep existing datalist demos working, and scott as not opposed but
worried that removing it closes the door on future comboboxes that open explicit dialogs or grids —
[jarhar](../../people/josepharhar.md) answering that a later datalist/dialog slot-in upgrade remains possible.

> RESOLVED: remove <datalist> from the content model as an element that the author can provide in a <select>, because it doesn't provide any useful capabilities yet

> RESOLVED: remove <datalist> from the content model as an element that the author can provide in a <select> because it doesn't provide any useful capabilities yet

([resolution](https://github.com/openui/open-ui/issues/1082#issuecomment-2291908722))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
