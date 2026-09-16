---
date: 2026-01-08
group: openui
type: telecon
topics_count: 2
issues: [1217, 1351]
generated_by: llm
---

# Open UI CG telecon — 2026-01-08

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/01/08-openui-minutes.html](https://www.w3.org/2026/01/08-openui-minutes.html) (linked from the bot's IRC log).

## Should select multiple with popup have OK/Cancel buttons? ([openui/open-ui#1217](https://github.com/openui/open-ui/issues/1217))

Part of the multi-select work on the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The group revisited an
earlier decision to add a close button to the default multi-select picker: the minutes record
[jarhar](../../people/josepharhar.md) as saying that specifying such a button raises hard questions (content, customization,
localization of its label) and that he wanted to revisit whether it is needed at all. [masonf](../../people/mfreed7.md) and
[lwarlow](../../people/lukewarlow.md) are recorded as preferring no built-in buttons — authors can add their own declaratively,
and [lwarlow](../../people/lukewarlow.md) noted existing component libraries offer no close/cancel mechanism either. scott is
recorded as pressing for documented answers rather than a particular outcome, noting Windows and
macOS platform conventions for Escape/cancel differ, and [keithamus](../../people/keithamus.md) recounted GitHub's experience
that light dismiss committing the selection tested better with assistive-technology users.

> RESOLVED: Don't add buttons in default pickers.

([resolution](https://github.com/openui/open-ui/issues/1217#issuecomment-3725472817))

## [listbox] Usability downgrades with new customisable listbox ([openui/open-ui#1351](https://github.com/openui/open-ui/issues/1351))

Also on the customizable `<select>` listbox
(see [customizable select](../../features/customizable-select.md)). The minutes record [lwarlow](../../people/lukewarlow.md)
as reporting capabilities lost relative to the native multi-select listbox: Ctrl+A select-all no
longer works, and the form can no longer be submitted from inside the listbox. [masonf](../../people/mfreed7.md) questioned
how widely known those native behaviors are and suggested the common "check all" checkbox pattern
— or a future `select-all` command invoker — might serve better; [jarhar](../../people/josepharhar.md) noted he would be fine
implementing Ctrl+A but found shift+arrow range selection confusing in the react-aria example.
The group opted not to change anything yet.

> RESOLVED: wait and see on this question - don't make changes now.

([resolution](https://github.com/openui/open-ui/issues/1351#issuecomment-3725536132))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
