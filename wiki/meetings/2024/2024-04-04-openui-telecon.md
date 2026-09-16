---
date: 2024-04-04
group: openui
type: telecon
topics_count: 2
issues: [1024, 1026]
generated_by: llm
---

# Open UI CG telecon — 2024-04-04

Two topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/04/04-openui-minutes.html](https://www.w3.org/2024/04/04-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] - Ensure any new UA defaults meet WCAG 2.2 target size (minimum) ([openui/open-ui#1026](https://github.com/openui/open-ui/issues/1026))

[scotto](../../people/scottaohara.md) asked that the default UA styles for the new [customizable
select](../../features/customizable-select.md) — and future controls like split buttons — meet WCAG
2.2's new 24×24px Target Size (Minimum) criterion. The minutes record lukew as strongly supportive
("the default control should be accessible to start with"), [masonf](../../people/mfreed7.md) as clarifying this constrains
defaults only (authors can still shrink targets), and [flackr](../../people/flackr.md) as suggesting 24px of *spacing* can
satisfy the requirement where a smaller control is wanted. SashaFirsov raised per-platform tap
sizes; the group noted WCAG's baseline is defined in CSS pixels.

> RESOLVED: For this and all future controls we resolve to ensure that interactive elements will not share the same area - with a boundary of 24px, meeting WCAG 2.5.8 Target Size requirements

([resolution](https://github.com/openui/open-ui/issues/1026#issuecomment-2037934427))

## Other topics

- [openui/open-ui#1024](https://github.com/openui/open-ui/issues/1024) — imperative invoker
  relationships; two resolutions were recorded
  ([resolution](https://github.com/openui/open-ui/issues/1024#issuecomment-2037882914)):

> RESOLVED: add an option to showPopover() to declare the invoking element.

> RESOLVED: invoketarget=popover should create the same relationships (e.g. nesting and keyboard behavior) that popovertarget=popover does. Behavior TBD for interesttarget attribute.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
