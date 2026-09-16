---
date: 2026-02-19
group: openui
type: telecon
topics_count: 4
issues: [1282, 1355, 1369, 1372]
generated_by: llm
---

# Open UI CG telecon — 2026-02-19

Four topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/02/19-openui-minutes.html](https://www.w3.org/2026/02/19-openui-minutes.html) (dated-URL convention for CG minutes).

## [switch] Should the explainer be rewritten to support the switch attribute? ([openui/open-ui#1282](https://github.com/openui/open-ui/issues/1282))

The switch explainer proposed a new element, but WebKit has shipped `<input switch>` as an
attribute. The minutes record philipp as asking whether to keep the element proposal, and
conceding the only concrete benefit of an element is putting rich content (text, inline SVG) on
the track — with the attribute that needs CSS. [masonf](../../people/mfreed7.md) is recorded as seeing no value in a separate
explainer absent a concrete improvement; [lwarlow](../../people/lukewarlow.md) argued the shipped attribute is "not fatally
flawed" and covers most cases (the rich-content gap applies to all inputs), though he doubted
shipping it in Chromium without `appearance: base`. nmn is recorded as fine with shipping under
`appearance: auto`, and ollie noted Safari's two-year-old implementation with thumb/track pseudos
works reasonably well.

> RESOLVED: rewrite explainer to incorporate switch attribute

([resolution](https://github.com/openui/open-ui/issues/1282#issuecomment-3929622950))

## [Select] What to do with selectedcontent when multiple select is set with size 1 ([openui/open-ui#1355](https://github.com/openui/open-ui/issues/1355))

The bot comment on this issue dated 2026-02-19 records a **CSS Working Group** discussion (not
the CG's own call): [jarhar](../../people/josepharhar.md) briefed the CSSWG on the Open UI resolution to auto-wrap each cloned
option's content in `<selectedcontent>` for the multi-select customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [lwarlow](../../people/lukewarlow.md)
as accepting wrappers given that adding `<selectedcontent>` is an opt-in, while insisting the
default rendering not be garbage; [jarhar](../../people/josepharhar.md) countered that the harder problem is what to render when
zero options are selected (a placeholder option "is kind of weird too") and said he would continue
prototyping the wrapper approach and gather feedback. No resolution was recorded in this group.

([discussion](https://github.com/openui/open-ui/issues/1355#issuecomment-3928467441))

## Other topics

- [openui/open-ui#1369](https://github.com/openui/open-ui/issues/1369) — the group agreed that a `<label>` should count as part of light dismiss for the popover its button controls ([resolution](https://github.com/openui/open-ui/issues/1369#issuecomment-3929535576)).
- [openui/open-ui#1372](https://github.com/openui/open-ui/issues/1372) — the group agreed to incubate "Declarative Overscroll Actions" inside Open UI ([resolution](https://github.com/openui/open-ui/issues/1372#issuecomment-3929508361)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
