---
date: 2024-05-09
group: openui
type: telecon
topics_count: 2
issues: [863, 1026]
generated_by: llm
---

# Open UI CG telecon — 2024-05-09

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/05/09-openui-minutes.html](https://www.w3.org/2024/05/09-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] - Ensure any new UA defaults meet WCAG 2.2 target size (minimum) ([openui/open-ui#1026](https://github.com/openui/open-ui/issues/1026))

Following the [2024-04-04](2024-04-04-openui-telecon.md) resolution, [jarhar](../../people/josepharhar.md) surveyed CSS mechanisms
for giving [customizable select](../../features/customizable-select.md) options a 24px minimum: a
min size alone misaligns the text, flex containers might have side effects. The minutes record Luke
as suggesting the alignment properties that now apply to block layout, [flackr](../../people/flackr.md) as liking that,
and [dbaron](../../people/dbaron.md) as walking the compatibility risks of each option (author resets like
`option { display: block }` would silently break a flex-based default; `line-height` risks overlap)
and as correcting mid-call that Chromium had in fact shipped alignment properties on
`display: block`. sanketj_ asked whether other implementers would follow.

> RESOLVED: use align-content with display:block and min-size properties to ensure minimum size for options

([resolution](https://github.com/openui/open-ui/issues/1026#issuecomment-2103187647))

## selectlist: Should the "checked" option have a checkmark next to it? ([openui/open-ui#863](https://github.com/openui/open-ui/issues/863))

The default-checkmark debate for [customizable select](../../features/customizable-select.md).
[jarhar](../../people/josepharhar.md) noted the accessibility push for a non-color selected indicator. The minutes record una as
arguing against a UA default — only ~20% of surveyed selects use checkmarks, icons are branded, and
authors would have to undo both the icon and its spacing — with sanketj_ agreeing; [masonf](../../people/mfreed7.md) and
[scotto](../../people/scottaohara.md) argued the accessible thing should be the default ([scotto](../../people/scottaohara.md) adding it survives author
mistakes and high-contrast mode), and Luke favored a default checkmark via `content` in a form
screen readers do not announce. No resolution was recorded; the topic returned on
[2024-05-23](2024-05-23-openui-telecon.md).

([bot comment](https://github.com/openui/open-ui/issues/863#issuecomment-2103244160))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
