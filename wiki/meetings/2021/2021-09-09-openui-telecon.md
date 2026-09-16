---
date: 2021-09-09
group: openui
type: telecon
topics_count: 2
issues: [386, 396]
generated_by: llm
---

# Open UI CG telecon — 2021-09-09

Two topics, no bot-recorded resolutions (the IRC log records two "Resolved" lines for
[openui/open-ui#386](https://github.com/openui/open-ui/issues/386) that the bot did not surface
as resolution bullets). Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2021-09-09](https://www.w3.org/2021/09/09-openui-minutes.html).

## [select] Clarify use of Enter/Space keys for opening/closing listbox ([openui/open-ui#386](https://github.com/openui/open-ui/issues/386))

The minutes record [dandclark](../../people/dandclark.md) and [chrisdholt](../../people/chrisdholt.md) agreeing that Open UI should follow the ARIA
Authoring Practices for Enter/Space handling in combobox/dropdown/select-type controls, while
[nicole](../../people/stubbornella.md) and hdv cautioned that some ARIA patterns are out of date and were not user-tested, so
Open UI should feed gaps back to the Authoring Practices task force. The scribe recorded two
resolutions in the IRC log: that such controls should defer to ARIA Best Practices design, and
that specification text for behaviors and interactions should leverage the ARIA Best Practices
as a starting point. These do not appear in the resolutions index because the bot comment did
not record them as resolution bullets. This feeds the
[customizable select](../../features/customizable-select.md) keyboard model.

([discussion](https://github.com/openui/open-ui/issues/386#issuecomment-916336828))

## [select] Clarify the need for both part="option" and `<option>` ([openui/open-ui#396](https://github.com/openui/open-ui/issues/396))

The minutes record [dandclark](../../people/dandclark.md) laying out the problem: allowing both `<option>` elements and
arbitrary elements labeled `part=option` creates subtle behavioral differences, because
HTMLOptionElement reflects IDL attributes like `disabled` while arbitrary elements do not.
Restricting options to `<option>` only would sidestep the issue but break custom-element
options; extending HTMLOptionElement via customized built-ins would not work in WebKit.
The minutes record BoCupp proposing a controller-code convention (check for the IDL attribute,
fall back to the content attribute) and [chrisdholt](../../people/chrisdholt.md) raising concern about obfuscated magic;
[masonf](../../people/mfreed7.md) suggested simply allowing arbitrary content inside `<option>` under `<selectmenu>`.
No resolution was recorded; [gregwhitworth](../../people/gregwhitworth.md) took an action to open a follow-up issue.
Part of the [customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/396#issuecomment-916408368))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
