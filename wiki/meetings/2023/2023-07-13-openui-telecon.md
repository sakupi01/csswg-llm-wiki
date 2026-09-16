---
date: 2023-07-13
group: openui
type: telecon
topics_count: 3
issues: [767, 773, 778]
generated_by: llm
---

# Open UI CG telecon — 2023-07-13

Three topics, no resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/07/13-openui-minutes.html](https://www.w3.org/2023/07/13-openui-minutes.html) (dated-URL convention for CG minutes).

## Rename `selectmenu` to `selectbox` ([openui/open-ui#773](https://github.com/openui/open-ui/issues/773))

The naming debate that would eventually produce `<selectlist>` — a step in the history of the
customizable `<select>` (see [customizable select](../../features/customizable-select.md)). The
minutes record [masonf](../../people/mfreed7.md) as presenting the problem: "menu" in `selectmenu` invites confusion with
action menus, which the control is explicitly not for. [scotto](../../people/scottaohara.md) backed the rename on semantic
grounds — the control opens a listbox of options, and options vs menuitems carry very different
associations in screen readers. una worried "box" is so generic it loses the useful limitation
the "menu" name implied, and floated `selectlist`; [brecht_dr](../../people/brechtDR.md) also found "box" too generic.
[Westbrook](../../people/westbrook.md) noted Adobe Spectrum calls the pattern a "picker" and [gregwhitworth](../../people/gregwhitworth.md) that Salesforce
says "picklist". The group deferred the rename to async discussion. Separately, [annevk](../../people/annevk.md) (newly
attending) asked where it is explained why `<select>` itself cannot be extended; [gregwhitworth](../../people/gregwhitworth.md)
and [dandclark](../../people/dandclark.md) cited security concerns with arbitrary option content, styleability, and parser
behavior, and the group leaned toward writing a one-pager. No resolution was recorded.

## Other topics

- [openui/open-ui#767](https://github.com/openui/open-ui/issues/767) — bikeshedding a `popovertargetaction` value for hover/focus triggering, discussed without resolution.
- [openui/open-ui#778](https://github.com/openui/open-ui/issues/778) — exclusive-accordion behavior in disconnected subtrees, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
