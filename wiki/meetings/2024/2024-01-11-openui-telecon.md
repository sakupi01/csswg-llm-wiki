---
date: 2024-01-11
group: openui
type: telecon
topics_count: 1
issues: [971]
generated_by: llm
---

# Open UI CG telecon — 2024-01-11

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2024/01/11-openui-minutes.html](https://www.w3.org/2024/01/11-openui-minutes.html)
(dated-URL convention for CG minutes).

## [combobox] Should we allow a button child to control the dropdown? ([openui/open-ui#971](https://github.com/openui/open-ui/issues/971))

lukew asked whether combobox should support the split-button pattern that selectlist had allowed.
The minutes record [masonf](../../people/mfreed7.md) as being of two minds (no real-world examples of a combobox split button)
and [gregwhitworth](../../people/gregwhitworth.md) as worried about focus management and about "any button triggers the popover"
breaking patterns like removable pills/tags inside a combobox; una's Amazon search-bar example was
judged to be visually-grouped separate components rather than one combobox. The group settled on an
explicit `type=popover` button, shared between the stylable `<select>` and combobox. After the
resolution, [masonf](../../people/mfreed7.md) recapped the history of the styling opt-in (CSS `appearance` vs an attribute),
which continued into [openui/open-ui#985](https://github.com/openui/open-ui/issues/985). This topic
is part of the [customizable select](../../features/customizable-select.md) story.

> RESOLVED: for stylable <select> use <button type=popover>. For combobox, any button with type=popover inside a combobox will trigger the popover. Other buttons will not.

([resolution](https://github.com/openui/open-ui/issues/971#issuecomment-1887875716))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
