---
date: 2024-10-24
group: openui
type: telecon
topics_count: 2
issues: [825, 1114]
generated_by: llm
---

# Open UI CG telecon — 2024-10-24

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/10/24-openui-minutes.html](https://www.w3.org/2024/10/24-openui-minutes.html)
(dated-URL convention for CG minutes).

## select: Should `<selectedoption>` respond to mutations in the selected `<option>` ([openui/open-ui#825](https://github.com/openui/open-ui/issues/825))

A reversal of the [2024-04-25](2024-04-25-openui-telecon.md) resolution for [customizable
select](../../features/customizable-select.md). [JakeA](../../people/jakearchibald.md) laid out why observing mutations does not
hold up: WebKit found asynchronous recloning weird, synchronous recloning fires far more often than
authors expect, and there is no way to opt out when an author deliberately diverges the button copy
(hover effects, self-mutating elements like `hidden-until-found`). The minutes record steveOrvell
as noting the visible/accessible-name split this can create ([masonf](../../people/mfreed7.md) calling the current mismatch a
bug to fix), sarah as arguing anyone mutating options via script has a render function anyway, and
[masonf](../../people/mfreed7.md) as withdrawing part of his earlier position while keeping a proposal for an explicit
"synchronise" method. Clone-on-reselect edge cases were spun out (see
[2024-10-31](2024-10-31-openui-telecon.md)).

> RESOLVED: dont observe mutations in option elements. only clone into selectedoption during parsing and when a new option becomes selected

([resolution](https://github.com/openui/open-ui/issues/825#issuecomment-2436124668))

## Other topics

- [openui/open-ui#1114](https://github.com/openui/open-ui/issues/1114) — the utility of the
  `popover=hint` feature; its resolution was recorded the following week, on
  [2024-11-07](2024-11-07-openui-telecon.md).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
