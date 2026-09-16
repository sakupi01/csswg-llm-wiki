---
date: 2025-05-15
group: openui
type: telecon
topics_count: 3
issues: [1102, 1185, 1220]
generated_by: llm
---

# Open UI CG telecon — 2025-05-15

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/05/15-openui-minutes.html](https://www.w3.org/2025/05/15-openui-minutes.html) (dated-URL convention for CG minutes).

## Does `<select multiple>` need a button and popup by default? ([openui/open-ui#1102](https://github.com/openui/open-ui/issues/1102))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). The minutes record [jarhar](../../people/josepharhar.md) as
proposing that `<select multiple>` support a button-plus-popup rendering (in addition to the
in-page listbox) while explicitly excluding text inputs and nested interactive content from the
button, keeping it simple. [sorvell](../../people/sorvell.md) asked whether "chips"-style multi-select patterns (e.g.
GitHub's labels dropdown) could be built on it; scott called chips a poor pattern and endorsed
shipping a basic baseline, deferring the complex responsive cases to a later version or to the
combobox work. [brecht_dr](../../people/brechtDR.md) reported prototyping it and being in favour.

> RESOLVED: Select multiple should support rendering with a button and popup in addition to being rendered as an in-page listbox. The button should not be a text input and should not have nested buttons or other interactive content, just like a single select. Controlling which mode is used should be figured out separately.

([resolution](https://github.com/openui/open-ui/issues/1102#issuecomment-2884760537))

## [Range] Keyboard navigation for multi-handle ranges ([openui/open-ui#1185](https://github.com/openui/open-ui/issues/1185))

How keyboards move between and move the thumbs. The minutes record [brecht_dr](../../people/brechtDR.md) as presenting the
common pattern (Tab between thumbs, arrows to slide, sometimes PageUp/PageDown for larger jumps);
scott suggested resolving on Tab unless community feedback demands better, while noting ten tab
stops for one control is unappealing; [sorvell](../../people/sorvell.md) reported Material, Angular and Zillow all give each
thumb a tab stop; [flackr](../../people/flackr.md) raised whether AT group-entry concepts and home/end semantics apply, and
supported keeping the existing single-range key behaviour.

> RESOLVED: Each tab stop goes on a thumb, keep current behavior as it is on the current input range for pagedown, -up, home, end.

([resolution](https://github.com/openui/open-ui/issues/1185#issuecomment-2884720589))

## Other topics

- [openui/open-ui#1220](https://github.com/openui/open-ui/issues/1220) — [command invokers] scroll command.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
