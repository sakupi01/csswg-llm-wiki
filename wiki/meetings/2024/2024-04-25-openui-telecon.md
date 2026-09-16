---
date: 2024-04-25
group: openui
type: telecon
topics_count: 7
issues: [571, 600, 608, 637, 825, 926, 934]
generated_by: llm
---

# Open UI CG telecon — 2024-04-25

Seven topics, seven resolutions — a triage sweep through long-open [customizable
select](../../features/customizable-select.md) issues. Minutes recorded by the CSS meeting bot on
the linked issues. Official minutes:
[2024/04/25-openui-minutes.html](https://www.w3.org/2024/04/25-openui-minutes.html)
(dated-URL convention for CG minutes).

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

A quick close-out of one of the oldest selectmenu-era questions. The minutes record [gregwhitworth](../../people/gregwhitworth.md)
and [jarhar](../../people/josepharhar.md) as noting the group had already resolved to clone option content into
`<selectedoption>`, [masonf](../../people/mfreed7.md) as observing the latest issue comment supported that plan, and [keithamus](../../people/keithamus.md)
as suggesting only that closing messaging be added.

> RESOLVED: we already resolved to clone content from options into `<selectedoption>`. We will stick with that resolution.

([resolution](https://github.com/openui/open-ui/issues/571#issuecomment-2077986244))

## [selectmenu] How should writing-mode work with selectmenu ([openui/open-ui#600](https://github.com/openui/open-ui/issues/600))

una demonstrated that the prototype button did not respect `writing-mode` while the options did.
The minutes record [masonf](../../people/mfreed7.md) as saying support is a given and the tricky part is the behavior per
writing mode, [dbaron](../../people/dbaron.md) as expecting the interesting work to land in the default styles (written with
logical properties), and [gregwhitworth](../../people/gregwhitworth.md) as insisting on MUST-level language. Details were deferred
to the `appearance: base-select` UA stylesheet work for [customizable
select](../../features/customizable-select.md).

> RESOLVED: <select> MUST support writing-modes but it will be defined in another issue that covers the user-agent stylesheet default styles when appearance: base-select is set

([resolution](https://github.com/openui/open-ui/issues/600#issuecomment-2077965467))

## [selectmenu (& co.)] Figure out interaction with autofill. ([openui/open-ui#608](https://github.com/openui/open-ui/issues/608))

[jarhar](../../people/josepharhar.md) raised how autofill preview values should render in the new [customizable
select](../../features/customizable-select.md), suggesting a UA-internal popover as prototyped for
selectlist. The minutes record [masonf](../../people/mfreed7.md) as calling it a browser implementation question, and [flackr](../../people/flackr.md)
as warning a popover preview would badly overlay scrolled-out-of-view selects but agreeing it is up
to implementations. The group resolved only the observable constraint.

> RESOLVED: The new select should support autofill, and browsers should implement previews in a way which is not observable by the page

([resolution](https://github.com/openui/open-ui/issues/608#issuecomment-2077946090))

## SelectMenu placeholder capability? ([openui/open-ui#637](https://github.com/openui/open-ui/issues/637))

The group had previously resolved to reuse `<select>`'s existing placeholder idioms (a
disabled/selected empty option). The minutes record lukew and [brecht_dr](../../people/brechtDR.md) as attracted to treating
`<selectedoption>` as a slot that could hold placeholder content, [masonf](../../people/mfreed7.md) as fearing that would make
the just-resolved cloning model brittle, and [gregwhitworth](../../people/gregwhitworth.md) as concluding that with `<select>` being
reused this is no longer a battle worth having. Part of the [customizable
select](../../features/customizable-select.md) effort.

> RESOLVED: Keep the previous resolution which reuses the existing APIs for placeholders for select elements

([resolution](https://github.com/openui/open-ui/issues/637#issuecomment-2077928559))

## select: Should `<selectedoption>` respond to mutations in the selected `<option>` ([openui/open-ui#825](https://github.com/openui/open-ui/issues/825))

[jarhar](../../people/josepharhar.md) argued authors will expect `<selectedoption>` to track DOM changes in the selected option,
citing hydration flows that update options after load. The minutes record [dbaron](../../people/dbaron.md) as finding the
hydration example convincing, [masonf](../../people/mfreed7.md) as fearing the spec consequences and asking for real use
cases, and [keithamus](../../people/keithamus.md) as noting a web-component author would build this with slots anyway; [masonf](../../people/mfreed7.md)
countered that cloning (not slotting) is needed so button and popover copies can be styled
differently. This resolution was later reversed on
[2024-10-24](2024-10-24-openui-telecon.md). See [customizable
select](../../features/customizable-select.md).

> RESOLVED: The selectedoption element should update its contents when the selected options DOM descendants are modified

([resolution](https://github.com/openui/open-ui/issues/825#issuecomment-2077912960))

## [Selectlist] `<label>`s as children of `<selectlist>` ([openui/open-ui#926](https://github.com/openui/open-ui/issues/926))

[jarhar](../../people/josepharhar.md) asked whether a `<label>` inside the select's button should get special behavior, preferring
not. The minutes record [scotto](../../people/scottaohara.md) as saying the label belongs outside the control (with a plain `div`
for the border styling shown in the explainer example), and [masonf](../../people/mfreed7.md) agreeing the example was simply
not a good one. Part of the [customizable select](../../features/customizable-select.md) effort.

> RESOLVED: Change the example in the explainer to move the label text to a label element outside of the select element

([resolution](https://github.com/openui/open-ui/issues/926#issuecomment-2077889944))

## [invokers] Default actions for selectlist ([openui/open-ui#934](https://github.com/openui/open-ui/issues/934))

A short one: lukew noted `<select>` already has `showPicker()`, and the minutes record [masonf](../../people/mfreed7.md) as
agreeing that is the sensible default invoker action for the [customizable
select](../../features/customizable-select.md), leaving richer actions for later.

> RESOLVED: Leave it at just showPicker for now.

([resolution](https://github.com/openui/open-ui/issues/934#issuecomment-2077863126))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
