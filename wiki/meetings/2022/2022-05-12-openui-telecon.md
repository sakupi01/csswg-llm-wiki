---
date: 2022-05-12
group: openui
type: telecon
topics_count: 3
issues: [525, 526, 528]
generated_by: llm
---

# Open UI CG telecon — 2022-05-12

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-05-12](https://www.w3.org/2022/05/12-openui-minutes.html).

## [selectmenu] Should we drop support for attachShadow? ([openui/open-ui#528](https://github.com/openui/open-ui/issues/528))

The minutes record [dandclark](../../people/dandclark.md) proposing a scope reduction: `attachShadow()` on `<selectmenu>`
turned out to be redundant with the existing customization mechanisms, appeared unused inside
and outside the group, and raised awkward spec questions (what happens to the old shadow root —
throw it away without a host, or keep it?). The minutes record [JonathanNeal](../../people/jonathanneal.md) agreeing while
asking how this stays consistent with other elements' `attachShadow()` behavior, and [masonf](../../people/mfreed7.md)
giving "essentially +1". Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: Proposed resolution: selectmenu will not support attachShadow().

([resolution](https://github.com/openui/open-ui/issues/528#issuecomment-1125286285))

## Other topics

- [openui/open-ui#525](https://github.com/openui/open-ui/issues/525) — resolved to accept the proposed interaction rules between `popup=popup`, `popup=hint`, and `popup=async` ([resolution](https://github.com/openui/open-ui/issues/525#issuecomment-1125293226)).
- [openui/open-ui#526](https://github.com/openui/open-ui/issues/526) — "interest"-based (hover) triggering for popovers, discussed without resolution this day.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
