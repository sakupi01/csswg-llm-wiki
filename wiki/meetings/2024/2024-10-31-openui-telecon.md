---
date: 2024-10-31
group: openui
type: telecon
topics_count: 4
issues: [1112, 1115, 1117, 1119]
generated_by: llm
---

# Open UI CG telecon — 2024-10-31

Four topics, three resolutions — all on [customizable
select](../../features/customizable-select.md). Minutes recorded by the CSS meeting bot on the
linked issues. Official minutes:
[2024/10/31-openui-minutes.html](https://www.w3.org/2024/10/31-openui-minutes.html)
(dated-URL convention for CG minutes).

## select: Naming of `<selectedoption>` ([openui/open-ui#1112](https://github.com/openui/open-ui/issues/1112))

The minutes record [masonf](../../people/mfreed7.md) as finding `<selectedoption>` confusing (authors would mistake it for the
option itself), steve ([sorvell](../../people/sorvell.md)) as relaying [JakeA](../../people/jakearchibald.md)'s vote for `selectedcontent` while noting the
name is long, and [masonf](../../people/mfreed7.md) as liking that "selected" (not "select") makes clear it holds content, not
an option. bkardell_ quipped that the `<output>` paradigm would help "if anyone outside this chat
knew about `<output>`".

> RESOLVED: rename the selectedoption element to selectedcontent

([resolution](https://github.com/openui/open-ui/issues/1112#issuecomment-2450527487))

## select: How should we render `<option label=label>text`? ([openui/open-ui#1115](https://github.com/openui/open-ui/issues/1115))

[jarhar](../../people/josepharhar.md) had implemented the customizable select ignoring the legacy `label` attribute, but scott
pushed back. The minutes record [dbaron](../../people/dbaron.md) as recounting the attribute's origin (a fallback for
browsers that lacked `<optgroup>`, a plan wrecked by staggered implementations), [sorvell](../../people/sorvell.md) as calling
it legacy but necessary to cover in the MVP, and sarah as proposing a separate `text` attribute for
the typeahead/value question (split into
[openui/open-ui#1118](https://github.com/openui/open-ui/issues/1118)). The resolution — including
its editorializing final sentence — was recorded verbatim.

> RESOLVED: render the label attribute for options when it is present, regardless of the select's appearance value, just like it already does. also the label attribute is bad.

([resolution](https://github.com/openui/open-ui/issues/1115#issuecomment-2450588524))

## select: Should `<selectedoption>` update when selecting the already-selected option ([openui/open-ui#1119](https://github.com/openui/open-ui/issues/1119))

Follow-up to the [2024-10-24](2024-10-24-openui-telecon.md) no-mutation-observation resolution:
[JakeA](../../people/jakearchibald.md) had enumerated which operations should re-clone. The minutes record [jarhar](../../people/josepharhar.md) as noting
re-cloning on `select.value` assignment removes the immediate need for a dedicated sync method,
[sorvell](../../people/sorvell.md) as adding the custom↔non-custom transition case and proxying [JakeA](../../people/jakearchibald.md)'s view that stale
clones are "an intentional tradeoff", and sarah as observing that devs who mutate options in place
almost certainly also set the value programmatically, so things self-correct.

> RESOLVED: adopt Jake's suggestions: Clone when re-assigning to select.value, don't clone when user selects the same option again

([resolution](https://github.com/openui/open-ui/issues/1119#issuecomment-2450565150))

## select: clarifying what should be used as the chosen value ([openui/open-ui#1117](https://github.com/openui/open-ui/issues/1117))

scott asked what a screen reader should announce as the select's value when authors customize or
skip `<selectedcontent>` entirely. The minutes record scott as leaning toward ignoring ARIA labels
on button/selectedcontent (they do not contribute to the select's name), [sorvell](../../people/sorvell.md) as voting for
announcing the entire button contents, sarah as noting real patterns (placeholder-text buttons with
tags elsewhere) where the button text is not the value, and [jarhar](../../people/josepharhar.md) as sketching a name/value split
in the accessibility tree (button text as name, selected option as value). No resolution was
recorded; the topic returned on [2024-11-21](2024-11-21-openui-telecon.md).

([bot comment](https://github.com/openui/open-ui/issues/1117#issuecomment-2450620925))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
