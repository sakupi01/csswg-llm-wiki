---
date: 2023-11-30
group: openui
type: telecon
topics_count: 3
issues: [900, 952, 959]
generated_by: llm
---

# Open UI CG telecon — 2023-11-30

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/11/30-openui-minutes.html](https://www.w3.org/2023/11/30-openui-minutes.html) (dated-URL convention for CG minutes).

## [switch]: Should author defined content be allowed on tracks or thumb? ([openui/open-ui#959](https://github.com/openui/open-ui/issues/959))

The minutes record Philipp_Gfeller as reporting his design-system analysis (about 30% put content
on the track, 20% on the thumb — usually a checkmark, Ant Design even text) and asking whether
the `<switch>` element should allow it. scotto_ led the skeptical camp: track text almost always
just repeats the accessible state, must not enter the switch's name computation, and arbitrary
content today has no accessible exposure — he challenged anyone to show an accessible example,
with bkardell_ backing him via the generated-content cautionary tale. una argued track text is
not a best practice and should not be MVP scope; Luke agreed for tracks but saw thumb use cases
(OS "prefer shapes" settings). [gregwhitworth](../../people/gregwhitworth.md) pushed back against outright prohibition —
aesthetics, ripple effects, slider-thumb tooltips — suggesting console warnings or an element
subset, and noting the tension between accessible-by-default and extensibility; [keithamus](../../people/keithamus.md) cited
GitHub Primer's stylised I/O symbols in the track as a real design-system need. [dbaron](../../people/dbaron.md) noted
users often cannot tell whether a switch label describes the current state or the result of
pressing. Philipp_Gfeller was asked to split the issue into separate track and thumb issues.
No resolution was recorded on this issue.

## Other topics

- [openui/open-ui#952](https://github.com/openui/open-ui/issues/952) — resolved invokers v1 covers popover and dialog invoking, with the copy action pursued later ([resolutions](https://github.com/openui/open-ui/issues/952#issuecomment-1834461595)).
- [openui/open-ui#900](https://github.com/openui/open-ui/issues/900) — resolved custom invoker actions must contain a hyphen; unrecognised non-custom actions fire no event ([resolution](https://github.com/openui/open-ui/issues/900#issuecomment-1834448462)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
