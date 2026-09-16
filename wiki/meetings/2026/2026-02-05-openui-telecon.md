---
date: 2026-02-05
group: openui
type: telecon
topics_count: 3
issues: [1355, 1363, 1366]
generated_by: llm
---

# Open UI CG telecon — 2026-02-05

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/02/05-openui-minutes.html](https://www.w3.org/2026/02/05-openui-minutes.html) (dated-URL convention for CG minutes).

## [Select] What to do with selectedcontent when multiple select is set with size 1 ([openui/open-ui#1355](https://github.com/openui/open-ui/issues/1355))

A long debate on how `<selectedcontent>` should render multiple selected options in the
customizable `<select>` (see [customizable select](../../features/customizable-select.md)).
The minutes record [brecht_dr](../../people/brechtDR.md) as proposing that all selected options' content be cloned in, and
maikelkrause4 as wanting each option wrapped so UA styles can separate them; [keithamus](../../people/keithamus.md) floated
letting authors supply one `<selectedcontent>` per selection. [jarhar](../../people/josepharhar.md) and [masonf](../../people/mfreed7.md) pushed back on
"magic" wrappers (authors will restyle anyway; cloning `<option>` itself would require reworking
many algorithms), while [masonf](../../people/mfreed7.md) and [brecht_dr](../../people/brechtDR.md) worried that plain concatenated text is unreadable
by default. The group converged on an opt-out wrapper attribute.

> RESOLVED: <selectedcontent wrap={yes|no}> where the default is yes for multi-select, and no for single-select. Wrapper is a div or span.

([resolution](https://github.com/openui/open-ui/issues/1355#issuecomment-3855878975))

## Implied case folding with Combobox search attribute ([openui/open-ui#1366](https://github.com/openui/open-ui/issues/1366))

Follow-up on the combobox filtering design for the customizable `<select>` family
(see [customizable select](../../features/customizable-select.md)). The minutes record [keithamus](../../people/keithamus.md)
as relaying [hsivonen](../../people/hsivonen.md)'s concern that substring matching needs case folding, which collides with
the "keep it simple" design and has no JavaScript equivalent. [dbaron](../../people/dbaron.md) is recorded as noting i18n
circles know no single correct algorithm (diacritic elision is language-specific; Turkish dotted
and dotless I are a classic trap). [masonf](../../people/mfreed7.md) suggested specifying intent and letting browsers refine
behavior over time, as they already do for type-ahead; [jarhar](../../people/josepharhar.md) said he would rather drop the
attribute than stay blocked. No resolution was recorded.

([discussion](https://github.com/openui/open-ui/issues/1366#issuecomment-3855924156))

## Other topics

- [openui/open-ui#1363](https://github.com/openui/open-ui/issues/1363) — the group agreed a pseudo-class should match a `<menuitem>` whose submenu is open, resolving ":open matches a menuitem that triggers a submenu, and that submenu is currently open (confirm with all vendors)" ([resolution](https://github.com/openui/open-ui/issues/1363#issuecomment-3854729244)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
