---
date: 2023-08-17
group: openui
type: telecon
topics_count: 2
issues: [637, 787]
generated_by: llm
---

# Open UI CG telecon — 2023-08-17

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/08/17-openui-minutes.html](https://www.w3.org/2023/08/17-openui-minutes.html) (dated-URL convention for CG minutes).

Both topics concern `<selectlist>` (formerly `<selectmenu>`), the precursor of the customizable
`<select>` (see [customizable select](../../features/customizable-select.md)).

## SelectMenu placeholder capability? ([openui/open-ui#637](https://github.com/openui/open-ui/issues/637))

The placeholder saga (see [2023-01-05](2023-01-05-openui-telecon.md),
[2023-03-30](2023-03-30-openui-telecon.md), [2023-04-13](2023-04-13-openui-telecon.md)) reached a
resolution. The minutes record [jarhar](../../people/josepharhar.md) as proposing to lean on what classic `<select>` already
supports — `value=""` (blocks submission under `required`), `disabled`, `selected`, and `hidden`
on `<option>` — whose combination reproduces placeholder behavior. scotto_ pressed on which
combination "is" the placeholder and asked for author guidance; [masonf](../../people/mfreed7.md)'s answer was that in this
proposal there is no placeholder concept at all, just composable attributes that also serve other
use cases (e.g. a sold-out variant rendered but disabled). [gregwhitworth](../../people/gregwhitworth.md) and [argyle](../../people/argyleink.md) found
reaching for `hidden` hacky ("it's not an option, it's a label"), and [dbaron](../../people/dbaron.md) repeated the i18n
caution against presentable text in attributes — feeding the v2 idea of a `placeholder`
attribute/element as sugar for `<option value="" disabled hidden>`, staged later to avoid
delaying the spec.

> RESOLVED: Support the value="" attribute, selected attribute, disabled attribute, and hidden attribute on option elements in selectlist. For v2, consider a placeholder attribute or element that implies <option value="" disabled hidden>.

([resolution](https://github.com/openui/open-ui/issues/637#issuecomment-1682780451))

## [selectlist] Default appearance on mobile / native fallback ([openui/open-ui#787](https://github.com/openui/open-ui/issues/787))

akeerthi's issue on how a styleable selectlist should appear on mobile, and whether UAs may fall
back to a native picker. The minutes record [masonf](../../people/mfreed7.md) as initially open to UA overrides plus
media-query defaults, but [gregwhitworth](../../people/gregwhitworth.md) strongly disagreed with any UA freedom to swap styles:
the whole point of the effort is that authors get consistent, testable rendering, with
standardized UA styles inside standardized media queries covering form factors (touch, foldables,
watches). [ntim](../../people/nt1m.md) argued the other side — developers who never test mobile would get better results
from a native picker. scotto_ made the key constraint concrete: arbitrary slotted content cannot
be "swapped" for a native select without throwing author content away, so any fallback creates
content disparity. The group agreed to go use-case driven, research component libraries, and
split the "may UAs ever fall back to native?" question into its own issue.
No resolution was recorded.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
