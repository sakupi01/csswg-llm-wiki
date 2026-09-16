---
date: 2023-03-02
group: openui
type: telecon
topics_count: 3
issues: [386, 433, 665]
generated_by: llm
---

# Open UI CG telecon — 2023-03-02

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/03/02-openui-minutes.html](https://www.w3.org/2023/03/02-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics define keyboard behavior for `<selectmenu>`, the precursor of the
customizable `<select>` (see [customizable select](../../features/customizable-select.md)).

## Arrow key up/down on closed `<selectmenu>` ([openui/open-ui#433](https://github.com/openui/open-ui/issues/433))

Classic `<select>` arrow-key behavior differs by OS: on Windows/Linux, up/left and down/right
move between options on a closed select; on macOS the arrows open the listbox without changing
the selection. The minutes record a long consistency debate: [masonf](../../people/mfreed7.md) argued for matching the
majority of user expectations with one interoperable behavior, since component libraries do not
adapt per platform; bkardell_ countered that a Domenic poll on platform-vs-uniform behavior split
roughly 50/50 and suggested asking design-system owners (FAST, Material, Lightning, Adobe);
[flackr](../../people/flackr.md) made the case for platform consistency by precedent. [jarhar](../../people/josepharhar.md) concluded the group should
pick one cross-OS behavior and proposed following macOS, since cycling options invisibly is
confusing. [dbaron](../../people/dbaron.md) flagged an i18n concern with treating left/right like up/down in vertical
writing modes, and [masonf](../../people/mfreed7.md) stressed this is "resolved for now". The resolution was recorded on the
[#386 bot comment](https://github.com/openui/open-ui/issues/386#issuecomment-1452469497):

> RESOLVED: Up, down, left, and right open the listbox without changing the selected option

## Clarify use of Enter/Space keys for opening/closing listbox ([openui/open-ui#386](https://github.com/openui/open-ui/issues/386))

The minutes record [jarhar](../../people/josepharhar.md) as proposing Enter/Space behavior aligned with what classic `<select>`
does across platforms (with [scotto](../../people/scottaohara.md) emphasising that Enter on a closed control should submit the
form; the ARIA Authoring Practices Guide is less clear, and bkardell_ suggested filing an APG
issue to align it). [masonf](../../people/mfreed7.md) confirmed that with no form to submit, Enter on a closed control does
nothing.

> RESOLVED: Spacebar while the listbox is closed should open the listbox. Spacebar while the listbox is open should do typeahead. Enter when the listbox is open should choose the selected item and close the listbox. Enter when the listbox is closed should submit the form.

([resolution](https://github.com/openui/open-ui/issues/386#issuecomment-1452469497))

## Other topics

- [openui/open-ui#665](https://github.com/openui/open-ui/issues/665) — agreed to move telecons to 8–9AM PST for inclusivity ([resolution](https://github.com/openui/open-ui/issues/665#issuecomment-1452421129)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
