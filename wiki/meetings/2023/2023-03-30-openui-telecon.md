---
date: 2023-03-30
group: openui
type: telecon
topics_count: 2
issues: [565, 637]
generated_by: llm
---

# Open UI CG telecon — 2023-03-30

Two topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/03/30-openui-minutes.html](https://www.w3.org/2023/03/30-openui-minutes.html) (dated-URL convention for CG minutes).

Both topics concern `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## [selectmenu] Accept "option" elements through multiple slots ([openui/open-ui#565](https://github.com/openui/open-ui/issues/565))

The minutes record [jarhar](../../people/josepharhar.md) as presenting the use case: a custom element wrapping a `<selectmenu>`
wants its light-DOM `<option>` children re-slotted through into the listbox. He had been
hesitant (it seemed complicated) but got nested slotting for the listbox working in Chrome, and
proposed supporting it for the listbox only — other parts require a `slot` attribute and would
not work the same way. bkardell_ found the use case plausible but complicated, wondering whether
the accessibility could be kept from "blowing up"; [JakeA](../../people/jakearchibald.md) declined to weigh in at this level of
detail without an up-to-date explainer, and hidde suggested leaving the issue open to gather more
opinions rather than resolving with so few voices. No resolution was recorded.

## SelectMenu placeholder capability? ([openui/open-ui#637](https://github.com/openui/open-ui/issues/637))

Continuing from [the 2023-01-05 resolution](2023-01-05-openui-telecon.md) to support placeholders
in some form, the group dug into the design. The minutes record [jarhar](../../people/josepharhar.md) as proposing a
`placeholder` attribute plus a default-value mechanism; una as enumerating four use cases the
design must cover (including a purely presentational placeholder vs one that is also the
selected value); and [JakeA](../../people/jakearchibald.md) as arguing a placeholder must support rich content — hence tagging an
`<option>` as the placeholder rather than a text attribute. [scotto](../../people/scottaohara.md) (with a codepen) showed the
classic `<option selected hidden>` pattern authors use today (which does not work in Safari), and
warned both about reflecting arbitrary content into the trigger and about whether a dedicated
placeholder is needed at all, given placeholder text in inputs is already an accessibility
problem. [flackr](../../people/flackr.md) argued no separate placeholder feature is needed if an option can be excluded
from the selectable list; bkardell_ probed the index/selectedIndex weirdness of a
placeholder-option. The group ended unsure whether existing mechanisms suffice.
No resolution was recorded.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
