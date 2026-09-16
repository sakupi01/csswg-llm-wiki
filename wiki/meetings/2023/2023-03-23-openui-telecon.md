---
date: 2023-03-23
group: openui
type: telecon
topics_count: 1
issues: [687]
generated_by: llm
---

# Open UI CG telecon — 2023-03-23

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [w3.org/2023/03/23-openui-minutes.html](https://www.w3.org/2023/03/23-openui-minutes.html) (dated-URL convention for CG minutes).

## [selectmenu] Should the text inside `<option>`s be selectable? ([openui/open-ui#687](https://github.com/openui/open-ui/issues/687))

A default-styling question for `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [dandclark](../../people/dandclark.md)
as surveying existing behavior — native `<select>`, date/time picker popups and Bootstrap all
make option text non-selectable — and preferring to match that while keeping it
author-overridable. [JakeA](../../people/jakearchibald.md) raised the rich-content angle (options containing links or a delete
button); [masonf](../../people/mfreed7.md) clarified `user-select` does not block clicking a button, only text
highlighting, and noted interactive content inside options is an accessibility gray area anyway.
[scotto](../../people/scottaohara.md) made the strongest case for non-selectable defaults: a user with a motor tremor could
accidentally drag-select text when trying to pick an option. [gregwhitworth](../../people/gregwhitworth.md) stressed whatever
default is picked must be overridable with CSS — hence the "not `!important`" in the resolution.

> RESOLVED: options in a selectmenu are user-select:none, but not !important, via the UA stylesheet.

([resolution](https://github.com/openui/open-ui/issues/687#issuecomment-1481379612))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
