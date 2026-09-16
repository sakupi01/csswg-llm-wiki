---
date: 2023-08-24
group: openui
type: telecon
topics_count: 5
issues: [799, 801, 804, 808, 809]
generated_by: llm
---

# Open UI CG telecon — 2023-08-24

Five topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/08/24-openui-minutes.html](https://www.w3.org/2023/08/24-openui-minutes.html) (dated-URL convention for CG minutes).

## [switch]: Naming of the component and its parts ([openui/open-ui#804](https://github.com/openui/open-ui/issues/804))

The minutes record philippgfeller as walking through his draft switch explainer and asking for a
name check (`<switch>` vs `<toggle>` vs other). [masonf](../../people/mfreed7.md) kept the competing proposal — reusing
`<input>` with a `switch` attribute, which falls back to a checkbox in older browsers — on the
table, asking what share of use cases each covers (philippgfeller's design-system analysis:
~70% need no text/imagery inside the switch). Luke ([lukewarlow](../../people/lukewarlow.md)) preferred a new element matching
the ARIA role and free of `input`'s behavioral history; scotto_ insisted on not calling it a
"toggle" (a toggle button with `aria-pressed` is semantically different) and, with [dbaron](../../people/dbaron.md) and
[gregwhitworth](../../people/gregwhitworth.md), cautioned against browser-provided on/off text for localisation and accessibility
reasons — the default should be empty and decorative content hidden from AT. [masonf](../../people/mfreed7.md) asked the
explainer to add a section contrasting `<input type=checkbox switch>` before landing.

> RESOLVED: call the new element `<switch>`, and land that in the explainer. Discuss the sub-parts later.

([resolution](https://github.com/openui/open-ui/issues/804#issuecomment-1692233975))

## Naming of the selected value element ([openui/open-ui#808](https://github.com/openui/open-ui/issues/808))

Part of the `<selectlist>` elements redesign (see
[customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
proposing `<selectedoption>` (rather than his earlier `<selectedvalue>`) since it renders the
selected option; [masonf](../../people/mfreed7.md) hoped for a name reusable beyond selectlist (`<value>`,
`<currentselection>`), but his own file-input example undercut it — scotto_ pointed out a chosen
file is not an "option". scotto_ also probed placement (must it live inside the trigger button?)
and how the mirrored content reaches the accessibility tree; [masonf](../../people/mfreed7.md) answered it can sit anywhere
within the selectlist, with much still to prototype. [jarhar](../../people/josepharhar.md) declined to resolve on a name that
might be reverted. No resolution was recorded.

## [selectlist] Should we worry about existing button behavior? ([openui/open-ui#809](https://github.com/openui/open-ui/issues/809))

The risk: in browsers without `<selectlist>`, `<button type=selectlist>` degrades to a plain
button whose default form behavior is submission. The minutes record [masonf](../../people/mfreed7.md) as offering
alternatives (a new element — "at best confusing, at worst terrible" — or a non-`type`
attribute), while [jarhar](../../people/josepharhar.md) and scotto_ argued the concern is moot: a selectlist page in an
unsupporting browser is already broken without a polyfill, and a polyfill handles the button
too. lukew's idea of making buttons inside unknown elements not submit forms was rejected as
breaking custom elements.

> RESOLVED: Keep the current <button type=selectlist> proposal the way it is because polyfills would be required to make selectlist work anyway

([resolution](https://github.com/openui/open-ui/issues/809#issuecomment-1692191406))

## Other topics

- [openui/open-ui#799](https://github.com/openui/open-ui/issues/799) — agreed to land a `<table>` UI enhancements explainer ([resolution](https://github.com/openui/open-ui/issues/799#issuecomment-1692244445)).
- [openui/open-ui#801](https://github.com/openui/open-ui/issues/801) — agreed to revamp the website to separate active from historical material ([resolution](https://github.com/openui/open-ui/issues/801#issuecomment-1692255256)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
