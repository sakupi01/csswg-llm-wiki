---
date: 2025-02-06
group: openui
type: telecon
topics_count: 4
issues: [700, 1058, 1068, 1069]
generated_by: llm
---

# Open UI CG telecon — 2025-02-06

Four topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/02/06-openui-minutes.html](https://www.w3.org/2025/02/06-openui-minutes.html) (dated-URL convention for CG minutes).

## Consider "toggle" (expand/collapse) attribute ([openui/open-ui#700](https://github.com/openui/open-ui/issues/700))

Follow-up to the January discussion of the `openable` attribute. The minutes record [lwarlow](../../people/lukewarlow.md) as
summarising the motivation — `<details>` has improved but still doesn't cover expand/collapse
patterns like app panels, expandable table rows, or hamburger menus — and asking the group for
interest to incubate. [masonf](../../people/mfreed7.md) noted Chromium is actively improving `<details>` (including its
accessibility issues); [brecht_dr](../../people/brechtDR.md) and scott raised responsive-disclosure use cases where the
trigger and the panel are not adjacent in the DOM, which `<details>` cannot express. The group
agreed to incubate.

> RESOLVED: incubate the openable attribute in OpenUI.

([resolution](https://github.com/openui/open-ui/issues/700#issuecomment-2640877326))

## Other topics

- [openui/open-ui#1058](https://github.com/openui/open-ui/issues/1058) — Press Button Proposal; the group resolved it is open to incubating the proposal ([resolution](https://github.com/openui/open-ui/issues/1058#issuecomment-2640853893)).
- [openui/open-ui#1068](https://github.com/openui/open-ui/issues/1068) — [invokers] add a way to list supported commands?; deemed useful but not essential for v1, to be taken back to the TAG ([resolution](https://github.com/openui/open-ui/issues/1068#issuecomment-2640802623)).
- [openui/open-ui#1069](https://github.com/openui/open-ui/issues/1069) — [invokers] add an invoke method?; the group doesn't think it is needed and will justify that to the TAG ([resolution](https://github.com/openui/open-ui/issues/1069#issuecomment-2640773344)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
