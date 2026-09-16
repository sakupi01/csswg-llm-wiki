---
date: 2021-08-05
group: openui
type: telecon
topics_count: 3
issues: [357, 379, 380]
generated_by: llm
---

# Open UI CG telecon — 2021-08-05

Three topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2021-08-05](https://www.w3.org/2021/08/05-openui-minutes.html).

## [select] To what extent should customizable select implement the old `<select>`'s interface? ([openui/open-ui#380](https://github.com/openui/open-ui/issues/380))

The minutes record [dandclark](../../people/dandclark.md) framing two sides: matching the old `<select>`'s behavior so that
two similar dropdown elements don't diverge suspiciously, versus treating a new element as a
chance to fix past mistakes. The minutes record [bkardell](../../people/bkardell.md) arguing developer sentiment and adoption
should weigh heavily ("stay weird" so authors only learn the weirdness once), and una and [nicole](../../people/stubbornella.md)
citing developer surveys where form styling — especially `<select>` — topped the pain list.
[masonf](../../people/mfreed7.md) is recorded as supporting departures from the old API where there is good motivation. The
takeaway recorded: decide case by case, document every intentional divergence, and [nicole](../../people/stubbornella.md)
volunteered to draft a one-pager of principles. No resolution was recorded. This thread is part
of the [customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/380#issuecomment-893692365))

## Other topics

- [openui/open-ui#357](https://github.com/openui/open-ui/issues/357) — anchor positioning syntax for popups discussed.
- [openui/open-ui#379](https://github.com/openui/open-ui/issues/379) — ensuring `delegatesfocus` cannot trap focus.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
