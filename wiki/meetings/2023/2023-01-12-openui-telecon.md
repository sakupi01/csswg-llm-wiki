---
date: 2023-01-12
group: openui
type: telecon
topics_count: 3
issues: [342, 646, 648]
generated_by: llm
---

# Open UI CG telecon — 2023-01-12

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/01/12-openui-minutes.html](https://www.w3.org/2023/01/12-openui-minutes.html).

## [selectmenu] Mechanism to use `<select>` as progressive enhancement? ([openui/open-ui#648](https://github.com/openui/open-ui/issues/648))

A suggestion from hdv: nest a `<select>` inside `<selectmenu>` so supporting browsers get the new
control and older ones fall back to the classic one. This thread feeds directly into the
progressive-enhancement story of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [scotto](../../people/scottaohara.md) as
questioning why `<select>` alone would be kicked out when `<selectmenu>` accepts arbitrary
content, while Brecht_De_Ruyte argued a built-in fallback would speed adoption for sites that
must support older browsers. [dbaron](../../people/dbaron.md) is recorded as calling the idea interesting but warning that
the layer at which the "ignoring" happens (parse time or later) matters and every option may have
downsides; [masonf](../../people/mfreed7.md) agreed there may be parser edge cases, and tbondwilkinson noted the lack of a
generalized `@supports`-style mechanism for elements. [gregwhitworth](../../people/gregwhitworth.md) summarised the outcome: the
group agrees a progressive-enhancement solution is needed but not on how to do it.
No resolution was recorded.

## Other topics

- [openui/open-ui#342](https://github.com/openui/open-ui/issues/342) — agreed to add an asynchronous `aftertoggle` popover event ([resolution](https://github.com/openui/open-ui/issues/342#issuecomment-1380882740)).
- [openui/open-ui#646](https://github.com/openui/open-ui/issues/646) — the `popovershowtarget`/`popoverhidetarget` functionality stays in the API, exact shape still open ([resolution](https://github.com/openui/open-ui/issues/646#issuecomment-1380896870)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
