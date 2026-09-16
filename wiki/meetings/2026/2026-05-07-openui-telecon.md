---
date: 2026-05-07
group: openui
type: telecon
topics_count: 3
issues: [1433, 1441, 1442]
generated_by: llm
---

# Open UI CG telecon — 2026-05-07

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/05/07-openui-minutes.html](https://www.w3.org/2026/05/07-openui-minutes.html) (dated-URL convention for CG minutes).

## Filterable select and scrollbars ([openui/open-ui#1441](https://github.com/openui/open-ui/issues/1441))

On where scrolling should live in a filterable customizable `<select>` picker
(see [customizable select](../../features/customizable-select.md)). **Data gap**: the bot comment
for this date contains an essentially empty IRC log (only queue commands survived the automated
minuting experiment) — [mfreed7](../../people/mfreed7.md) pointed to a Google Doc holding the actual meeting notes
([comment](https://github.com/openui/open-ui/issues/1441#issuecomment-4400901757)). From the
mirror, the discussion involved [masonf](../../people/mfreed7.md), [flackr](../../people/flackr.md) and [dbaron](../../people/dbaron.md) (who queued on sticky positioning);
[jarhar](../../people/josepharhar.md) later implemented "option 2" in the Chromium prototype with a new part-like
`::select-listbox` pseudo-element
([comment](https://github.com/openui/open-ui/issues/1441#issuecomment-4791650181)).
No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1441#issuecomment-4400004856))

## Other topics

- [openui/open-ui#1433](https://github.com/openui/open-ui/issues/1433) — resolved to change the a11y mapping of `<menulist>` from menu to dialog when it contains non-menuitem interactive elements, deferring to the ARIA WG on details ([resolution](https://github.com/openui/open-ui/issues/1433#issuecomment-4399942493)).
- [openui/open-ui#1442](https://github.com/openui/open-ui/issues/1442) — resolved to move the `show-menu` and `hide-menu` commands to v2 ([resolution](https://github.com/openui/open-ui/issues/1442#issuecomment-4400108036)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
