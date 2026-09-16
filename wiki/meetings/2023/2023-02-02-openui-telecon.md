---
date: 2023-02-02
group: openui
type: telecon
topics_count: 4
issues: [600, 633, 645, 657]
generated_by: llm
---

# Open UI CG telecon — 2023-02-02

Four topics, one resolution captured by the bot. Minutes recorded by the CSS meeting bot on the
linked issues.
Official minutes: [w3.org/2023/02/02-openui-minutes.html](https://www.w3.org/2023/02/02-openui-minutes.html) (dated-URL convention for CG minutes).

All three detailed topics concern `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## [selectmenu] How should writing-mode work with selectmenu ([openui/open-ui#600](https://github.com/openui/open-ui/issues/600))

The minutes record ScottKellum as reporting that writing-mode support in classic `<select>` is
inconsistent across contexts and that the earlier proposal was to change "should" to "must" in
the spec — now overtaken by the topic joining Interop 2023. He offered three options: leave
as-is, still change the spec, or close the issue as handled. [masonf](../../people/mfreed7.md) preferred keeping the issue
open until `<selectmenu>` ships with writing modes working, and adding an Interop test case for
selectmenu specifically; [gregwhitworth](../../people/gregwhitworth.md) agreed closing before the spec changes would be
premature. The issue stays open for the next owners of selectmenu.
No resolution was recorded.

## [selectmenu] Add CSS selector to consistently select selectmenu parts ([openui/open-ui#645](https://github.com/openui/open-ui/issues/645))

The minutes record xiaocheng as proposing a new pseudo selector because `::part()` cannot select
selectmenu parts in all cases — notably when the listbox is slotted in from an outer tree scope
or lives in the light DOM. [masonf](../../people/mfreed7.md) supported making the same CSS work however the parts are
provided; [gregwhitworth](../../people/gregwhitworth.md) asked whether `::part()` itself could be expanded instead, but agreed
the light-DOM case cannot fit its definition. The minutes record a resolution typed as
"Resolved: We recommend to add a new CSS pseudo selector of ::behavior which will allow
selection within a shadow or light DOM" (lower-case, so not captured in the bot's resolution
summary); [gregwhitworth](../../people/gregwhitworth.md) anticipated the CSSWG would want to bikeshed the `::behavior` name.

## Should `<selectmenu>`'s `selected-value` support slot assignment? ([openui/open-ui#657](https://github.com/openui/open-ui/issues/657))

The minutes record [jarhar](../../people/josepharhar.md) as asking whether omitting a slot for the `selected-value` part was
intentional, since the `behavior` attribute replaces the slotted element's text content with the
selected option's text. [masonf](../../people/mfreed7.md) liked being able to provide custom content for the displayed
value but questioned how useful it is if the text content is overwritten; [gregwhitworth](../../people/gregwhitworth.md) added
background that an earlier anatomy sketch assumed innerHTML (not just text) would be reflected,
which is no longer the case, and supported slots on all parts for consistency.

> RESOLVED: all elements which support the behavior attribute should also by default support slotting with the slot attribute

([resolution](https://github.com/openui/open-ui/issues/657#issuecomment-1414262186))

## Other topics

- [openui/open-ui#633](https://github.com/openui/open-ui/issues/633) — follow-up on moving telecons to Jitsi (the call itself hit Jitsi audio problems and moved to Google Meet mid-meeting).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
