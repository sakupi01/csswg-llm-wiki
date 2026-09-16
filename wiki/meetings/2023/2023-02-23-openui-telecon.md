---
date: 2023-02-23
group: openui
type: telecon
topics_count: 2
issues: [143, 276]
generated_by: llm
---

# Open UI CG telecon — 2023-02-23

Two topics, one resolution captured by the bot. Minutes recorded by the CSS meeting bot on the
linked issues.
Official minutes: [w3.org/2023/02/23-openui-minutes.html](https://www.w3.org/2023/02/23-openui-minutes.html) (dated-URL convention for CG minutes).

Both topics concern `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## `<select>` anatomy seems Windows-centric ([openui/open-ui#143](https://github.com/openui/open-ui/issues/143))

Whether the "listbox" part name is too Windows-centric, since on macOS, iOS and Android the
native control is not a listbox. The minutes record joey ([jarhar](../../people/josepharhar.md)) as preferring to keep the name,
and [gregwhitworth](../../people/gregwhitworth.md) as citing anatomy research: "listbox" is a very common component name in the
wild, independent of whether it pops up. [sarah_h](../../people/smhigley.md) is recorded as the main voice of caution —
listbox is an ARIA role name, the correct role differs per platform, and the role for
`<select multiple>` may change (possibly to menu), so tying the part name to a role could
confuse; [scotto](../../people/scottaohara.md) was similarly ambivalent given arbitrary content is allowed. [dbaron](../../people/dbaron.md) relayed the
view that multiple selects should behave more like checkbox groups. [jhey](../../people/jhey.md) and [masonf](../../people/mfreed7.md) argued
developers think of it as a list of options and "listbox" is what they expect; [sarah_h](../../people/smhigley.md) accepted
the name as understandable enough separate from ARIA.

> RESOLVED: Keep the part name "listbox" instead of changing it

([resolution](https://github.com/openui/open-ui/issues/143#issuecomment-1442324035))

## Change URL parameter without Javascript ([openui/open-ui#276](https://github.com/openui/open-ui/issues/276))

A request for selectmenu options to change a URL query parameter and reload the page without
JavaScript. The minutes record joey ([jarhar](../../people/josepharhar.md)) as calling it out of scope ([jhey](../../people/jhey.md) and lea agreed on
the issue), with [masonf](../../people/mfreed7.md) noting it is a single line of JS and [dbaron](../../people/dbaron.md) supporting out-of-scope at
least for v1. The group agreed to close and decline; the outcome was typed as
"Resolved: This is out of scope and close the issue" (lower-case, so not captured in the bot's
resolution summary — see the [discussion comment](https://github.com/openui/open-ui/issues/276#issuecomment-1442304389)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
