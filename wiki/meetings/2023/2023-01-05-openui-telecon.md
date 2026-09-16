---
date: 2023-01-05
group: openui
type: telecon
topics_count: 5
issues: [342, 578, 633, 635, 637]
generated_by: llm
---

# Open UI CG telecon — 2023-01-05

Five topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/01/05-openui-minutes.html](https://www.w3.org/2023/01/05-openui-minutes.html) (dated-URL convention for CG minutes).

## SelectMenu placeholder capability? ([openui/open-ui#637](https://github.com/openui/open-ui/issues/637))

The group took up whether `<selectmenu>` — the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)) — should get placeholder
functionality. The minutes record Sarah ([sarah_higley](../../people/smhigley.md)) as proposing it and favouring text-only
placeholders, [scotto](../../people/scottaohara.md) as asking whether text-only would rule out placeholder icons, and [masonf](../../people/mfreed7.md)
as noting the group had not yet resolved what to do with non-text options in the button anyway.
[JonathanNeal](../../people/jonathanneal.md) is recorded as wanting a `::placeholder` pseudo and a mostly symmetric API between
options and placeholders; Brecht raised that a pseudo-based approach could complicate
multi-language content. On [dandclark](../../people/dandclark.md)'s suggestion the group resolved the "whether" first and
deferred the "how" (tentatively slots/parts, to be explored in code snippets). A side thread on
plain-text alternative values for rich-text options was split off to a separate issue.

> RESOLVED: Add placeholder functionality of some sort

> RESOLVED: `<selectmenu>` should support placeholder functionality in some form

([resolution](https://github.com/openui/open-ui/issues/637#issuecomment-1372659701))

## Other topics

- [openui/open-ui#633](https://github.com/openui/open-ui/issues/633) — the group agreed to try Jitsi Meet for the next telecon ([resolution](https://github.com/openui/open-ui/issues/633#issuecomment-1372624024)).
- [openui/open-ui#635](https://github.com/openui/open-ui/issues/635) — popover "layers" for modals/toast stacking were declined for now ([resolution](https://github.com/openui/open-ui/issues/635#issuecomment-1372638607)).
- [openui/open-ui#342](https://github.com/openui/open-ui/issues/342) — popover show/hide event naming discussed without resolution.
- [openui/open-ui#578](https://github.com/openui/open-ui/issues/578) — async vs sync popover `hide` events, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
