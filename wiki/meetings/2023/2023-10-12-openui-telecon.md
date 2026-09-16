---
date: 2023-10-12
group: openui
type: telecon
topics_count: 3
issues: [845, 863, 869]
generated_by: llm
---

# Open UI CG telecon — 2023-10-12

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/10/12-openui-minutes.html](https://www.w3.org/2023/10/12-openui-minutes.html) (dated-URL convention for CG minutes).

## selectlist: Should the "checked" option have a checkmark next to it? ([openui/open-ui#863](https://github.com/openui/open-ui/issues/863))

Default UA styling for `<selectlist>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
asking whether the checked option should get a default checkmark. luke doubted its value since
most developers would strip it; una and Cat_Johnson argued the opposite — strong, easily
removable defaults (macOS `<select>` shows a checkmark today) — and [nicole](../../people/stubbornella.md) grounded it in
accessibility: default styles protect users developers don't test for, and WCAG 1.4.1 forbids
conveying state by colour alone ([keithamus](../../people/keithamus.md) cited chapter and verse; scotto_ noted an icon is
easier to recognise than a colour change). [keithamus](../../people/keithamus.md) suggested `accent-color` plus a `::marker`
pseudo, which drew broad support; luke and [masonf](../../people/mfreed7.md) converged on a `::marker`-based checkmark that
`display: none` removes, with developer guidance for full replacement. una also voiced the
recurring wish for a way to strip UA styles wholesale. [jarhar](../../people/josepharhar.md) was asked to write up a concrete
proposal on the issue for use-case feedback. No resolution was recorded that day.

## Other topics

- [openui/open-ui#845](https://github.com/openui/open-ui/issues/845) — resolved to improve the design-system anatomy JSON schema ([resolution](https://github.com/openui/open-ui/issues/845#issuecomment-1760126879)).
- [openui/open-ui#869](https://github.com/openui/open-ui/issues/869) — resolved to propose eventual deprecation of `popovertarget` in favour of invokers, with both coexisting for a while ([resolution](https://github.com/openui/open-ui/issues/869#issuecomment-1760141869)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
