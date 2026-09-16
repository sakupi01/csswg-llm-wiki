---
date: 2025-05-22
group: openui
type: telecon
topics_count: 2
issues: [1197, 1220]
generated_by: llm
---

# Open UI CG telecon — 2025-05-22

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/05/22-openui-minutes.html](https://www.w3.org/2025/05/22-openui-minutes.html) (dated-URL convention for CG minutes).

## [Range] Update names and anatomy based on CSSWG decision ([openui/open-ui#1197](https://github.com/openui/open-ui/issues/1197))

The CSSWG's css-forms draft names the `<input type=range>` pseudo-elements `::slider-*`, so the
enhanced-range explainer's naming should follow. The minutes record [lwarlow](../../people/lukewarlow.md) as voting to rename
everything to "slider" (matching the ARIA role, and noting the same parts serve range, meter,
progress and switch), and expecting Open UI's ticks work to migrate into CSS Forms once specced;
[gregwhitworth](../../people/gregwhitworth.md) agreed, citing real-world radial slider/meter use cases; [brecht_dr](../../people/brechtDR.md) asked for help
restructuring the anatomy documentation.

> RESOLVED: Rename every instance of range to slider following the new forms draft by the CSSWG

([resolution](https://github.com/openui/open-ui/issues/1197#issuecomment-2902148878))

## Other topics

- [openui/open-ui#1220](https://github.com/openui/open-ui/issues/1220) — [command invokers] scroll command.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
