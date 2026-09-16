---
date: 2025-05-08
group: openui
type: telecon
topics_count: 3
issues: [1038, 1196, 1201]
generated_by: llm
---

# Open UI CG telecon — 2025-05-08

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/05/08-openui-minutes.html](https://www.w3.org/2025/05/08-openui-minutes.html) (dated-URL convention for CG minutes).

## [command invokers] `command=set/reset/clear` for form inputs ([openui/open-ui#1038](https://github.com/openui/open-ui/issues/1038))

Declarative commands acting on individual form fields. The minutes record [keithamus](../../people/keithamus.md) as framing it
as explaining the search input's clear button without script; [lwarlow](../../people/lukewarlow.md) connected it to the CSS
forms work on replaceable UA buttons (step up/down, clear) and saw the clear/reset cases but not
`set`; [keithamus](../../people/keithamus.md) leaned to `reset` as strictly more capable than clear. scott noted a clear
command that works outside `<form>` is useful but that clear buttons are conventionally exposed
as buttons kept out of the tab order, which deserves author guidance. [masonf](../../people/mfreed7.md) placed it on the
future-enhancements list rather than the initial command set.

> RESOLVED: Add reset or clear to explainer.

([resolution](https://github.com/openui/open-ui/issues/1038#issuecomment-2864010660))

## Other topics

- [openui/open-ui#1196](https://github.com/openui/open-ui/issues/1196) — [menu] allow buttons to open menu(list) popups; resolved to support opening menulists via buttons with a new command value ([resolution](https://github.com/openui/open-ui/issues/1196#issuecomment-2863984662)).
- [openui/open-ui#1201](https://github.com/openui/open-ui/issues/1201) — [menu] define orientation attribute; resolved to define a new orientation HTML attribute affecting styles, keyboard navigation and aria-orientation ([resolution](https://github.com/openui/open-ui/issues/1201#issuecomment-2863948841)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
