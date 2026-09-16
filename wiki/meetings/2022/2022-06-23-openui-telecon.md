---
date: 2022-06-23
group: openui
type: telecon
topics_count: 2
issues: [495, 536]
generated_by: llm
---

# Open UI CG telecon — 2022-06-23

Two topics, resolutions on both. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-06-23](https://www.w3.org/2022/06/23-openui-minutes.html).

## [selectmenu] Interoperability of styles ([openui/open-ui#536](https://github.com/openui/open-ui/issues/536))

A foundational styling decision for `<selectmenu>` — the direct ancestor of today's
`appearance: base-select` model for the
[customizable select](../../features/customizable-select.md). The minutes record [masonf](../../people/mfreed7.md)
proposing that `<selectmenu>` render identically across browsers by default, controlled by the
`appearance` property: `none` for a standardized minimal "interoperable" stylesheet (like
`<dialog>`'s ~10 lines of CSS), `auto` for UA-opinionated styling. The minutes record
[JonathanNeal](../../people/jonathanneal.md) noting one minimal stylesheet may not fit all form factors, [gregwhitworth](../../people/gregwhitworth.md) framing
interoperable control styles as a requirement for everything Open UI ships going forward (and
demanding MUST rather than SHOULD for the default), [chrishtr](../../people/chrishtr.md) predicting few developers would use
`auto` and flagging the contrast/accessibility question when developer CSS meets UA styling, and
una cautioning she could not speak for browser UX owners. The bot recorded the resolution twice,
in two wordings ("needs to ensure" and the MUST correction):

> RESOLVED: the <selectmenu> will have a "mode" that makes it have the same, standardized default styling. The appearance property will control this mode, with none being "interoperable" and auto being "UA opinionated styling". The default value for `appearance` for <selectmenu> must be "none". In 'auto' mode, the UA needs to ensure contrast/accessibility between developer-provided CSS and the UA's own opinionated styling.

> RESOLVED: the <selectmenu> will have a "mode" that makes it have the same, standardized default styling. The appearance property will control this mode, with none being "interoperable" and auto being "UA opinionated styling". The default value for `appearance` for <selectmenu> must be "none". In 'auto' mode, the UA must ensure contrast/accessibility between developer-provided CSS and the UA's own opinionated styling.

([resolution](https://github.com/openui/open-ui/issues/536#issuecomment-1164737967))

## Other topics

- [openui/open-ui#495](https://github.com/openui/open-ui/issues/495) — resolved that the `popup` attribute describes only behavior, not semantics, and that `popup=async` is renamed to `popup=manual` ([resolution](https://github.com/openui/open-ui/issues/495#issuecomment-1164827851)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
