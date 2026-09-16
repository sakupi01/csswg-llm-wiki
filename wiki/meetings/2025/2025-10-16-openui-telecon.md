---
date: 2025-10-16
group: openui
type: telecon
topics_count: 2
issues: [847, 1273]
generated_by: llm
---

# Open UI CG telecon — 2025-10-16

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/10/16-openui-minutes.html](https://www.w3.org/2025/10/16-openui-minutes.html) (dated-URL convention for CG minutes).

## How to make an accessible searchable "select" list? ([openui/open-ui#847](https://github.com/openui/open-ui/issues/847))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). The minutes record [jarhar](../../people/josepharhar.md) as
reporting that every attempt to put a filter `<input>` inside customizable select ran into
accessibility-mapping and parser problems, and proposing sibling `<input>` and `<select>`
elements inside an author-provided picker instead. [keithamus](../../people/keithamus.md) stressed the server-side search case
(millions of options, debouncing, custom sorting/eliding) as too large to bake into the browser;
[masonf](../../people/mfreed7.md) insisted the JS override hooks must be in the first version because plain substring
matching is not good UX; scott asked what the cutoff is and flagged that the invoking button
would need explicit labeling, unlike an auto-generated one. [keithamus](../../people/keithamus.md) sketched a two-event design
(a preventDefault-able filter event plus a done event).

> RESOLVED: pursue sibling input and select elements with built-in filtering and keyboard behavior inside an author provided picker rather than putting input elements inside selects

([resolution](https://github.com/openui/open-ui/issues/847#issuecomment-3412348342))

## Some thoughts and questions about combobox ([openui/open-ui#1273](https://github.com/openui/open-ui/issues/1273))

Related to the customizable `<select>` family of form-control work — see
[customizable select](../../features/customizable-select.md). The minutes record [jarhar](../../people/josepharhar.md) as
proposing to drop the combobox explainer's new element in favour of improving `<input>` with
`<datalist>`, following the precedent of enhancing existing elements; [keithamus](../../people/keithamus.md) was enthusiastic
provided datalist becomes styleable with consistent events and APIs; scott agreed it solves many
use cases while noting complex patterns (tag lists, grouping) remain unsolved; [masonf](../../people/mfreed7.md) relayed
that [gregwhitworth](../../people/gregwhitworth.md) had championed the new element and asked what a new element could do that
upgraded existing elements can't — [jarhar](../../people/josepharhar.md) had no answer yet.

> RESOLVED: pursue input with datalist as an alternative to a new combobox element for now

([resolution](https://github.com/openui/open-ui/issues/1273#issuecomment-3412722822))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
