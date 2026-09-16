---
date: 2023-12-07
group: openui
type: telecon
topics_count: 3
issues: [956, 969, 970]
generated_by: llm
---

# Open UI CG telecon — 2023-12-07

Three topics, two resolutions — including the pivotal decision to abandon the `<selectlist>`
element in favour of reusing `<select>` itself, the direction that became the customizable
`<select>` (see [customizable select](../../features/customizable-select.md)). Minutes recorded
by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/12/07-openui-minutes.html](https://www.w3.org/2023/12/07-openui-minutes.html) (dated-URL convention for CG minutes).

## selectlist feedback from apple ([openui/open-ui#970](https://github.com/openui/open-ui/issues/970))

The minutes record jarhar_ as relaying feedback from his WHATWG issue and discussions with Anne
([annevk](../../people/annevk.md), Apple): reuse `<select>` rather than mint `<selectlist>`, and reuse `<datalist>` rather
than a new `listbox` element — and proposing to accept both. [masonf](../../people/mfreed7.md) admitted he had initially
opposed this as an implementation nightmare, but the parser turns out to help: old browsers throw
away unrecognised content inside `<select>`, giving natural graceful degradation (a `select
multiple` with new content just falls back). Luke supported it for progressive enhancement while
flagging the unresolved `multiple` story and the split-button use cases; [dandclark](../../people/dandclark.md) warned parser
changes are scary — the old hacks exist for a reason — and asked about feature detection (jarhar_:
check for the `selectedoption` element) and the bag of legacy `<select>` attributes (`size`,
`type`) previously excluded from selectlist. scotto_ raised platform accessibility mappings
(combobox means different things on macOS vs Windows) — [masonf](../../people/mfreed7.md) noted the new behavior forks only
when authors opt in (e.g. a `datalist` child), so mappings can be defined then — and suggested
the selectlist work still has legs as a future menu-element proposal.

> RESOLVED: Reuse the select element instead of creating the selectlist element and reuse the datalist element for selectlist/select instead of using a new listbox element for it

([resolution](https://github.com/openui/open-ui/issues/970#issuecomment-1846026582))

## Other topics

- [openui/open-ui#956](https://github.com/openui/open-ui/issues/956) — resolved to defer the invoker `toggle`/`show` actions and remove the explicit `toggleModal` string ([resolution](https://github.com/openui/open-ui/issues/956#issuecomment-1845987671)).
- [openui/open-ui#969](https://github.com/openui/open-ui/issues/969) — casing for invoker action values, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
