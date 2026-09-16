---
date: 2023-08-31
group: openui
type: telecon
topics_count: 3
issues: [758, 786, 802]
generated_by: llm
---

# Open UI CG telecon — 2023-08-31

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/08/31-openui-minutes.html](https://www.w3.org/2023/08/31-openui-minutes.html) (dated-URL convention for CG minutes).

## Errors for form related controls ([openui/open-ui#802](https://github.com/openui/open-ui/issues/802))

Raised by [gregwhitworth](../../people/gregwhitworth.md) before `<selectlist>` (see
[customizable select](../../features/customizable-select.md)) gets cemented: design systems
render validation errors inline as part of the control's anatomy, but browser validation bubbles
are native UI outside the renderer and unstylable. The minutes record [masonf](../../people/mfreed7.md) as firmly against
putting error UI in the selectlist anatomy — a WHATWG request to style validation bubbles exists
and should be solved independently. lukew observed error bubbles (like tooltips) are essentially
popovers, suggesting the invoker paradigm; [gregwhitworth](../../people/gregwhitworth.md) liked that framing but noted invokers
don't cover the on-submit moment, and got what he wanted: don't block selectlist, solve error
styling generally. [bkardell](../../people/bkardell.md) added the problem is broader than selectlist as a rule.

> RESOLVED: this is a good problem to solve, but it's independent of the <selectlist>. We should solve this generally.

([resolution](https://github.com/openui/open-ui/issues/802#issuecomment-1701581534))

## Other topics

- [openui/open-ui#758](https://github.com/openui/open-ui/issues/758) — agreed to review the design-systems page annually ([resolution](https://github.com/openui/open-ui/issues/758#issuecomment-1701570826)).
- [openui/open-ui#786](https://github.com/openui/open-ui/issues/786) — exclusive accordion exclusivity, discussed again without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
