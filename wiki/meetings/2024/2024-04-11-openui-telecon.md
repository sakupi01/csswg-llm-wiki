---
date: 2024-04-11
group: openui
type: telecon
topics_count: 2
issues: [872, 1032]
generated_by: llm
---

# Open UI CG telecon — 2024-04-11

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/04/11-openui-minutes.html](https://www.w3.org/2024/04/11-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Should we support other forms of link elements? ([openui/open-ui#1032](https://github.com/openui/open-ui/issues/1032))

While prototyping interest invokers, lukew found the HTML `<a>` element was handled but SVG's `<a>`
was not, and saw no reason not to support it (and possibly MathML links). The minutes record [masonf](../../people/mfreed7.md)
as agreeing the feature should target *links* rather than particular elements, [scotto](../../people/scottaohara.md) as asking
whether every markup spec that repeats HTML's link concept would need updating, and [bkardell](../../people/bkardell.md) as
recounting MathML's history of allowing `href` everywhere — an approach implementers rejected —
while supporting lukew's proposal. [keithamus](../../people/keithamus.md) floated interactive elements in general; the group
deferred inputs/selects.

> RESOLVED: Support interest invokers on link like elements, specifically SVGAElement.

([resolution](https://github.com/openui/open-ui/issues/1032#issuecomment-2050257941))

## Other topics

- [openui/open-ui#872](https://github.com/openui/open-ui/issues/872) — behaviour when
  `interesttarget` and `invoketarget` point to the same element
  ([resolution](https://github.com/openui/open-ui/issues/872#issuecomment-2050326847)):

> RESOLVED: Don't do anything special in this case.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
