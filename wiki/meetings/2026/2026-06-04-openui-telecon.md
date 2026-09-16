---
date: 2026-06-04
group: openui
type: telecon
topics_count: 4
issues: [1282, 1451, 1452, 1453]
generated_by: llm
---

# Open UI CG telecon — 2026-06-04

Four topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/06/04-openui-minutes.html](https://www.w3.org/2026/06/04-openui-minutes.html) (linked from the bot's IRC log).

## [switch] Should the explainer be rewritten to support the switch attribute? ([openui/open-ui#1282](https://github.com/openui/open-ui/issues/1282))

Returning topic, with Microsoft's Andres and LeoLee exploring an implementation. The minutes
record Andres as framing the choice: a new element vs. the checkbox `switch` attribute WebKit
shipped. [gregwhitworth](../../people/gregwhitworth.md) is recorded as dissenting — willing to "fight that battle" against the
shipped attribute, citing Codepen examples the attribute cannot express, though he later accepted
a stepping-stone plan (standardize the attribute now, keep an element option open) provided
progressive enhancement works. [lwarlow](../../people/lukewarlow.md) argued the pragmatic path is to follow Safari; [dandclark](../../people/dandclark.md)
disagreed with how WebKit shipped without a finished spec but supported the attribute approach
given CSS Forms pseudo-elements; ollie pushed back on complicating markup for "frivolous SVG
animations". Internationalized text on the track was noted as a real gap
([whatwg/html#12162](https://github.com/whatwg/html/issues/12162)).

> RESOLVED: Define the switch attribute approach but also ensure that we define the pseudo elements for styling in CSS Forms and will open an issue on WHATWG on gaps for the attribute approach

([resolution](https://github.com/openui/open-ui/issues/1282#issuecomment-4625109642))

## Should `select multiple size=1` have a placeholder option? ([openui/open-ui#1453](https://github.com/openui/open-ui/issues/1453))

Follow-on from the multi-select customizable `<select>` work
(see [customizable select](../../features/customizable-select.md)). The minutes record sbender as
explaining that the recent spec change defines a placeholder option for `select multiple size=1`
that in practice only feeds validation — it is selectable alongside other options and adds no real
placeholder behavior; for multiple selects, nothing gets auto-selected, so the placeholder
algorithm never applies. [keithamus](../../people/keithamus.md) and [masonf](../../people/mfreed7.md) noted `select multiple` is rarely used and nothing
seemed objectionable; [masonf](../../people/mfreed7.md) suggested moving the question to WHATWG given how much select work is
in flight there. sbender had prototyped a CSS-based alternative, and an HTML issue already existed
([whatwg/html#12246](https://github.com/whatwg/html/issues/12246)).

> RESOLVED: this seems reasonable we should file under WHATWG as the better forum for this.

([resolution](https://github.com/openui/open-ui/issues/1453#issuecomment-4625210382))

## Other topics

- [openui/open-ui#1451](https://github.com/openui/open-ui/issues/1451) — meta triage session for the issue backlog.
- [openui/open-ui#1452](https://github.com/openui/open-ui/issues/1452) — markup and a11y mappings for navigation menus, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
