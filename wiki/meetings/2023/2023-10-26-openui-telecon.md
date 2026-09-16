---
date: 2023-10-26
group: openui
type: telecon
topics_count: 4
issues: [743, 881, 896, 900]
generated_by: llm
---

# Open UI CG telecon — 2023-10-26

Four topics, three resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/10/26-openui-minutes.html](https://www.w3.org/2023/10/26-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics concern `<selectlist>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## selectlist: customizing the default button's marker is weird ([openui/open-ui#881](https://github.com/openui/open-ui/issues/881))

The minutes record [jarhar](../../people/josepharhar.md) as reporting that the `::marker` chevron is hard to manipulate because
it is implemented as an SVG data-URL — setting `color` does nothing — and asking whether the
marker should exist at all. Luke_W's gut said keep the default chevron in the button but drop the
pseudo; [masonf](../../people/mfreed7.md) disagreed strongly, preferring the SVG be replaced with a Unicode character so
basic customisation (colour) just works, with full replacement left to authors who swap the
button. [dbaron](../../people/dbaron.md) offered `mask-image` and SVG context-color as alternatives (with the caveat
currentcolor fails on data-URLs, per [zcorpan](../../people/zcorpan.md)), and warned a Unicode glyph varies up to 3× in size
across fonts; [argyle](../../people/argyleink.md) advocated platform variety over normalisation. scotto_ stressed the default
UA chevron matters for plain-HTML users and high-contrast themes. [gregwhitworth](../../people/gregwhitworth.md) raised the deeper
interop question — pixel-perfect vs merely dimensional consistency across UAs — which [masonf](../../people/mfreed7.md)
split into a separate standardised-styles issue.

> RESOLVED: Keep ::marker pseudo element in selectlist. Further investigate exact implementation.

([resolution](https://github.com/openui/open-ui/issues/881#issuecomment-1781648738))

## Design the `<listbox>` element ([openui/open-ui#896](https://github.com/openui/open-ui/issues/896))

The minutes record [jarhar](../../people/josepharhar.md) as proposing to design `<listbox>` as a standalone element (replacing
the old `slot=listbox`), since problems found in selectlist would apply standalone anyway.
[gregwhitworth](../../people/gregwhitworth.md) connected it to the combobox explainer work; [flackr](../../people/flackr.md) suggested listbox as the
visualisation with selectlist as the data container. [masonf](../../people/mfreed7.md) supported an explainer but registered
a fear on the record: selectlist is "the largest thing to hit HTML maybe ever" and a giant
listbox project must not delay it by years — the group should keep the flexibility to retreat to
a selectlist-only listbox. Luke_W countered that not speccing standalone behavior invites future
breaking changes; [argyle](../../people/argyleink.md) enumerated the open questions of a detached listbox (focus, keyboard,
options without a target); [masonf](../../people/mfreed7.md) noted `<datalist>` (which already "renders nothing") remains
the backup plan. scotto_ recalled WHATWG's aversion to duplicate elements but saw real problems
being solved.

> RESOLVED: Create an explainer for and incubate the design of a listbox element

([resolution](https://github.com/openui/open-ui/issues/896#issuecomment-1781689460))

## Other topics

- [openui/open-ui#743](https://github.com/openui/open-ui/issues/743) — resolved that slots should wrap parts where the intent is whole-part replacement ([resolution](https://github.com/openui/open-ui/issues/743#issuecomment-1781593051)).
- [openui/open-ui#900](https://github.com/openui/open-ui/issues/900) — naming requirements for custom invoker actions, discussed without resolution this day.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
