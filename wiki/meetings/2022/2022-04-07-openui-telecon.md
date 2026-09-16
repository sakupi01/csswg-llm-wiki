---
date: 2022-04-07
group: openui
type: telecon
topics_count: 6
issues: [480, 483, 486, 491, 500, 508]
generated_by: llm
---

# Open UI CG telecon — 2022-04-07

Six topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-04-07](https://www.w3.org/2022/04/07-openui-minutes.html).

## `<selectmenu>` always snaps shut when opened with mouse ([openui/open-ui#483](https://github.com/openui/open-ui/issues/483))

The minutes record [dandclark](../../people/dandclark.md) describing the bug report: a `<selectmenu>` inside a `<form>`
contained a `<button>`, whose default behavior submitted the form and navigated the page. He
suggested exempting elements inside a `<selectmenu>` from automatic form association, while
still allowing explicit association. The minutes record [masonf](../../people/mfreed7.md) cringing at a flat-tree walk in
the parser and suggesting the parser instead force `type=button`; [JonathanNeal](../../people/jonathanneal.md) asked which
option would be most backwards compatible and compared the slotting behavior to
details/summary; una is recorded as hoping `button` vs `type=button` would not become the
differentiator. [dandclark](../../people/dandclark.md) took an action to research the parser's form-association complexity.
No resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/483#issuecomment-1092172842))

## [selectmenu] button click behavior when the popup is open ([openui/open-ui#486](https://github.com/openui/open-ui/issues/486))

The minutes record [dandclark](../../people/dandclark.md) stating the desired behavior: when the popup is open and the user
clicks the button, the popup should close and stay closed, avoiding a close-then-reopen cycle —
event order matters. The minutes record [masonf](../../people/mfreed7.md) agreeing the behavior should be a toggle and
noting the spec will need to define the button click as a light-dismiss trigger. No resolution
was recorded. Part of the [customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/486#issuecomment-1092084600))

## Other topics

- [openui/open-ui#480](https://github.com/openui/open-ui/issues/480) — resolved to bring the focusgroup work under the Open UI umbrella ([resolution](https://github.com/openui/open-ui/issues/480#issuecomment-1092082620)).
- [openui/open-ui#491](https://github.com/openui/open-ui/issues/491) — resolved to keep the `popup` attribute and bikeshed a replacement for the `popup` *value* ([resolution](https://github.com/openui/open-ui/issues/491#issuecomment-1092063546)).
- [openui/open-ui#508](https://github.com/openui/open-ui/issues/508) — resolved to rename `triggerpopup` to `togglepopup` and keep discussing only-open/only-close variants ([resolution](https://github.com/openui/open-ui/issues/508#issuecomment-1092081568)).
- [openui/open-ui#500](https://github.com/openui/open-ui/issues/500) — renaming `initiallyopen`, discussed without resolution this day.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
