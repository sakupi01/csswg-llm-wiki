---
date: 2022-07-28
group: openui
type: telecon
topics_count: 2
issues: [540, 558]
generated_by: llm
---

# Open UI CG telecon — 2022-07-28

Two topics, two resolutions (both on [openui/open-ui#558](https://github.com/openui/open-ui/issues/558)).
Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-07-28](https://www.w3.org/2022/07/28-openui-minutes.html) (dated-URL convention).

## [selectmenu] Accessibility of option labels ([openui/open-ui#558](https://github.com/openui/open-ui/issues/558))

How to label option groups in `<selectmenu>` when `<optgroup label=…>` can't be styled. The
minutes record [dandclark](../../people/dandclark.md) proposing a `<legend>` element inside `<optgroup>` whose text content
becomes the group's accessible name — visible, styleable text instead of an attribute — with a
console warning for stray text outside options. The minutes record [scotto](../../people/scottaohara.md) supporting the move
and proposing the clean rule that the `label` attribute simply isn't supported inside
`<selectmenu>`; [tantek](../../people/tantek.md) agreed human-readable text belongs in element content, questioned whether
`<legend>` carries fieldset parsing baggage ([dandclark](../../people/dandclark.md) had researched: it doesn't), and argued
back-compat with "decades-long patterns" matters for users, not for developers. Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: the `label` attribute is not supported within <selectmenu>.

> RESOLVED: Use the <legend> element for labeling <selectmenu> <optgroup>s as described in https://github.com/openui/open-ui/issues/558#issue-1289047468.

([resolution](https://github.com/openui/open-ui/issues/558#issuecomment-1198490800))

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

The topic was opened as a continuation, but the bot comment for this date records only the
topic line — no substantive log was captured on this issue this day. The debate continued on
2022-08-04 and was resolved by straw poll on 2022-08-11. Part of the
[customizable select](../../features/customizable-select.md) history.

([bot comment](https://github.com/openui/open-ui/issues/540#issuecomment-1198467379))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
