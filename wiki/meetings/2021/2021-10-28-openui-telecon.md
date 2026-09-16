---
date: 2021-10-28
group: openui
type: telecon
topics_count: 2
issues: [354, 396]
generated_by: llm
---

# Open UI CG telecon — 2021-10-28

Two topics, no bot-recorded resolutions (the IRC logs record "Resolved" lines on both issues
that the bot did not surface as resolution bullets). Minutes recorded by the CSS meeting bot
on the linked issues.
Official minutes: [2021-10-28](https://www.w3.org/2021/10/28-openui-minutes.html).

## [SELECT] The use of "part" clashes with custom elements containing `<selectmenu>` ([openui/open-ui#354](https://github.com/openui/open-ui/issues/354))

The minutes record [dandclark](../../people/dandclark.md) explaining that `<selectmenu>` overloaded the `part` attribute:
it both applied controller-code behavior and exposed elements for styling across shadow
boundaries (the CSS `::part()` feature) — desirable at different times but not always together.
The minutes record [nicole](../../people/stubbornella.md) relaying that framework authors (Stencil, Ionic) had use cases for the
two meanings separately, and [flackr](../../people/flackr.md) calling the overload bad design. Candidate names included
`controlpart`, `as`/`as-part` (davidluhr), and `behavior`, which [gregwhitworth](../../people/gregwhitworth.md), [masonf](../../people/mfreed7.md), [flackr](../../people/flackr.md)
and [scottohara](../../people/scottaohara.md) supported. The scribe recorded a resolution to use a `behavior` content attribute
instead of `part` for applying controller code; it does not appear in the resolutions index
because the bot comment did not record it as a resolution bullet. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/354#issuecomment-954161227))

## [select] Clarify the need for both part="option" and `<option>` ([openui/open-ui#396](https://github.com/openui/open-ui/issues/396))

Continuation of the 2021-09-09 discussion. The minutes record [dandclark](../../people/dandclark.md) proposing, as a
simplification, that `<selectmenu>` option controller code apply only to HTMLOptionElement —
custom-element options could inherit from HTMLOptionElement (not supported in WebKit today) or
simply contain `<option>` elements, as [masonf](../../people/mfreed7.md) noted. The minutes record [gregwhitworth](../../people/gregwhitworth.md) predicting
"custom option custom elements" would fade over time and offering to sound out WebKit. The
scribe recorded a resolution that `<selectmenu>` option part controller code is only applied to
HTMLOptionElements; it does not appear in the resolutions index because the bot comment did not
record it as a resolution bullet. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/396#issuecomment-954084906))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
