---
date: 2022-08-04
group: openui
type: telecon
topics_count: 2
issues: [529, 540]
generated_by: llm
---

# Open UI CG telecon — 2022-08-04

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-08-04](https://www.w3.org/2022/08/04-openui-minutes.html).

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

The longest round of the debate, with both sides fully argued. The minutes record [flackr](../../people/flackr.md),
[masonf](../../people/mfreed7.md), una, [gregwhitworth](../../people/gregwhitworth.md) and vicgutt against restrictions: developers will do this anyway,
restrictions push them back to inaccessible divs or frameworks, and painting the platform into a
corner prevents making these patterns accessible later. The minutes record [sarah_h](../../people/smhigley.md) and hdv (and
partially [scotto](../../people/scottaohara.md)) on the other side: developers more likely reach for off-the-shelf components
than raw divs, screen readers are bound by what ARIA can express, a control that allows too much
becomes unteachable, and specific slots (before/after the options) would cover the real use
cases. The minutes record [scotto](../../people/scottaohara.md) pressing the concrete question of how keyboard users would even
reach a button between options, and una reframing it as a teaching problem for dev tools and
documentation rather than platform limits. Discussion moved to GitHub; no resolution was
recorded this day (the straw poll came a week later). Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/540#issuecomment-1205649153))

## Other topics

- [openui/open-ui#529](https://github.com/openui/open-ui/issues/529) — resolved that light dismiss happens on `mouseup`, and not if the `mousedown` happened within the pop-up (to allow text selection) ([resolution](https://github.com/openui/open-ui/issues/529#issuecomment-1205605282)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
