---
date: 2022-10-20
group: openui
type: telecon
topics_count: 4
issues: [415, 483, 598, 610]
generated_by: llm
---

# Open UI CG telecon — 2022-10-20

Four topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-10-20](https://www.w3.org/2022/10/20-openui-minutes.html).

## `<selectmenu>` always snaps shut when opened with mouse ([openui/open-ui#483](https://github.com/openui/open-ui/issues/483))

Closing out the April discussion of the form-association trap: a light-DOM `<button>` slotted
into a `<selectmenu>` inside a `<form>` gets auto-associated and submits the form on click. The
minutes record [dandclark](../../people/dandclark.md) concluding there is no quick fix that doesn't add complexity to an
already corner-case-rich part of the HTML parser, that the same problem hits form-associated
custom elements generally, and proposing to do nothing selectmenu-specific. The minutes record
[masonf](../../people/mfreed7.md) agreeing (recalling a "one week" form-association project that took a new employee a
year) and [scotto](../../people/scottaohara.md) noting the practical answer is authoring guidance to always write
`<button type="button">`. Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: Don't make any special rules preventing `selectmenu` child elements from being form-associated.

([resolution](https://github.com/openui/open-ui/issues/483#issuecomment-1285967239))

## `<p>` element parser rules cause content to be kicked out of `<selectmenu>` ([openui/open-ui#598](https://github.com/openui/open-ui/issues/598))

The minutes record [dandclark](../../people/dandclark.md) describing the HTML parser problem [scotto](../../people/scottaohara.md) had spotted: inside a
`<p>`, elements like `<hr>` in a `<selectmenu>` auto-close the paragraph and kick content out of
the selectmenu. The parser already special-cases `<button>` via the "has a p element in button
scope" algorithm, so the fix is to add `selectmenu` to that list. The minutes record [masonf](../../people/mfreed7.md)
agreeing it must be solved ("people will put a selectmenu in a paragraph") and judging the
parser change less risky than upcoming shadow-DOM parser changes. Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: Add `selectmenu` to the HTML parser's `has a p element in button scope` algorithm and rename the algo appropriately.

([resolution](https://github.com/openui/open-ui/issues/598#issuecomment-1285956512))

## Other topics

- [openui/open-ui#415](https://github.com/openui/open-ui/issues/415) — resolved that blur is not a light dismiss trigger for pop-ups ([resolution](https://github.com/openui/open-ui/issues/415#issuecomment-1285995113)).
- [openui/open-ui#610](https://github.com/openui/open-ui/issues/610) — resolved to add a `togglePopUp()` method ([resolution](https://github.com/openui/open-ui/issues/610#issuecomment-1285950492)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
