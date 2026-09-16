---
date: 2024-05-23
group: openui
type: telecon
topics_count: 4
issues: [863, 998, 1052, 1055]
generated_by: llm
---

# Open UI CG telecon — 2024-05-23

Four topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/05/23-openui-minutes.html](https://www.w3.org/2024/05/23-openui-minutes.html)
(dated-URL convention for CG minutes).

## selectlist: Should the "checked" option have a checkmark next to it? ([openui/open-ui#863](https://github.com/openui/open-ui/issues/863))

Continuing from [2024-05-09](2024-05-09-openui-telecon.md), the group converged on a default
checkmark for the [customizable select](../../features/customizable-select.md) that is easy to
remove. The minutes record [keithamus](../../people/keithamus.md) as asking which selector authors would use
(`option:checked::marker`), Luke as noting `::marker` content is easy to replace or hide, hdv as
raising that `content` text is normally read by screen readers (Luke pointing to the trailing-slash
alternative-text syntax as the fix), and [masonf](../../people/mfreed7.md) as preferring a Unicode character over SVG to avoid
bikeshedding — [flackr](../../people/flackr.md) adding it would follow OS font conventions.

> RESOLVED: support checkmark next to checked option, implemented via the content property on the ::marker pseudo element. The UA should set a Unicode character by default, which isn't read out by screen reader.

([resolution](https://github.com/openui/open-ui/issues/863#issuecomment-2127775634))

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

Returning from [2024-05-16](2024-05-16-openui-telecon.md), the group stepped back from picking a
gesture and pinned the principle instead. The minutes record [masonf](../../people/mfreed7.md) as proposing that keyboard and
mouse behavior be standardized while other modalities only require "a way" chosen by the UA, [flackr](../../people/flackr.md)
as noting long-press is already overloaded (context menus, drag-and-drop) but interest could work
if non-destructive, and [dbaron](../../people/dbaron.md) as supplying the final user-centric wording after Luke found "any
input modality" ambiguous.

> RESOLVED: the spec should say that any user "must" be able to show interest via some input modality.

([resolution](https://github.com/openui/open-ui/issues/1052#issuecomment-2127821037))

## Explore `<input>` Element as a child within `<select>` for Combobox ([openui/open-ui#1055](https://github.com/openui/open-ui/issues/1055))

Sudheer asked whether a text `<input>` should live inside the new
[customizable select](../../features/customizable-select.md) to make it a combobox. The minutes
record Luke as relaying that an input directly inside select is almost certainly not web-compatible
(the parser would close the select) while noting searchable selects are a top author demand, [masonf](../../people/mfreed7.md)
as arguing select and combobox are semantically distinct ARIA roles and interactive content inside
a select's button is bad for accessibility, and [brecht_dr](../../people/brechtDR.md) as demonstrating in a codepen that an
input inside a datalist breaks. Luke flagged the filterable-select question as unresolved follow-up.

> RESOLVED: the input should not be allowed within the select. The combobox should be implemented as a new element or as part of e.g. input/datalist.

([resolution](https://github.com/openui/open-ui/issues/1055#issuecomment-2127802432))

## Other topics

- [openui/open-ui#998](https://github.com/openui/open-ui/issues/998) — naming bikeshed for the
  invoker attributes, discussed without a recorded resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
