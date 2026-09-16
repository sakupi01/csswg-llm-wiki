---
date: 2025-12-11
group: openui
type: telecon
topics_count: 3
issues: [1337, 1338, 1339]
generated_by: llm
---

# Open UI CG telecon — 2025-12-11

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/12/11-openui-minutes.html](https://www.w3.org/2025/12/11-openui-minutes.html) (dated-URL convention for CG minutes).

## [Range] Standardize visual and audio feedback for constrained handle movement. ([openui/open-ui#1339](https://github.com/openui/open-ui/issues/1339))

How assistive technology should convey that a thumb is blocked by another thumb or a
`stepbetween` constraint. The minutes record [masonf](../../people/mfreed7.md) as suggesting studying native two-handle
sliders and expecting a new property for the announcement; [keithamus](../../people/keithamus.md) flipped the question —
should handles push or swap instead of blocking? — which [brecht_dr](../../people/brechtDR.md) resisted because crossing
thumbs breaks min/max labeling; sarah argued screen-reader users already learn the current
min/max of the focused handle and warned against announcing too much, suggesting screen-reader
vendors be consulted.

> RESOLVED: Look for a way to make the rangegroup pronounce its current min and max values, as well as stepbetween when entering the rangegroup (first thumb), then each thumb will pronounce its individual min and max and current value

([resolution](https://github.com/openui/open-ui/issues/1339#issuecomment-3643442599))

## [Range] Clarifying the propagation of the disabled attribute ([openui/open-ui#1338](https://github.com/openui/open-ui/issues/1338))

The minutes record [keithamus](../../people/keithamus.md) as finding it straightforward that a disabled thumb skips focus and
activation while remaining programmatically settable, and that disabled on the rangegroup should
propagate to all handles; [masonf](../../people/mfreed7.md) added that an individually disabled handle should stay locked in
place with no nudging; [brecht_dr](../../people/brechtDR.md) raised the progressive-enhancement question of whether all
thumbs disabled equals a disabled group (affecting track painting and tab stops).

> RESOLVED: A disabled state on the rangegroup should make it completely disabled, a thumb can be individually disabled, but when all thumbs are disabled, it should behave like a fully disabled group

([resolution](https://github.com/openui/open-ui/issues/1338#issuecomment-3643489654))

## [Range] Multi-handle necessity and scalability guidelines (3+ Thumbs) ([openui/open-ui#1337](https://github.com/openui/open-ui/issues/1337))

Whether the API should target two thumbs or n thumbs. The minutes record [masonf](../../people/mfreed7.md) as wanting data —
if 3+ handles is under ~5% of use, a simple attribute on the existing range input would beat a
container API — and arguing it should be either a two-thumb attribute or genuinely infinite;
[keithamus](../../people/keithamus.md) saw no big barrier to supporting three and wanted the design kept open to future
capabilities; [brecht_dr](../../people/brechtDR.md) reported an informal poll where nobody opposed 3 handles and noted the
container design already solves the min/max thumb-labeling problem an attribute would create.

> RESOLVED: Try to find more examples of more than two thumbs. A two-thumb api could be an attribute, while an n-thumb api could look like the current example. Gather feedback based on usages or lack of usages due to a reason (not able, no design library that supports it, etc...)

([resolution](https://github.com/openui/open-ui/issues/1337#issuecomment-3643842135))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
