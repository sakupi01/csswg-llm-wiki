---
date: 2024-02-08
group: openui
type: telecon
topics_count: 3
issues: [532, 978, 979]
generated_by: llm
---

# Open UI CG telecon — 2024-02-08

Three topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/02/08-openui-minutes.html](https://www.w3.org/2024/02/08-openui-minutes.html)
(dated-URL convention for CG minutes).

## [switch]: Should author defined content be allowed on the thumb? ([openui/open-ui#979](https://github.com/openui/open-ui/issues/979))

philipp asked whether author content should be allowed on the switch thumb. The minutes record
[gregwhitworth](../../people/gregwhitworth.md) as noting Safari's beta only allows content via `::before`/`::after` pseudos and
arguing authors will want more than Unicode characters; [scotto](../../people/scottaohara.md) cautioned that allowing one thing
tends to end in allowing everything, and [keithamus](../../people/keithamus.md) preferred not to entangle switch with anchor
positioning. philipp reported the researched use cases were simple (a checkmark on the thumb,
"on"/"off" text on the track), and the group limited author content to images/SVG. The bot recorded
the resolution with the "PROPOSED RESOLUTION" prefix accidentally left in.

> RESOLVED: PROPOSED RESOLUTION: allow img/svg content (excluding <foreignObject>) within the thumb of the switch

([resolution](https://github.com/openui/open-ui/issues/979#issuecomment-1934797009))

## [switch]: Should author defined content be allowed on the track? ([openui/open-ui#978](https://github.com/openui/open-ui/issues/978))

The bot logged this as a separate topic, but its IRC log contains only a single "+1" — the
substantive discussion of track content happened inside the
[openui/open-ui#979](https://github.com/openui/open-ui/issues/979) discussion above. No resolution
was recorded.

([bot comment](https://github.com/openui/open-ui/issues/978#issuecomment-1934797685))

## Other topics

- [openui/open-ui#532](https://github.com/openui/open-ui/issues/532) — bikeshedding
  `popover=hint`, discussed without a recorded resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
