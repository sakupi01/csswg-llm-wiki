---
date: 2026-07-30
group: openui
type: telecon
topics_count: 4
issues: [1459, 1483, 1489, 1491]
generated_by: llm
---

# Open UI CG telecon — 2026-07-30

Four topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/07/30-openui-minutes.html](https://www.w3.org/2026/07/30-openui-minutes.html) (dated-URL convention for CG minutes).

## Link input elements with a slider value ([openui/open-ui#1459](https://github.com/openui/open-ui/issues/1459))

**Data gap**: the bot comment for this date contains an empty IRC log
([bot comment](https://github.com/openui/open-ui/issues/1459#issuecomment-5134540186)), so the
discussion — pairing a numeric `<input>` with a slider's value — cannot be reconstructed from the
mirror. No resolution was recorded.

## Making a filterable select with an attribute ([openui/open-ui#1491](https://github.com/openui/open-ui/issues/1491))

An alternative shape for filterable customizable `<select>`: an attribute that makes the browser
create the filter `<input>` in the select's shadow root
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
asking which parts of the input's API would need re-exposing; [masonf](../../people/mfreed7.md) suggested enumerating the
surface (a `searchvalue` property, the input event, maybe the Selection API) and noted developers
will want everything. [flackr](../../people/flackr.md) liked the approach as less awkward than the alternatives, pointing
to the earlier resolution to expose pseudo-element targets on events for disambiguation. [dbaron](../../people/dbaron.md)
floated the two-child container element pattern from the submenu work as another option; [jarhar](../../people/josepharhar.md)
was recorded as preferring a small opt-in, noting the sibling-input design was not well received
at WHATWG, and took actions to inventory the input API surface and get Mozilla feedback.
No resolution was recorded.

([discussion](https://github.com/openui/open-ui/issues/1491#issuecomment-5134684046))

## Other topics

- [openui/open-ui#1483](https://github.com/openui/open-ui/issues/1483) — declarative feature detection for focusgroup was declined ("interesting idea, but we don't think it's needed") ([resolution](https://github.com/openui/open-ui/issues/1483#issuecomment-5135876916)).
- [openui/open-ui#1489](https://github.com/openui/open-ui/issues/1489) — bikeshedding names for the focusgroup `itemcontrols` modifiers, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
