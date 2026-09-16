---
date: 2023-05-11
group: openui
type: telecon
topics_count: 3
issues: [737, 741, 742]
generated_by: llm
---

# Open UI CG telecon — 2023-05-11

Three topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/05/11-openui-minutes.html](https://www.w3.org/2023/05/11-openui-minutes.html) (dated-URL convention for CG minutes).

## `<selectmenu>` eagerly makes selections ([openui/open-ui#742](https://github.com/openui/open-ui/issues/742))

Event semantics for `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [argyle](../../people/argyleink.md) as
reporting that on Windows, arrowing through an open `<select>` eagerly fires `change` events
before the user has committed a choice — disruptive when the select drives layout or navigation.
Brecht_DR and [sarah_higley](../../people/smhigley.md) preferred committing only on explicit selection; [sarah_higley](../../people/smhigley.md) added
that the Windows escape behavior (committing the arrowed-to value) matches no other control,
including native comboboxes, and later verified the JS events actually fire only on close.
[dbaron](../../people/dbaron.md) dissented on escape — his intuition, from long Windows/Linux web use, was that escape
keeps the currently arrowed-to option. A side thread on selectmenu width tracking the selected
option (jank vs. a genuinely new capability, per [argyle](../../people/argyleink.md)) was split into a separate issue.

> RESOLVED: selectmenu should fire `input` as options are visited with the mouse or keyboard, and `change` is fired only when an option is selected. Escape acts as "undo" and does not fire a `change` event. Visiting options does *not* update the "selected" or "previewed" value.

([resolution](https://github.com/openui/open-ui/issues/742#issuecomment-1544234741))

## Other topics

- [openui/open-ui#737](https://github.com/openui/open-ui/issues/737) — meta discussion on explainers deferring to specs where appropriate.
- [openui/open-ui#741](https://github.com/openui/open-ui/issues/741) — dialogs with popover-like triggers, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
