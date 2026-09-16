---
date: 2025-03-06
group: openui
type: telecon
topics_count: 3
issues: [1157, 1162, 1163]
generated_by: llm
---

# Open UI CG telecon — 2025-03-06

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/03/06-openui-minutes.html](https://www.w3.org/2025/03/06-openui-minutes.html) (dated-URL convention for CG minutes).

## [openable] What pseudo class should an open openable match? ([openui/open-ui#1157](https://github.com/openui/open-ui/issues/1157))

The minutes record [lwarlow](../../people/lukewarlow.md) as noting popovers deliberately don't match `:open` (to distinguish
them from dialogs), and that since `openable` is a global attribute an element could be both an
open `<details>`/`<select>` and an openable, making a bare `:open` ambiguous. [sorvell](../../people/sorvell.md) observed
that a global attribute makes disambiguation harder than a special-purpose element would.

> RESOLVED: Use `:openable-open` (name tbd) instead of `:open`

([resolution](https://github.com/openui/open-ui/issues/1157#issuecomment-2704986748))

## [openable] how should we support find in page? ([openui/open-ui#1162](https://github.com/openui/open-ui/issues/1162))

Whether closed openables should be findable by find-in-page. The minutes record [lwarlow](../../people/lukewarlow.md) as
proposing opt-in searchability via `hidden=until-found` (which would not be removed on find when
combined with openable); scott preferred not-findable-by-default, citing collapsed navigation
lists and tree-grid rows a user deliberately closed; [keithamus](../../people/keithamus.md) agreed, noting GitHub uses
`<details>` in UI chrome where substring matches should not pop things open, though
user-authored content is a counter-case. [sorvell](../../people/sorvell.md) objected that `hidden=until-found`'s
content-visibility behaviour draws a box for closed openables, which he called broken for this
use. The group leaned to not-searchable-by-default with an explicit opt-in; no resolution was
recorded.

## [openable] do we need exclusive openables? ([openui/open-ui#1163](https://github.com/openui/open-ui/issues/1163))

Whether openables need exclusive (accordion/tab-like) behaviour. The minutes record [masonf](../../people/mfreed7.md) as
supportive if it reuses the `name` attribute like exclusive `<details>`; scott relayed user
confusion with exclusive `<details>` today, where "x of y" announcements puzzle screen-reader
users; sarah6 questioned whether complex tab UIs would actually use this rather than JS, with
[lwarlow](../../people/lukewarlow.md) conceding heavyweight cases will use script but simple cases benefit. Where `name` should
live (on the openable vs. the invoking button) was left open — the minutes record scott as
expecting it on buttons and [lwarlow](../../people/lukewarlow.md) on the openable.

> RESOLVED: We should support exclusive openables via the name attribute.

([resolution](https://github.com/openui/open-ui/issues/1163#issuecomment-2704762663))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
