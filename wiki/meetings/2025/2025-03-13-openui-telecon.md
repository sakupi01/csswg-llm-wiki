---
date: 2025-03-13
group: openui
type: telecon
topics_count: 4
issues: [1156, 1158, 1159, 1175]
generated_by: llm
---

# Open UI CG telecon — 2025-03-13

Four topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/03/13-openui-minutes.html](https://www.w3.org/2025/03/13-openui-minutes.html) (dated-URL convention for CG minutes).

## [openable] Does defaultopen as a separate attribute make sense? ([openui/open-ui#1156](https://github.com/openui/open-ui/issues/1156))

How to declare an initially-open openable when the same element could also be a popover or
dialog. The minutes record [lwarlow](../../people/lukewarlow.md) as laying out options (separate attributes, an enum attribute,
or one attribute with defined conflict handling); [masonf](../../people/mfreed7.md) favoured an `initiallyopen`-style
attribute with a missing-value default, arguing that a state-reflecting attribute like
`<details open>` has ugly edge cases around DOM removal/insertion, while [sorvell](../../people/sorvell.md) preferred the
details model precisely because a live declarative attribute is usable from every framework
without refs. [brecht_dr](../../people/brechtDR.md) raised the responsive use case — closed on small screens, open on large —
and [lwarlow](../../people/lukewarlow.md) sketched a two-button `command` workaround. No resolution was recorded.

## [openable] focus management behaviour ([openui/open-ui#1158](https://github.com/openui/open-ui/issues/1158))

The minutes record [lwarlow](../../people/lukewarlow.md) as asking whether openables should get popover's focus/tab-order
fixup; scott argued yes, citing a banner button opening a navigation panel that is a DOM sibling
of `<main>` — without tab-order restructuring keyboard users get lost. [sorvell](../../people/sorvell.md) initially voted -1
without an opt-out, worried about toast-like cases, and moved to 0 after [masonf](../../people/mfreed7.md) pointed out that
calling `showPopover()` without a source element already avoids the focus fixup.

> RESOLVED: Copy popover focus management behaviour (investigate use cases for opt-out).

([resolution](https://github.com/openui/open-ui/issues/1158#issuecomment-2722388906))

## [openable] Should openable be disallowed on certain elements? ([openui/open-ui#1159](https://github.com/openui/open-ui/issues/1159))

The minutes record scott and [masonf](../../people/mfreed7.md) as agreeing openable should be global like popover, with the
weird combinations (`<details>`, `<dialog>`, elements that also have `popover`) explicitly
specified rather than disallowed — precedent being that `showModal()` then `showPopover()`
throws. [lwarlow](../../people/lukewarlow.md) walked through the conflict cases (which API wins, what a declaratively-open
element with both attributes does); [sorvell](../../people/sorvell.md) questioned whether openable vs. popover even needs to
be two features, with [lwarlow](../../people/lukewarlow.md) defending the split on findability and focus-management
differences. scott noted the responsive use case of declaring both attributes on one element. No
resolution was recorded.

## Other topics

- [openui/open-ui#1175](https://github.com/openui/open-ui/issues/1175) — New draft of appearance:base spec.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
