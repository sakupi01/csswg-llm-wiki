---
date: 2026-07-09
group: openui
type: telecon
topics_count: 6
issues: [226, 1118, 1189, 1220, 1227, 1465]
generated_by: llm
---

# Open UI CG telecon — 2026-07-09

Six topics, five resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/07/09-openui-minutes.html](https://www.w3.org/2026/07/09-openui-minutes.html) (linked from the bot's IRC log).

## select: provide a way for authors to define the string value of rich options ([openui/open-ui#1118](https://github.com/openui/open-ui/issues/1118))

For rich options in the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record sarah as
laying out Fluent's need: a rich option (name plus email, status, etc.) has up to four distinct
text representations — button rendering, picker rendering, typeahead matching, and filter
matching. [lwarlow](../../people/lukewarlow.md) argued the existing `label` attribute is compromised (it already replaces the
option's rendered content) and proposed a new string attribute (placeholder name "bruce"); lea
posted support for reusing `label`. [gregwhitworth](../../people/gregwhitworth.md) is recorded as noting the group could invent
solutions all day and no consensus will come without a concrete proposal, suggesting working
sessions coordinated with focusgroup and menu work.

> RESOLVED: Workshop a concrete design for this, meanwhile investigate adding a use counter for label.

([resolution](https://github.com/openui/open-ui/issues/1118#issuecomment-4928266893))

## [menu] How should we group checkboxes and radios, and how should we decide if they are checkboxes or radios? ([openui/open-ui#1189](https://github.com/openui/open-ui/issues/1189))

The minutes record [dbaron](../../people/dbaron.md) as introducing the grouping question for checkable menu items, noting
the proposal had drawn objections in a WHATWG meeting. sarah is recorded as favoring `<fieldset>`
as (at least) an option, since it gives a semantic grouping a visible label; [lwarlow](../../people/lukewarlow.md) argued a
containing element beats `type`/`name` attributes — it lets the browser force items to be uniformly
radios or checkboxes, closing off bad authoring — and that separate elements per role would allow
mixing and matching. [gregwhitworth](../../people/gregwhitworth.md) backed the container but cautioned against boxing out a future
`radiogroup`-style element outside menus.

> RESOLVED: David to document rationales for fieldset approach in explainer

> RESOLVED: Also allow <fieldset> as a grouping element for non-radio/checkbox menuitems.

([resolution](https://github.com/openui/open-ui/issues/1189#issuecomment-4928386129))

## Keyboard behaviour of custom select options ([openui/open-ui#1465](https://github.com/openui/open-ui/issues/1465))

Arrow-key behavior in the customizable `<select>` picker
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
asking whether Chromium should match Safari, where right acts as down and left as up, and how
arrow keys should work when options are laid out in a grid. [lwarlow](../../people/lukewarlow.md) is recorded as viewing
keyboard behavior as implementation-defined and preferring to solve layout-aware navigation
holistically via focusgroup rather than a select-specific fix; [gregwhitworth](../../people/gregwhitworth.md) disagreed with
treating listboxes as inherently vertical, citing horizontal game-style pickers. [dbaron](../../people/dbaron.md) suggested
defaults should be a function of writing mode and direction (vertical-rl being the awkward case).
[jarhar](../../people/josepharhar.md) posted a browser-difference matrix on the issue afterwards
([comment](https://github.com/openui/open-ui/issues/1465#issuecomment-4928627449)).
No resolution was recorded.

## Other topics

- [openui/open-ui#226](https://github.com/openui/open-ui/issues/226) — the token feature was closed as not planned for lack of a champion ([resolution](https://github.com/openui/open-ui/issues/226#issuecomment-4928144724)).
- [openui/open-ui#1227](https://github.com/openui/open-ui/issues/1227) — resolved that `interestfor` should not work on disabled elements, with the `::interest-button` pseudo left for further exploration ([resolution](https://github.com/openui/open-ui/issues/1227#issuecomment-4928486339)).
- [openui/open-ui#1220](https://github.com/openui/open-ui/issues/1220) — the command-invokers scroll command, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
