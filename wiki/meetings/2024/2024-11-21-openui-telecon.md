---
date: 2024-11-21
group: openui
type: telecon
topics_count: 1
issues: [1117]
generated_by: llm
---

# Open UI CG telecon — 2024-11-21

One topic, one resolution. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2024/11/21-openui-minutes.html](https://www.w3.org/2024/11/21-openui-minutes.html)
(dated-URL convention for CG minutes).

## select: clarifying what should be used as the chosen value ([openui/open-ui#1117](https://github.com/openui/open-ui/issues/1117))

Resolving the accessible-value question left open on
[2024-10-31](2024-10-31-openui-telecon.md) for [customizable
select](../../features/customizable-select.md). The minutes record [scottohara](../../people/scottaohara.md) as presenting a
three-step algorithm worked out with Aaron and Sarah: (1) if `aria-valuetext` is present on the
select, use it (empty string included); (2) else if there is a button part, compute the value from
its contents; (3) else compute it from the selected option's name. [masonf](../../people/mfreed7.md) noted it mirrors what
sighted users see and applies to the accessibility value, not the IDL value; sarah and [scottohara](../../people/scottaohara.md)
supplied the empty-button use cases (multi-select tags rendered outside the button, Microsoft
patterns where the invoking button has no visible text); ARIA attributes on the button part and
`<selectedcontent>` are ignored since those nodes are absent from the accessibility tree.

> RESOLVED: adopt the behavior described in https://github.com/openui/open-ui/issues/1117#issuecomment-2492045184

([resolution](https://github.com/openui/open-ui/issues/1117#issuecomment-2492081152))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
