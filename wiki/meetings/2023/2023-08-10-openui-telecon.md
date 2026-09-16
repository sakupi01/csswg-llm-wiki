---
date: 2023-08-10
group: openui
type: telecon
topics_count: 2
issues: [338, 786]
generated_by: llm
---

# Open UI CG telecon — 2023-08-10

Two topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/08/10-openui-minutes.html](https://www.w3.org/2023/08/10-openui-minutes.html) (dated-URL convention for CG minutes).

## [switch] Should a switch proposal graduate to the web platform? ([openui/open-ui#338](https://github.com/openui/open-ui/issues/338))

Prompted by a WebKit pull request adding a `switch` attribute to checkboxes. The minutes record
lilyspiniolas as presenting the proposal — a `switch` attribute limited to the checkbox state,
with graceful fallback in browsers that don't know the attribute, and thumb/track pseudo-classes
hoped for later. [jarhar](../../people/josepharhar.md) and una asked for more use-case gathering; [masonf](../../people/mfreed7.md) agreed demand is
strong but stressed real styleability is the bar, since `appearance: none` just leaves authors
styling a div. Philipp_Gfeller and [flackr](../../people/flackr.md) made the case that an attribute-based design limits
richer customisation (elements slotted inside the switch, swipe gestures) that a dedicated
`<switch>` element could support; [ntim](../../people/nt1m.md) countered that slotting is the only reason to want a new
element. [scotto](../../people/scottaohara.md) worried about interactive/nested content inside a switch and localisation
affecting its width. [masonf](../../people/mfreed7.md) closed by asking for the draft PR, issues and concepts to be brought
together into a simple explainer. No resolution was recorded.

## Other topics

- [openui/open-ui#786](https://github.com/openui/open-ui/issues/786) — exclusive accordion: whether `name`-grouped `<details>` should ever be non-exclusive, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
