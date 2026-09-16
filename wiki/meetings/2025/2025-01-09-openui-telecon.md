---
date: 2025-01-09
group: openui
type: telecon
topics_count: 1
issues: [700]
generated_by: llm
---

# Open UI CG telecon — 2025-01-09

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [www.w3.org/2025/01/09-openui-minutes.html](https://www.w3.org/2025/01/09-openui-minutes.html) (dated-URL convention for CG minutes).

## Consider "toggle" (expand/collapse) attribute ([openui/open-ui#700](https://github.com/openui/open-ui/issues/700))

[lwarlow](../../people/lukewarlow.md) presented the case for a generic show/hide primitive: `<details>` is not the right
element for every expand/collapse pattern (app panels, expandable navigation, hamburger menus).
The minutes record [masonf](../../people/mfreed7.md) as pushing back — why isn't `<details>`/`<summary>` the answer, and
could its gaps be fixed instead? — while scott argued the semantics differ (a chevron button
expanding inline navigation is not a summary, and expand-all/collapse-all buttons don't fit the
details model). [masonf](../../people/mfreed7.md) then reframed the proposal as an `openable` attribute that only adds one
bit of state matching `:open`, sidestepping the display question; [lwarlow](../../people/lukewarlow.md) noted find-in-page
(`hidden=until-found`) interplay would need care. The minutes record [dbaron](../../people/dbaron.md) as objecting to JS
methods appearing and disappearing based on an attribute, which was left to follow popover's
precedent.

> RESOLVED: Add a global attribute called `openable` that opts an element into matching `:open`, adds JS methods like .open(), .close(), and .toggle(), and connects to command/commandfor. All names subject to bikeshedding.

([resolution](https://github.com/openui/open-ui/issues/700#issuecomment-2581101053))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
