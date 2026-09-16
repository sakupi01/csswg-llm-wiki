---
date: 2025-06-05
group: openui
type: telecon
topics_count: 4
issues: [1205, 1217, 1225, 1226]
generated_by: llm
---

# Open UI CG telecon — 2025-06-05

Four topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/06/05-openui-minutes.html](https://www.w3.org/2025/06/05-openui-minutes.html) (dated-URL convention for CG minutes).

## Should select multiple with popup have OK/Cancel buttons? ([openui/open-ui#1217](https://github.com/openui/open-ui/issues/1217))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). The minutes record [jarhar](../../people/josepharhar.md) as
laying out three options for the multi-select popup: OK/Cancel buttons (Android-style, but light
dismiss silently cancelling changes is a known annoyance), a lone Cancel button (iOS-style), or
no buttons at all. [masonf](../../people/mfreed7.md) argued against buttons, drawing the analogy to `closedby` on dialogs —
users already expect light dismiss to work; scott and sarah pushed back from the accessibility
and mobile side: ARIA today forbids buttons inside a listbox (making any button design push the
ARIA spec toward dialog semantics), and on mobile a picker without a close affordance is hard to
escape. [jarhar](../../people/josepharhar.md) noted iOS's native multi-select commits immediately and light dismiss keeps the
selection. The group settled on a single commit-and-close button, with light dismiss also
committing.

> RESOLVED: choose option 2 for now, where there is one button which commits the options and closes the picker. light dismiss will also commits the options and close the picker.

([resolution](https://github.com/openui/open-ui/issues/1217#issuecomment-2946116847))

## Other topics

- [openui/open-ui#1205](https://github.com/openui/open-ui/issues/1205) — [menu] Define a default checked attribute for menuitem; resolved on a `defaultchecked` content attribute plus a `checked` IDL-only attribute ([resolution](https://github.com/openui/open-ui/issues/1205#issuecomment-2945557882)).
- [openui/open-ui#1225](https://github.com/openui/open-ui/issues/1225) — Keyboard shortcuts for menuitems and buttons; resolved to note it as a future enhancement, out of scope for the current design ([resolution](https://github.com/openui/open-ui/issues/1225#issuecomment-2945575484)).
- [openui/open-ui#1226](https://github.com/openui/open-ui/issues/1226) — [menu] Should menulist be a popover by default?; resolved not to require the popover attribute on menulist ([resolution](https://github.com/openui/open-ui/issues/1226#issuecomment-2945628277)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
