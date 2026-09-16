---
date: 2025-09-11
group: openui
type: telecon
topics_count: 3
issues: [1243, 1244, 1265]
generated_by: llm
---

# Open UI CG telecon — 2025-09-11

Three topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/09/11-openui-minutes.html](https://www.w3.org/2025/09/11-openui-minutes.html) (dated-URL convention for CG minutes).

## [Range] Explainer example issue? + question ([openui/open-ui#1243](https://github.com/openui/open-ui/issues/1243))

A typo in the enhanced-range explainer surfaced the question of conflicting `min`/`max` between
a rangegroup and its inner inputs. The minutes record [brecht_dr](../../people/brechtDR.md) as laying out three options
(no group-level min/max; ignore inner min/max; or render the group's larger track while clamping
the thumb); [lwarlow](../../people/lukewarlow.md) offered a livestream video-seek use case for a track wider than the thumb's
allowed range; una argued the parent should be allowed wider bounds than the children but a
child exceeding the parent should be cut off, which [lwarlow](../../people/lukewarlow.md) agreed with. [bkardell](../../people/bkardell.md) and [sorvell](../../people/sorvell.md)
pressed for surveying real-world multi-slider implementations before deciding. No resolution was
recorded.

## [Range] What is the label? ([openui/open-ui#1244](https://github.com/openui/open-ui/issues/1244))

How to label a rangegroup and its thumbs accessibly. The minutes record [brecht_dr](../../people/brechtDR.md) as endorsing
scott's labeling idea from the issue and demoing a proof of concept; [lwarlow](../../people/lukewarlow.md) liked it (a legend
matches fieldset, labels match other form controls) but noted the legend-vs-label question has
focus/click-behaviour implications, which [sorvell](../../people/sorvell.md) also raised; sarah cautioned that a fully
invisible default label would be unprecedented; [bkardell](../../people/bkardell.md) asked for the progressive-enhancement
story to be addressed explicitly in the explainer, and [keithamus](../../people/keithamus.md) warned against over-indexing on
no-JS progressive enhancement.

> RESOLVED: Update the explainer with the idea by scott for labeling, update the part on progressive enhancement with clear directions on where we want to go

([resolution](https://github.com/openui/open-ui/issues/1244#issuecomment-3282190667))

## Other topics

- [openui/open-ui#1265](https://github.com/openui/open-ui/issues/1265) — Open a11y questions for overflow/carousels.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
