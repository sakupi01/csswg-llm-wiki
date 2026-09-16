---
date: 2025-11-06
group: openui
type: telecon
topics_count: 4
issues: [931, 1317, 1321, 1322]
generated_by: llm
---

# Open UI CG telecon — 2025-11-06

Four topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/11/06-openui-minutes.html](https://www.w3.org/2025/11/06-openui-minutes.html) (dated-URL convention for CG minutes).

## Combobox search attribute and its values ([openui/open-ui#931](https://github.com/openui/open-ui/issues/931))

Related to the customizable `<select>` family of form-control work — see
[customizable select](../../features/customizable-select.md). Deep-dive on the `beforefilter`
event API for custom filtering. The minutes record [jarhar](../../people/josepharhar.md) as presenting two designs — the author
hands the browser a promise, or the author self-debounces with their own AbortController — and
preferring the latter; [keithamus](../../people/keithamus.md) agreed debouncing belongs in userland (citing GitHub's finely
tuned throttling) and disliked promise-assignment as guaranteed-async and confusing next to
event semantics, proposing instead a filter API on the element itself usable outside the event.
[masonf](../../people/mfreed7.md) worried a DIY design is a footgun for one-off developers who would refetch on every
keystroke, and floated a `filteredOptions` promise setter; [jarhar](../../people/josepharhar.md) countered that providing an
AbortController on the event saves only a line or two. The trade-off between browser-managed
safety and developer control was left open. No resolution was recorded.

## Other topics

- [openui/open-ui#1321](https://github.com/openui/open-ui/issues/1321) — What event should fire on checkable menu items?; resolved on a cancellable click, a synchronous checked event, then popover close and beforetoggle ([resolution](https://github.com/openui/open-ui/issues/1321#issuecomment-3499140509)).
- [openui/open-ui#1317](https://github.com/openui/open-ui/issues/1317) — [focusgroup] Add in sections detailing interactions with reading flow and aria-orientation.
- [openui/open-ui#1322](https://github.com/openui/open-ui/issues/1322) — [focusgroup] Add entry priority attribute; don't consider direction.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
