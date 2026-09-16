---
date: 2023-03-16
group: openui
type: telecon
topics_count: 3
issues: [571, 648, 670]
generated_by: llm
---

# Open UI CG telecon — 2023-03-16

Three topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/03/16-openui-minutes.html](https://www.w3.org/2023/03/16-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics concern `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## [select] Should the inner HTML & styles of the selected option be copied into selected-value? ([openui/open-ui#571](https://github.com/openui/open-ui/issues/571))

A long-running issue (discussed since 2022): should selecting a rich option — say a country with
a flag — mirror the whole content into the `selected-value` part, not just its text? The minutes
record [jarhar](../../people/josepharhar.md) as sympathetic to the use case but noting there is no good mechanism: a "mirror
primitive" doesn't exist, and copying innerHTML is error-prone (duplicated IDs, and authors can
do it in a few lines of script anyway). [masonf](../../people/mfreed7.md) added the shadow-root complications and argued the
capability could come in a later iteration; [scotto](../../people/scottaohara.md) recalled prior accessibility concerns about
copying non-static HTML into the triggering element; [flackr](../../people/flackr.md) supported exploring it later.
JakeArchibald, newly joining, suggested CSSWG-style "story so far" summary comments on issues.

> RESOLVED: Don't implement behavior to copy innerHTML from the selected option into the selected value for V1 of selectmenu

([resolution](https://github.com/openui/open-ui/issues/571#issuecomment-1472206358))

## [selectmenu] Mechanism to use `<select>` as progressive enhancement? ([openui/open-ui#648](https://github.com/openui/open-ui/issues/648))

Returning from [the 2023-01-12 telecon](2023-01-12-openui-telecon.md): nesting a `<select>`
inside `<selectmenu>` as a built-in fallback. The minutes record [gregwhitworth](../../people/gregwhitworth.md) and [dandclark](../../people/dandclark.md) as
noting `<select>` parsing rules would make the simple nesting approach a mess, and [scotto](../../people/scottaohara.md) as
arguing that with arbitrary option content (e.g. a button inside an option) a text-only fallback
would submit garbage form content — only the plain-text case hdv had in mind could work. [masonf](../../people/mfreed7.md)
observed the parser would probably need to skip `<select>` entirely, while [jarhar](../../people/josepharhar.md)'s few-line
polyfill covers the need; xiaocheng and [flackr](../../people/flackr.md) agreed developers can build better fallbacks than
the browser could. bkardell_ asked the holistic question of why one would use selectmenu without
slots at all.

> RESOLVED: Don't support nesting select tags inside selectmenu tags as a progressive enhancement

([resolution](https://github.com/openui/open-ui/issues/648#issuecomment-1472261108))

## Other topics

- [openui/open-ui#670](https://github.com/openui/open-ui/issues/670) — agreed to adopt the proposed updated Open UI charter ([resolution](https://github.com/openui/open-ui/issues/670#issuecomment-1472185444)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
