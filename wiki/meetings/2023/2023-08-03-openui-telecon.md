---
date: 2023-08-03
group: openui
type: telecon
topics_count: 2
issues: [702, 773]
generated_by: llm
---

# Open UI CG telecon — 2023-08-03

Two topics, two resolutions — a landmark meeting for the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)): the control was renamed to
`<selectlist>` and its architecture switched from slots to dedicated elements. Minutes recorded
by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/08/03-openui-minutes.html](https://www.w3.org/2023/08/03-openui-minutes.html) (dated-URL convention for CG minutes).

## Rename `selectmenu` to `selectbox` ([openui/open-ui#773](https://github.com/openui/open-ui/issues/773))

Concluding the poll from [2023-07-13](2023-07-13-openui-telecon.md) and
[2023-07-27](2023-07-27-openui-telecon.md). The minutes record [masonf](../../people/mfreed7.md) as restating the problem —
the control is not a "menu" — and reporting that after social-media sharing the vote had
tightened between `selectlist` and `selectbox` (27 vs 20 live during the meeting). una argued
"list" is more semantic than "box" (a shape), and that a future `listbox` element next to a
`selectbox` would confuse; [brecht_dr](../../people/brechtDR.md) agreed "box" is old-school and non-descriptive. una floated
`<selectpicker>` late but declined to make it a formal objection.

> RESOLVED: rename `<selectmenu>` to `<selectlist>`.

([resolution](https://github.com/openui/open-ui/issues/773#issuecomment-1664421419))

## [select] Don't reuse `slot=""` and `::part()`; `behavior=""` is also strange ([openui/open-ui#702](https://github.com/openui/open-ui/issues/702))

Concluding the architecture debate opened by Domenic's feedback (see
[2023-07-27](2023-07-27-openui-telecon.md)). The minutes record [masonf](../../people/mfreed7.md) as presenting the
prototype he and [jarhar](../../people/josepharhar.md) built: replacing every slot with elements needs only two new elements —
`<selectlist>` itself acts as the container, an attribute (`<button type=selectmenu>`) marks the
trigger, and a `listbox` element is only needed to customise the listbox (options alone get one
implicitly, which [flackr](../../people/flackr.md) compared to `<table>` auto-creating `tbody`). [scotto](../../people/scottaohara.md) probed how
arbitrary non-button content should be treated and compared the implicit-part behavior to
`<details>`/`<summary>`; [brecht_dr](../../people/brechtDR.md) questioned a dedicated selected-value element (adam suggested
`<output>` in chat, which [scotto](../../people/scottaohara.md) noted is a live region by default); westbrook_ pressed for the
design to stay compatible with web components; [nicole](../../people/stubbornella.md) argued skipped wrapper elements reduce
styleability use cases. bkardell_ said plainly he did not understand the new structure well
enough to form an opinion and asked for more examples, though he did not object.

> RESOLVED: move forward with the "elements" approach for `<selectlist>`, abandoning the "slots" approach. Open fresh issues for any new questions.

([resolution](https://github.com/openui/open-ui/issues/702#issuecomment-1664464531))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
