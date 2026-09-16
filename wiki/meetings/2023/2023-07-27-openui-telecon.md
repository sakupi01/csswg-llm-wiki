---
date: 2023-07-27
group: openui
type: telecon
topics_count: 4
issues: [665, 702, 767, 773]
generated_by: llm
---

# Open UI CG telecon — 2023-07-27

Four topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/07/27-openui-minutes.html](https://www.w3.org/2023/07/27-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics feed into the history of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## [select] Don't reuse `slot=""` and `::part()`; `behavior=""` is also strange ([openui/open-ui#702](https://github.com/openui/open-ui/issues/702))

The architectural turning point raised by Domenic's feedback: web-component features (slots,
parts) are meant for authors, not browsers, and HTML routinely defines elements only meaningful
inside another element. The minutes record [gregwhitworth](../../people/gregwhitworth.md) as summarising that history and
worrying about complex compositions like split buttons without slotting; [masonf](../../people/mfreed7.md) as reframing it
as an ergonomics question (`<selectmenubutton>` vs an attribute) that the WHATWG editors'
preference will likely decide; and una as asking whether a datepicker would blow up into dozens
of elements — [masonf](../../people/mfreed7.md) answered that element-specific (non-global) attributes are acceptable.
[scotto](../../people/scottaohara.md) favoured dedicated elements: a required, styleable-but-not-replaceable trigger element
avoids the early demos where replacing the button broke the control, and elements known to
contain interactive content can be planned for in accessibility terms. [keithamus](../../people/keithamus.md) pushed for
looser, reusable element names (`summary` works inside `details` without being `detailssummary`)
and cross-linked the invoker discussion; [masonf](../../people/mfreed7.md) countered that highly generic attributes take
years and often die. [nicole](../../people/stubbornella.md) called for design resources to map anatomies and lamented such
feedback arriving this late. una proposed a work session comparing (a) reusing existing
elements, (b) new elements for everything, (c) attributes. No resolution was recorded that day.

## Rename `selectmenu` to `selectbox` ([openui/open-ui#773](https://github.com/openui/open-ui/issues/773))

The minutes record [masonf](../../people/mfreed7.md) as reporting the naming poll standings — "selectbox" leading by one
vote, "picklist" the runner-up — and judging the result not definitive enough to resolve on,
asking people to share the poll for more votes. No resolution was recorded.

## Other topics

- [openui/open-ui#767](https://github.com/openui/open-ui/issues/767) — resolved to use `popovertargetaction=interest` for hover/focus triggering ([resolution](https://github.com/openui/open-ui/issues/767#issuecomment-1654177227)).
- [openui/open-ui#665](https://github.com/openui/open-ui/issues/665) — follow-up on the meeting day/time change.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
