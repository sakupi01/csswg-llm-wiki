---
date: 2026-04-30
group: openui
type: telecon
topics_count: 4
issues: [1163, 1436, 1438, 1439]
generated_by: llm
---

# Open UI CG telecon — 2026-04-30

Four topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/04/30-openui-minutes.html](https://www.w3.org/2026/04/30-openui-minutes.html) (dated-URL convention for CG minutes).

## [openable] do we need exclusive openables? ([openui/open-ui#1163](https://github.com/openui/open-ui/issues/1163))

Revisiting last year's resolution to use the `name` attribute for exclusive openables (mirroring
the exclusive-accordion `name` on `<details>`). The minutes record [lwarlow](../../people/lukewarlow.md) as relaying pushback:
`name` would have to become a global attribute with IDL, and it already means something on forms,
iframes and other elements. [keithamus](../../people/keithamus.md) is recorded as defending `name` — its existing meanings map
well, and elements where it clashes "are broken anyway" — with [masonf](../../people/mfreed7.md) and [bkardell](../../people/bkardell.md) agreeing, and
[bkardell](../../people/bkardell.md) predicting WHATWG editors would say the same. scott cautioned that changing an iframe's
role has made iframe content inaccessible in past testing, so openable-on-iframe is best avoided
via a wrapper div.

> RESOLVED: Maintain 'name' attribute as our resolved solution.

([resolution](https://github.com/openui/open-ui/issues/1163#issuecomment-4355031104))

## Which option should be focused when tabbing and shift+tabbing into a listbox select element? ([openui/open-ui#1436](https://github.com/openui/open-ui/issues/1436))

Keyboard behavior for the listbox form of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
describing the current asymmetry — tab enters at the first option, shift+tab at the last. [lwarlow](../../people/lukewarlow.md)
and scott are recorded as favoring "memory" keyed to the *selected* option (not the last-focused
one, which no longer makes sense once selection doesn't follow focus); Jacques pressed the
asymmetry problem (shift+tab then tab lands you somewhere else), and [jarhar](../../people/josepharhar.md) noted Chrome, Edge
and Windows all enter at the first option, with several issue commenters preferring symmetry.
[sorvell](../../people/sorvell.md) later objected on the issue that the non-base select remembers the last focused item
([comment](https://github.com/openui/open-ui/issues/1436#issuecomment-4355399553)).

> RESOLVED: make tabbing and shift+tabbing symmetrical so that the first option gets focused. if there is a selected option, then focus the first selected option.

([resolution](https://github.com/openui/open-ui/issues/1436#issuecomment-4355152090))

## Other topics

- [openui/open-ui#1438](https://github.com/openui/open-ui/issues/1438) — the group resolved that pressing tab on a `<menuitem>` moves focus past the entire menubar/menulist tree ([resolution](https://github.com/openui/open-ui/issues/1438#issuecomment-4355242573)).
- [openui/open-ui#1439](https://github.com/openui/open-ui/issues/1439) — resolved how keyboard focus moves into submenus (space/enter/down/right focus the first menuitem, arrow up the last) ([resolution](https://github.com/openui/open-ui/issues/1439#issuecomment-4355406361)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
