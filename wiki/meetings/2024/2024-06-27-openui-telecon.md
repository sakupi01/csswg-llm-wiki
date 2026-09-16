---
date: 2024-06-27
group: openui
type: telecon
topics_count: 3
issues: [1063, 1064, 1066]
generated_by: llm
---

# Open UI CG telecon — 2024-06-27

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/06/27-openui-minutes.html](https://www.w3.org/2024/06/27-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] `<selectedoption for=id>` as an alternative to split buttons and `<button type=popover>` ([openui/open-ui#1063](https://github.com/openui/open-ui/issues/1063))

[jarhar](../../people/josepharhar.md) proposed letting the selected-option mirror of the [customizable
select](../../features/customizable-select.md) live outside the select via an ID reference,
replacing the split-button / `<button type=popover>` machinery. The minutes record [masonf](../../people/mfreed7.md) as loving
the idea ("I like not having two buttons that are magical") and relaying [annevk](../../people/annevk.md)'s suggestion to
invert the reference — an attribute on `<select>` pointing at the element rather than a `for`
attribute on each `<selectedoption>`; [scotto](../../people/scottaohara.md) as thanking [jarhar](../../people/josepharhar.md) and endorsing the inversion; and
[jarhar](../../people/josepharhar.md) as still preferring `for` but happy with either, later noting the inversion enables
incremental extension to other elements. The group capped it at two mirrors: the referenced one plus
the first one inside the select.

> RESOLVED: add an attribute called `selectedoptionelement=foo` to select, which can point to a single <selectedoption> element to update. The first <selectedoption> contained within the <select> would also be updated.

([resolution](https://github.com/openui/open-ui/issues/1063#issuecomment-2195407344))

## Other topics

- [openui/open-ui#1064](https://github.com/openui/open-ui/issues/1064) — how to define the action
  on "losing interest"
  ([resolution](https://github.com/openui/open-ui/issues/1064#issuecomment-2195447746)):

> RESOLVED: there should be a value of the interestaction attribute that means the correct behavior for popovers. They show when interest is shown, and hide when interest is lost.

- [openui/open-ui#1066](https://github.com/openui/open-ui/issues/1066) — foundation for the Global
  Design System component library, discussed without a recorded resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
