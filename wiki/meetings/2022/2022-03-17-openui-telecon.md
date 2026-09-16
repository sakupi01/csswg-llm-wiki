---
date: 2022-03-17
group: openui
type: telecon
topics_count: 3
issues: [415, 476, 489]
generated_by: llm
---

# Open UI CG telecon — 2022-03-17

Three topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-03-17](https://www.w3.org/2022/03/17-openui-minutes.html).

## [select] mult-select variation doesn't allow for keyboard access ([openui/open-ui#476](https://github.com/openui/open-ui/issues/476))

The minutes record [dandclark](../../people/dandclark.md) proposing that the button part of a custom select built from divs
get an implicit `tabindex` of 0, so authors don't have to add it themselves. The minutes record
[scotto](../../people/scottaohara.md) asking whether that element would always be exposed as a combobox role, and [sarah_higley](../../people/smhigley.md)
warning from her own combobox work that slotting arbitrary content (focusable items, labels)
into such controls "messes up so much" — guards are needed on what content is allowed. [tantek](../../people/tantek.md)
and [JonathanNeal](../../people/jonathanneal.md) raised the CSSWG's earlier spatial/sequential navigation proposals
([w3c/csswg-drafts#3377](https://github.com/w3c/csswg-drafts/issues/3377)) as a possible broader
fix for tabindex's problems. No resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/476#issuecomment-1071502619))

## Other topics

- [openui/open-ui#415](https://github.com/openui/open-ui/issues/415) — whether `blur()` should be a light dismiss trigger for popups.
- [openui/open-ui#489](https://github.com/openui/open-ui/issues/489) — Panelset/Spicy-Sections issues review.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
