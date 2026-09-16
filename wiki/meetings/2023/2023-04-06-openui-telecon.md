---
date: 2023-04-06
group: openui
type: telecon
topics_count: 2
issues: [565, 621]
generated_by: llm
---

# Open UI CG telecon — 2023-04-06

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/04/06-openui-minutes.html](https://www.w3.org/2023/04/06-openui-minutes.html) (dated-URL convention for CG minutes).

## [selectmenu] Accept "option" elements through multiple slots ([openui/open-ui#565](https://github.com/openui/open-ui/issues/565))

Returning from [the 2023-03-30 discussion](2023-03-30-openui-telecon.md) on `<selectmenu>` — the
precursor of the customizable `<select>` (see
[customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
demonstrating nested slotting (a selectmenu inside the author's own shadow root, with options
slotted through) and [dandclark](../../people/dandclark.md) as reframing the previously "scary" case: selectmenu already does
a flat-tree walk to hook up its parts, so slotted options fall out naturally — the Chromium
failure was a performance-optimization bug, not a design gap, and [jarhar](../../people/josepharhar.md) had a CL to fix it.
[xiaochengh](../../people/xiaochengh.md) asked about future-proofing with boundary elements; [dandclark](../../people/dandclark.md) recalled the Chromium
implementation stops at a nested selectmenu so it does not reach into it.

> RESOLVED: Support nested slotting of option elements. Selectmenu should look at the flat tree for its parts. For corner cases such as encountering another selectmenu in the flat tree, skip over it and don't look into it for more parts.

([resolution](https://github.com/openui/open-ui/issues/565#issuecomment-1499241647))

## Other topics

- [openui/open-ui#621](https://github.com/openui/open-ui/issues/621) — process discussion on adding a "don't make it worse" decision principle.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
