---
date: 2022-08-25
group: openui
type: telecon
topics_count: 4
issues: [297, 520, 533, 571]
generated_by: llm
---

# Open UI CG telecon — 2022-08-25

Four topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-08-25](https://www.w3.org/2022/08/25-openui-minutes.html).

## Should we standardize the anatomy of `<input type=range>`? ([openui/open-ui#297](https://github.com/openui/open-ui/issues/297))

The minutes record [bkardell](../../people/bkardell.md) reporting that the CSSWG had deferred anything beyond minor
decisions on range anatomy to Open UI, and that Ana Tudor — author of much of the community's
range-styling research — had received funding to work on it. He proposed starting with an
explainer, with Ana and himself as editors. The minutes record [emilio](../../people/emilio.md) agreeing but noting the
compat impact of changing the existing control needs assessing, [scotto](../../people/scottaohara.md) asking whether the
current element's anatomy can even be made consistent cross-browser without breaking authors'
workarounds, and [masonf](../../people/mfreed7.md) noting the confusing overlap between `progress`, `meter` and
`input type=range`. No resolution was recorded; a new issue was to be opened once the explainer
existed.

([discussion](https://github.com/openui/open-ui/issues/297#issuecomment-1227713627))

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

The minutes record [dandclark](../../people/dandclark.md) noting the issue was waiting on more use cases requested at the
previous discussion, so the group deferred it from the agenda until those were collected —
[dandclark](../../people/dandclark.md) calling it "a fairly complex issue". No resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/571#issuecomment-1227623212))

## Other topics

- [openui/open-ui#533](https://github.com/openui/open-ui/issues/533) — resolved to change the Invalid Value Default for `popup` to `manual` ([resolution](https://github.com/openui/open-ui/issues/533#issuecomment-1227619710)).
- [openui/open-ui#520](https://github.com/openui/open-ui/issues/520) — interaction between popup and other top layer elements.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
