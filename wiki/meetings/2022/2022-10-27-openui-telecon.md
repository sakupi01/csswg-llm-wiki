---
date: 2022-10-27
group: openui
type: telecon
topics_count: 2
issues: [571, 627]
generated_by: llm
---

# Open UI CG telecon — 2022-10-27

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-10-27](https://www.w3.org/2022/10/27-openui-minutes.html).

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

The minutes record [gregwhitworth](../../people/gregwhitworth.md) reporting back from his survey: almost no design system or
email client copies an option's complex content 1:1 into the trigger — even Gmail/Outlook show
only the value or a part of it — so his proposed resolution was to keep the current
innerText-only behavior. The minutes record [masonf](../../people/mfreed7.md) mostly agreeing but flagging icon fonts
(Material Symbols) as a case that innerText breaks, and floating imperative slotting; [scotto](../../people/scottaohara.md)
suggesting a `<template>` for author-defined trigger markup; [sarah_h](../../people/smhigley.md) proposing an idref
mechanism ("selected-value-for") to clone a designated part of an option; and [tantek](../../people/tantek.md) arguing
that if the DOM were cloned, CSS alone could hide the unwanted pieces. After [masonf](../../people/mfreed7.md) noted a
cloning behavior could be opt-in (preserving back-compat), [gregwhitworth](../../people/gregwhitworth.md) is recorded as torn
— "let's not resolve on it today" — and took an action to write up the three paths forward.
No resolution was recorded on this issue. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/571#issuecomment-1293943290))

## Other topics

- [openui/open-ui#627](https://github.com/openui/open-ui/issues/627) — resolved to rename "pop-up" to "popover" for the entire API, settling the developer-confusion concern with `window.open` popups ([resolution](https://github.com/openui/open-ui/issues/627#issuecomment-1293918937)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
