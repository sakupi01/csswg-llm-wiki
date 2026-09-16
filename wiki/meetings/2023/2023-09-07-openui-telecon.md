---
date: 2023-09-07
group: openui
type: telecon
topics_count: 3
issues: [807, 815, 821]
generated_by: llm
---

# Open UI CG telecon — 2023-09-07

Three topics, four resolutions recorded (one duplicated by the bot). Minutes recorded by the CSS
meeting bot on the linked issues.
Official minutes: [w3.org/2023/09/07-openui-minutes.html](https://www.w3.org/2023/09/07-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics concern `<selectlist>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## [selectlist] Add `showPicker()` method to `<selectlist>` ([openui/open-ui#807](https://github.com/openui/open-ui/issues/807))

The minutes record Luke_W_ as noting WHATWG added `showPicker()` to input elements and deferred
`<select>`, so selectlist should follow; una asked about toggle/close variants (tracked as future
work). [masonf](../../people/mfreed7.md) recalled the original hesitation — some browsers lack pickers for some input types,
and revealing whether a picker was shown was seen as a platform leak — but judged it inapplicable
to select/selectlist, which always have pickers. [jarhar](../../people/josepharhar.md) and [masonf](../../people/mfreed7.md) converged on following the
existing input conventions.

> RESOLVED: Add showPicker to selectlist matching existing input conventions, other methods can be added across the board in future if need be.

([resolution](https://github.com/openui/open-ui/issues/807#issuecomment-1710601627))

## Should all `<button type=selectlist>`s get behavior? What about `<button>`? ([openui/open-ui#821](https://github.com/openui/open-ui/issues/821))

An implementation question from [jarhar](../../people/josepharhar.md)'s work on the new elements architecture: should any button
inside a selectlist open the listbox (with an opt-out), or only buttons explicitly marked
`type=selectlist`? The minutes record [masonf](../../people/mfreed7.md) as initially favouring making the 98% single-button
case implicit, but Luke_W_, una, [brecht_dr](../../people/brechtDR.md) and scotto_ argued for the explicit attribute: it
makes intent visible (una had been prototyping and found untyped buttons ambiguous), avoids
accidental form submission by typeless buttons, keeps split-button cases coherent, and allows
multiple trigger buttons (e.g. only one visible at a time). [masonf](../../people/mfreed7.md) recorded that he changed his
mind. The bot's RESOLVED line carries a stray leading colon, quoted verbatim below.

> RESOLVED: : keep type=selectlist as a requirement for buttons which open the listbox, and allow multiple type=selectlist buttons to each have listbox toggling behavior.

([resolution](https://github.com/openui/open-ui/issues/821#issuecomment-1710592976))

## Other topics

- [openui/open-ui#815](https://github.com/openui/open-ui/issues/815) — resolved to support "interest"-triggering on anchor elements, expanding to other elements later ([resolution](https://github.com/openui/open-ui/issues/815#issuecomment-1710631016)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
