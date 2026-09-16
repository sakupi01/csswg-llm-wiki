---
date: 2022-11-03
group: openui
type: telecon
topics_count: 1
issues: [571]
generated_by: llm
---

# Open UI CG telecon — 2022-11-03

One topic, no resolutions. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2022-11-03](https://www.w3.org/2022/11/03-openui-minutes.html).

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

Deep-dive on the four candidate solutions listed in the issue. The minutes record [masonf](../../people/mfreed7.md)
summarizing the consensus that rich option content usually differs from what belongs in the
button, and worrying that cloned HTML loses its styling once inside the shadow root; [flackr](../../people/flackr.md)
raising the CSS `element()` image function as a fifth option and noting imperative slotting
fails because the selected option must appear in two places at once ([dbaron](../../people/dbaron.md) agreed users expect
to see it in both the listbox and the button); [scotto](../../people/scottaohara.md) asking how CSS-based hiding behaves in
Reader Mode, and again proposing an author-supplied `<template>`; [sarah_h](../../people/smhigley.md) +1ing the template
route because rewriting styles breaks tooling with generated class names; and [jhey](../../people/jhey.md) pressing the
developer-experience angle — icon-font options make plain innerText visibly wrong, and framework
users need a declarative hook. The recorded sense of the room was that the feature is important
but needs more research; no resolution was recorded. The log also notes [flackr](../../people/flackr.md) volunteering to
open an issue on moving meetings off Zoom. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/571#issuecomment-1302542775))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
