---
date: 2022-07-21
group: openui
type: telecon
topics_count: 3
issues: [526, 532, 540]
generated_by: llm
---

# Open UI CG telecon — 2022-07-21

Three topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-07-21](https://www.w3.org/2022/07/21-openui-minutes.html).

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

Follow-up on the interactive content *outside* options (a button alongside the options rather
than inside them). The minutes record [dandclark](../../people/dandclark.md) arguing for the same soft console-warning
approach as inside options: parser changes meet implementer reluctance, and dynamically yanking
content back out of the DOM has no platform precedent — plus a warning doesn't box the group in
if ARIA later supports these patterns. The minutes record [bkardell](../../people/bkardell.md) describing the "garbage slot"
approach used in the tabs work, [flackr](../../people/flackr.md) finding disappearing content confusing and wanting the
door left open to making such content accessible, [sarah_higley](../../people/smhigley.md) countering that content the group
decides can never be accessible should be actively removed or broken (e.g. a text input between
options trapping focus), and [emilio](../../people/emilio.md) saying removal at any level goes against why `<selectmenu>`
exists. Time ran out; no resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/540#issuecomment-1191904350))

## Other topics

- [openui/open-ui#532](https://github.com/openui/open-ui/issues/532) — resolved to shortlist five candidate names for `popup=hint`: hint, title, light, info, advisory ([resolution](https://github.com/openui/open-ui/issues/532#issuecomment-1191797052)).
- [openui/open-ui#526](https://github.com/openui/open-ui/issues/526) — "interest"-based triggering for popovers, discussed without resolution this day.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
