---
date: 2022-08-11
group: openui
type: telecon
topics_count: 4
issues: [532, 540, 568, 571]
generated_by: llm
---

# Open UI CG telecon — 2022-08-11

Four topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-08-11](https://www.w3.org/2022/08/11-openui-minutes.html).

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

The straw poll that settled weeks of debate. The minutes record the two options put to the
group: (A) allow developers to put anything in, with a console warning when it would be
inaccessible, or (B) restrict what `<selectmenu>` can contain for accessibility certainty. The
recorded vote was A 8 (una, [jhey](../../people/jhey.md), [emilio](../../people/emilio.md), vicgutt, [flackr](../../people/flackr.md), [masonf](../../people/mfreed7.md), [dandclark](../../people/dandclark.md), [vmpstr](../../people/vmpstr.md)) to B 5
([sarah_h](../../people/smhigley.md), hdv, oluOnline, sana, [miriam](../../people/miriam.md)), with [tantek](../../people/tantek.md) and [scotto](../../people/scottaohara.md) abstaining — [scotto](../../people/scottaohara.md) "still
having concerns with both". [gregwhitworth](../../people/gregwhitworth.md) is recorded reiterating that resolutions can be
revisited as usage data arrives. Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: Allow interactive content outside of <options>, but issue strong console errors or warnings in this case.

([resolution](https://github.com/openui/open-ui/issues/540#issuecomment-1212330487))

## Selecting based on user changing values ([openui/open-ui#568](https://github.com/openui/open-ui/issues/568))

A CSSWG-adjacent question: a pseudo-class for form controls whose value the user changed. The
minutes record [emilio](../../people/emilio.md) preferring one pattern covering the main use cases over an explosion of
pseudo-classes, [scotto](../../people/scottaohara.md) insisting a purely visual indicator must also be exposed
programmatically (users with cognitive disabilities, or who are blind, would otherwise not know
a value changed), [masonf](../../people/mfreed7.md) and vicgutt floating a functional pseudo, [dbaron](../../people/dbaron.md) recalling an earlier
`:value` proposal in attribute selectors shelved over data-exfiltration worries, and una
suggesting style/state queries with [miriam](../../people/miriam.md) noting inputs have no contents to query from.
No resolution was recorded.

([discussion](https://github.com/openui/open-ui/issues/568#issuecomment-1212351389))

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

First discussion of what the button's `selected-value` part should show: today just the option's
text, but rich options (avatar + name) raise the question of copying the whole content. The
minutes record [gregwhitworth](../../people/gregwhitworth.md) favoring cloning the option's innerHTML into `selected-value`
(hiding is easy in CSS, adding content back requires JS), [masonf](../../people/mfreed7.md) suggesting imperative slotting
and calling it a "V-forever" back-compat question, [scotto](../../people/scottaohara.md) and [sarah_h](../../people/smhigley.md) noting it is more common
to *exclude* parts of an option from the trigger than to copy everything, and [tantek](../../people/tantek.md) asking
whether any UI framework hoists rich option content at all. Participants were asked to collect
use cases; no resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/571#issuecomment-1212361471))

## Other topics

- [openui/open-ui#532](https://github.com/openui/open-ui/issues/532) — resolved not to rename `popup=hint` ([resolution](https://github.com/openui/open-ui/issues/532#issuecomment-1212336046)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
