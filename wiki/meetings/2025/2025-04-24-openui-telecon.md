---
date: 2025-04-24
group: openui
type: telecon
topics_count: 3
issues: [1188, 1189, 1200]
generated_by: llm
---

# Open UI CG telecon — 2025-04-24

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/04/24-openui-minutes.html](https://www.w3.org/2025/04/24-openui-minutes.html) (dated-URL convention for CG minutes).

## [menu] How should we group checkboxes and radios, and how should we decide if they are checkboxes or radios? ([openui/open-ui#1189](https://github.com/openui/open-ui/issues/1189))

For the menu elements proposal, how to mark a group of `<menuitem>`s as checkboxes or radios.
The minutes record [jarhar](../../people/josepharhar.md) as preferring a grouping approach over dedicated elements, and
domfarolino as advocating a single `checkable` attribute on `<fieldset>` taking a value of
`multiple`, rather than a separate `multiple` attribute. [lwarlow](../../people/lukewarlow.md), who had proposed the separate
`multiple` attribute (mirroring `<select>`), said he still leaned that way but could live with
the enum; scott raised (and set aside) whether `checkable` reads oddly for single-check groups.

> RESOLVED: group menuitem radios and checkboxes with the fieldset element. the fieldset element will take a checkable attribute with a default value of single, which can be set to multiple to indicate single-select or multi-select

([resolution](https://github.com/openui/open-ui/issues/1189#issuecomment-2828496203))

## Other topics

- [openui/open-ui#1188](https://github.com/openui/open-ui/issues/1188) — [menu] improve distinction between menubar and toolbar; resolved to pursue menubar in the menu elements proposal and leave toolbar as a potential follow-up ([resolution](https://github.com/openui/open-ui/issues/1188#issuecomment-2828515741)).
- [openui/open-ui#1200](https://github.com/openui/open-ui/issues/1200) — [menu] do we *need* to introduce menuitem elements?; resolved to keep introducing `<menuitem>` rather than reusing buttons ([resolution](https://github.com/openui/open-ui/issues/1200#issuecomment-2828587753)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
