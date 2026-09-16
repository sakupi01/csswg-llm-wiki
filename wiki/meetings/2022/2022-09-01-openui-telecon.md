---
date: 2022-09-01
group: openui
type: telecon
topics_count: 1
issues: [599]
generated_by: llm
---

# Open UI CG telecon — 2022-09-01

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2022-09-01](https://www.w3.org/2022/09/01-openui-minutes.html) (dated-URL convention).

## Define behavior of tab key in `<selectmenu>` listbox ([openui/open-ui#599](https://github.com/openui/open-ui/issues/599))

The minutes record [dandclark](../../people/dandclark.md) proposing that `<selectmenu>` follow the native `<select>` model:
Tab closes the listbox and returns focus to the button, rather than moving through focusable
content inside the popup. The minutes record [sarah_h](../../people/smhigley.md) citing her user studies
([Select your poison](https://www.24a11y.com/2019/select-your-poison/)) showing Tab is the most
common way keyboard users *commit* a selection in single selects, and [scotto](../../people/scottaohara.md) warning against
grafting tree/menu-style behaviors onto a listbox — if the group wants a menu it should build a
menu element. The minutes record [masonf](../../people/mfreed7.md), initially hesitant about boxing in future
secondary-action content, being convinced, and a longer recorded exchange in which [gregwhitworth](../../people/gregwhitworth.md)
defended shipping `<selectmenu>` as the 90% solution with `<combobox>` and other elements to
follow. Part of the [customizable select](../../features/customizable-select.md) history.

> RESOLVED: Tab key in selectmenu listbox closes the listbox and sets focus back on the button, regardless of tabbing direction. This happens even if there is interactive content in the listbox.

([resolution](https://github.com/openui/open-ui/issues/599#issuecomment-1234646146))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
