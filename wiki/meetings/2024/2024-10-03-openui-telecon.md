---
date: 2024-10-03
group: openui
type: telecon
topics_count: 2
issues: [1099, 1102]
generated_by: llm
---

# Open UI CG telecon — 2024-10-03

Two topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/10/03-openui-minutes.html](https://www.w3.org/2024/10/03-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] rendering elements which don't fit the content model ([openui/open-ui#1099](https://github.com/openui/open-ui/issues/1099))

Post-TPAC follow-up on what the [customizable
select](../../features/customizable-select.md) should do with content outside its model. The
minutes record [jarhar](../../people/josepharhar.md) as relaying jamesn's TPAC concern ("I don't want to make it possible to make
stuff that works for sighted users but not assistive tech users"); [masonf](../../people/mfreed7.md) as arguing strongly for
rendering everything with loud console warnings — restricting rendering forever forecloses
evolution, and developers locked out will rebuild with inaccessible divs; [keithamus](../../people/keithamus.md) as wanting
parser restrictions lifted and proposing CSP-style aggregate accessibility-violation reporting;
naman as nervous about inputs specifically; and jamesn and [scotto](../../people/scottaohara.md) as insisting Aaron, Jamie, and
Matt King be heard before deciding, [scotto](../../people/scottaohara.md) volunteering to draft a short list of absolute no's.
No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1099#issuecomment-2392104438))

## Does `<select multiple>` need a button and popup by default? ([openui/open-ui#1102](https://github.com/openui/open-ui/issues/1102))

[jarhar](../../people/josepharhar.md) opened the multi-select chapter of [customizable
select](../../features/customizable-select.md): without a default button/popup he can ship
`<select multiple>` easily as an in-page control with checkboxes, letting authors wire their own
button + popover for the dropdown pattern; naman found that acceptable. The minutes record [scotto](../../people/scottaohara.md)
as recalling Sarah Higley's UX studies on multi-select dropdowns ("it was a tire fire" — users do
not know how to select items) and suggesting the modest glow-up plus a checkbox-group model, and
jamesn as asking whether this would actually satisfy design systems. No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1102#issuecomment-2392119169))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
