---
date: 2025-05-01
group: openui
type: telecon
topics_count: 3
issues: [1183, 1184, 1186]
generated_by: llm
---

# Open UI CG telecon — 2025-05-01

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/05/01-openui-minutes.html](https://www.w3.org/2025/05/01-openui-minutes.html) (dated-URL convention for CG minutes).

## [Range] Progressive enhancement as rule of thumb? ([openui/open-ui#1186](https://github.com/openui/open-ui/issues/1186))

Whether the enhanced range slider should extend `<input type=range>` (a `handles` attribute) or
be something new. The minutes record [masonf](../../people/mfreed7.md) as doubting an attribute could be progressively
enhanceable and liking a new element, while warning standards bodies resist elements duplicating
existing ones; [sorvell](../../people/sorvell.md) and [bkardell](../../people/bkardell.md) argued a multi-thumb slider is genuinely its own thing (curve
controls, gradient stops). The discussion converged on a wrapper element grouping multiple
`<input type=range>` children — polyfillable, with each input keeping its own value.
scott-o-bother floated `<fieldset>` as the wrapper; [keithamus](../../people/keithamus.md) pushed back, preferring a dedicated
wrapping element over overloading fieldset.

> RESOLVED: Go further with an idea where multiple input type="range" are wrapped inside of a wrapper element. Which wrapper to be further investigated

([resolution](https://github.com/openui/open-ui/issues/1186#issuecomment-2845430479))

## [Range] Handle count and maximum limitations? ([openui/open-ui#1183](https://github.com/openui/open-ui/issues/1183))

Two handles or n handles, and should there be a cap? The minutes record [sorvell](../../people/sorvell.md) as favouring
multi-handle support (price ranges dominate, but more exist) while noting nearly all in-the-wild
implementations are fully custom; [keithamus](../../people/keithamus.md) raised exclusive vs. overlapping ranges (price ranges
vs. gradient colour stops) as a looming can of worms; scott-o-bother flagged accessibility
questions — exposing the in-between value, whether the UA renders one track, and keyboard
patterns for many thumbs. The group agreed the maximum is the author's responsibility.

> RESOLVED: Go for multi-handles because of the use-case. The maximum is author's choice. Create a separate issue for the potential accessibility problems such as tabbing through a huge amount of thumbs

([resolution](https://github.com/openui/open-ui/issues/1183#issuecomment-2845497528))

## [Range] Thumb collision handling ([openui/open-ui#1184](https://github.com/openui/open-ui/issues/1184))

Short discussion on whether thumbs may overlap. The minutes record [keithamus](../../people/keithamus.md) as suggesting
per-range `min`/`max` to prevent overlap, with overlap allowed by leaving them off; [sorvell](../../people/sorvell.md)
countered that forbidding overlap is impractical and that overlap handling (which thumb moves)
is exactly where custom implementations get gnarly, so the group must get it right. [masonf](../../people/mfreed7.md)
suggested allowing everything for v1 and refining later. No resolution was recorded.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
