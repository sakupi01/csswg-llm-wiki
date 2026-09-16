---
date: 2024-10-10
group: openui
type: telecon
topics_count: 2
issues: [1098, 1104]
generated_by: llm
---

# Open UI CG telecon — 2024-10-10

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/10/10-openui-minutes.html](https://www.w3.org/2024/10/10-openui-minutes.html)
(dated-URL convention for CG minutes).

## [switch]: Does the "on" position change between rtl and ltr? ([openui/open-ui#1098](https://github.com/openui/open-ui/issues/1098))

[gregwhitworth](../../people/gregwhitworth.md) asked whether the switch's on/off thumb position should flip with text direction,
noting i18n-tracker input. The minutes record naman as citing iOS and Android documentation and
Arabic-locale videos showing switches (and sliders) do flip with RTL — "everything flips other than
scrollbars" — and [masonf](../../people/mfreed7.md) as raising vertical writing modes, where whether "more" means up or down
proved genuinely contested and possibly cultural; naman added that even physical switch conventions
are geographical (up is on in the US, down in India). Vertical modes were split into a new issue.

> RESOLVED: RTL and LTR should be supported that the thumb adjusts position. Open a new issue to discuss vertical writing modes

([resolution](https://github.com/openui/open-ui/issues/1098#issuecomment-2405817099))

## Other topics

- [openui/open-ui#1104](https://github.com/openui/open-ui/issues/1104) — link delegation to a
  descendant ([resolution](https://github.com/openui/open-ui/issues/1104#issuecomment-2405777834)):

> RESOLVED: Incubate an explainer for a new solution for declarative link delegation

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
