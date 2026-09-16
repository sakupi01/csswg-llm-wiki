---
date: 2024-02-01
group: openui
type: telecon
topics_count: 1
issues: [985]
generated_by: llm
---

# Open UI CG telecon — 2024-02-01

One topic, three resolutions. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2024/02/01-openui-minutes.html](https://www.w3.org/2024/02/01-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] How to enable interoperable DOM, behaviors and user-agent styles for `<select>` ([openui/open-ui#985](https://github.com/openui/open-ui/issues/985))

The foundational opt-in debate for [customizable
select](../../features/customizable-select.md). [gregwhitworth](../../people/gregwhitworth.md) walked through five candidate
mechanisms (CSS `appearance`, an HTML attribute, a new element, or content-based parser opt-in);
the minutes record [dbaron](../../people/dbaron.md) as warning that CSS influencing DOM structure repeats Mozilla's XBL1
design mistake, and [masonf](../../people/mfreed7.md) as noting only the split model had Apple support. lukew initially
objected to separating the styling opt-in from the DOM/behavior opt-in but the group resolved to
keep them independent; `appearance: base-select` (not bare `base`, to avoid `* { appearance: base }`
foot-guns) was chosen for styles, and a poll picked a new attribute (name TBD) over the
content-based option for DOM/behavior — [jarhar](../../people/josepharhar.md) predicting WHATWG pushback on the attribute.

> RESOLVED: trigger for dom structure and behavior should be independent from the trigger for interoperable styles

> RESOLVED: the opt-in for interoperable styling should be a new value for the `appearance` property, such as `base-select` or maybe `base`.

> RESOLVED: Use a new attribute (name TBD) to opts that <select> into the new behaviors and DOM structure

([resolutions](https://github.com/openui/open-ui/issues/985#issuecomment-1922141513))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
