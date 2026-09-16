---
date: 2022-09-29
group: openui
type: telecon
topics_count: 3
issues: [548, 571, 600]
generated_by: llm
---

# Open UI CG telecon — 2022-09-29

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-09-29](https://www.w3.org/2022/09/29-openui-minutes.html).

## [selectmenu] Method to change arrow icon? ([openui/open-ui#548](https://github.com/openui/open-ui/issues/548))

Naming the slot resolved on 2022-06-30. The minutes record [dandclark](../../people/dandclark.md) opening with "icon";
scottkellum and AlexanderFutekov suggested "marker" for consistency with the CSS `::marker`
pseudo-element, while [scotto](../../people/scottaohara.md) recalled that details/summary's marker leaks into the accessible
name and [masonf](../../people/mfreed7.md) mainly wanted to avoid `button-*`/`dropdown-*` names. A straw poll leaned to
"marker", and after [gregwhitworth](../../people/gregwhitworth.md) pushed to also expose it for CSS, the resolution covered both
the slot and a `part`. [bkardell](../../people/bkardell.md) is recorded unearthing the 2002 CSS3 Lists note that "the name
::marker is temporary… seriously overloaded". Part of the
[customizable select](../../features/customizable-select.md) history.

> RESOLVED: The slot around the selectmenu's button's icon is named "marker". The marker will also be addressible via a `part=marker` attribute.

([resolution](https://github.com/openui/open-ui/issues/548#issuecomment-1262650219))

## [selectmenu] How should writing-mode work with selectmenu ([openui/open-ui#600](https://github.com/openui/open-ui/issues/600))

The minutes record [gregwhitworth](../../people/gregwhitworth.md) raising interop gaps in how browsers apply vertical writing
modes to the current `<select>`, and pushing for a MUST where form controls have historically
had SHOULDs. The minutes record [dbaron](../../people/dbaron.md) explaining that vertical text is a stylistic choice for
Chinese/Japanese but mandatory for languages like Mongolian, and [dandclark](../../people/dandclark.md) noting the odd
Chromium state where the popup respected vertical writing mode but the button didn't — the two
should at least be consistent. scottkellum is recorded widening the point to all form controls
as an interop problem, with [masonf](../../people/mfreed7.md) +1ing writing modes for form controls as an Interop 2023
candidate. Part of the [customizable select](../../features/customizable-select.md) history.

> RESOLVED: UAs must respect writing-mode for all of a selectmenu's default content.

([resolution](https://github.com/openui/open-ui/issues/600#issuecomment-1262667387))

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

The minutes record [gregwhitworth](../../people/gregwhitworth.md) proposing to keep the option's `value` as a string but clone
the option's innerHTML into the `selected-value` part (use case: rich options such as avatar +
name, color swatches). The minutes record [dandclark](../../people/dandclark.md) flagging pitfalls — stylesheet-dependent
styling and duplicated IDs on cloned content — and preferring a deep clone over serializing
through the parser if anything; [sarah_h](../../people/smhigley.md) countering that excluding parts of an option from the
trigger is the more common need, so the default should stay a string value; [masonf](../../people/mfreed7.md) noting the
selectmenu demo achieves the cloning in about 3 lines of JS; and AlexanderFutekov recalling
CSS-only mirrors (`element()`, `-webkit-box-reflect`). [gregwhitworth](../../people/gregwhitworth.md) took an action to survey
design systems and email clients; no resolution was recorded. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/571#issuecomment-1262691570))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
