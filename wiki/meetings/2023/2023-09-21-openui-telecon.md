---
date: 2023-09-21
group: openui
type: telecon
topics_count: 3
issues: [834, 838, 839]
generated_by: llm
---

# Open UI CG telecon — 2023-09-21

Three topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/09/21-openui-minutes.html](https://www.w3.org/2023/09/21-openui-minutes.html) (dated-URL convention for CG minutes).

## [popover] Can we add focus-triggering to form elements? ([openui/open-ui#838](https://github.com/openui/open-ui/issues/838))

[brecht_dr](../../people/brechtDR.md)'s proposal: let form fields trigger popovers on focus — e.g. a password field showing
password rules — possibly focus-only, without hover. The minutes record [keithamus](../../people/keithamus.md) as cautioning
against reintroducing fixed input modalities: `interesttarget` deliberately abstracts them away,
and future devices (Apple Vision came up at TPAC) make per-modality APIs fragile — a point
[gregwhitworth](../../people/gregwhitworth.md) pushed back on as a discussion-derailing argument. [scotto](../../people/scottaohara.md) supported genuine
focus-without-hover cases (a password-strength popover should not appear while mousing across a
form; hover popups are troublesome for users with motor impairments) but warned against
shoehorning popover/interesttarget primitives into everything. [zcorpan](../../people/zcorpan.md) raised a screen-reader
hazard: dismissing on blur could strand forms-mode users with no way to reach the popover;
[scotto](../../people/scottaohara.md) detailed the "details relationship" plumbing that lets AT users enter a popover. Luke
noted focus already implies an action on mobile pickers, so what "counts as interest" must be
platform-aware. The group agreed to keep investigating on GitHub. No resolution was recorded.

## Other topics

- [openui/open-ui#834](https://github.com/openui/open-ui/issues/834) — bikeshedding a name for "light dismiss for dialog", discussed without resolution.
- [openui/open-ui#839](https://github.com/openui/open-ui/issues/839) — extending `interesttarget` to more elements, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
