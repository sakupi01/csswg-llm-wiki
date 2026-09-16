---
date: 2024-11-14
group: openui
type: telecon
topics_count: 2
issues: [1118, 1127]
generated_by: llm
---

# Open UI CG telecon — 2024-11-14

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/11/14-openui-minutes.html](https://www.w3.org/2024/11/14-openui-minutes.html)
(dated-URL convention for CG minutes).

## select: provide a way for authors to define the string value of rich options ([openui/open-ui#1118](https://github.com/openui/open-ui/issues/1118))

sarah raised typeahead on rich options in the [customizable
select](../../features/customizable-select.md): with complex option content (name + role + status),
the raw text content is the wrong search string. The minutes record [gregwhitworth](../../people/gregwhitworth.md) as pointing to
the combobox explainer's `search` attribute as the same problem, [masonf](../../people/mfreed7.md) as calling a per-option
attribute a foot-gun (attribute and content silently diverge) and noting today's typeahead is not
even specced, and [brecht_dr](../../people/brechtDR.md) as urging the group not to make v1 a "swiss army knife". The consensus
was to pull the typeahead/search design into its own explainer as a fast-follow rather than block
v1 — [gregwhitworth](../../people/gregwhitworth.md) stressing v2 need not take years — with sarah cautioning the mismatch is more
common than a corner case. No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1118#issuecomment-2477288690))

## select: use cases for opening the picker without user activation ([openui/open-ui#1127](https://github.com/openui/open-ui/issues/1127))

Answering a WHATWG question: `showPicker()` requires user activation because native pickers open
privileged windows, but the [customizable select](../../features/customizable-select.md) picker is
just in-page content. The minutes record [masonf](../../people/mfreed7.md) as seeing no security concern and hunting for use
cases, [gregwhitworth](../../people/gregwhitworth.md) as initially preferring to keep the status quo, and sarah as supplying the
convincing cases — editable comboboxes that open on focus and "teaching UI" that opens the picker
programmatically ([dbaron](../../people/dbaron.md) +1). The group resolved that the use cases are real.

> RESOLVED: There are real world usecases for opening a picker using programmatic activation on a custom select

([resolution](https://github.com/openui/open-ui/issues/1127#issuecomment-2477226488))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
