---
date: 2023-04-13
group: openui
type: telecon
topics_count: 1
issues: [637]
generated_by: llm
---

# Open UI CG telecon — 2023-04-13

One topic, no resolutions. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [w3.org/2023/04/13-openui-minutes.html](https://www.w3.org/2023/04/13-openui-minutes.html) (dated-URL convention for CG minutes).

## SelectMenu placeholder capability? ([openui/open-ui#637](https://github.com/openui/open-ui/issues/637))

Third round on placeholders for `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
laying out the candidates so far — a `placeholder` attribute on `<selectmenu>`, an attribute on
`<option>`, or the existing hidden-first-option hack — and proposing a placeholder attribute on
`<option>`. una and [scotto](../../people/scottaohara.md) are recorded as agreeing the `placeholder` name should not be reused
if the value is not a text string; [scotto](../../people/scottaohara.md) clarified his earlier `hidden`-attribute demo showed
how it can be done today, not an ideal design, and floated marking an option as the placeholder
or even a dedicated `<placeholderoption>` element. [dbaron](../../people/dbaron.md) relayed that the i18n Working Group
prefers presentable text not live in attributes (directionality, ruby); [masonf](../../people/mfreed7.md) countered with a
`placeholder="id"` attribute referencing an option. The alternatives were taken back to the
issue. No resolution was recorded.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
