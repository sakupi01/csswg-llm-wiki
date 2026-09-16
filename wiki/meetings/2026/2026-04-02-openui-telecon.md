---
date: 2026-04-02
group: openui
type: telecon
topics_count: 3
issues: [847, 931, 1319]
generated_by: llm
---

# Open UI CG telecon — 2026-04-02

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/04/02-openui-minutes.html](https://www.w3.org/2026/04/02-openui-minutes.html) (linked from the bot's IRC log).

## How to make an accessible searchable "select" list? ([openui/open-ui#847](https://github.com/openui/open-ui/issues/847))

The filterable-select design for the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
proposing to allow an `<input>` directly inside `<select>` (as the first element child, for
parser-compat and slotting reasons) instead of the current sibling-input-plus-idref pattern.
scott is recorded as liking the precedent (legend-in-fieldset); [keithamus](../../people/keithamus.md) and sarah raised that
designers commonly wrap inputs in a div or add leading icons, which a strict first-child rule
forbids. [jarhar](../../people/josepharhar.md) warned that allowing wrappers generalizes to "any interactive content inside
select", effectively a dialog-based picker; scott flagged that an implicit input needs an
accessible name, which is not trivial. The group sent the options outward for feedback.

> RESOLVED: Take feedback to WHATWG and solicit more feedback from authors on these options

([resolution](https://github.com/openui/open-ui/issues/847#issuecomment-4179758599))

## Combobox search attribute and its values ([openui/open-ui#931](https://github.com/openui/open-ui/issues/931))

Design of the `beforefilter` event for filterable/combobox selects
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
presenting two shapes: option 1, an event carrying a promise resolving to the filtered options;
option 2, a per-option `filtered` IDL flag plus `preventDefault()`, with no promises. [masonf](../../people/mfreed7.md) is
recorded as raising multi-listener orchestration (a promise can only be resolved once), and
[keithamus](../../people/keithamus.md) gave GitHub's search bar — multiple teams populating one input — as a concrete case
against the promise design; [masonf](../../people/mfreed7.md) added that hoisting promises out of event scope invites timing
bugs and leaks. sarah agreed option 2 is easier to fit into existing async architectures, and the
group also leaned toward no built-in loading/loaded screen-reader announcements for async
filtering, leaving that to authors.

> RESOLVED: choose option 2

([resolution](https://github.com/openui/open-ui/issues/931#issuecomment-4179888495))

## [combobox] supporting autocomplete use cases in aria practices guide ([openui/open-ui#1319](https://github.com/openui/open-ui/issues/1319))

This item was on the agenda for a resolution on auto-copying the active option into the input,
but the slot was consumed by the [openui/open-ui#931](https://github.com/openui/open-ui/issues/931)
discussion by mistake — [jarhar](../../people/josepharhar.md) later commented that he had mixed the two issues up, and the bot
log for this item records only the opening remark
([comment](https://github.com/openui/open-ui/issues/1319#issuecomment-4180905810)). No resolution
was recorded; the topic returned the following week.

([discussion](https://github.com/openui/open-ui/issues/1319#issuecomment-4179782278))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
