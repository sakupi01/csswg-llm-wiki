---
date: 2025-10-30
group: openui
type: telecon
topics_count: 3
issues: [847, 1273, 1312]
generated_by: llm
---

# Open UI CG telecon — 2025-10-30

Three topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/10/30-openui-minutes.html](https://www.w3.org/2025/10/30-openui-minutes.html) (dated-URL convention for CG minutes).

## How to make an accessible searchable "select" list? ([openui/open-ui#847](https://github.com/openui/open-ui/issues/847))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). Follow-up on filtering behaviour
for the sibling input-plus-select design. The minutes record sarah as arguing everyone wants
different filtering logic (capitalization, matching fields), suggesting a author-supplied matcher
function whose rendering the component handles; [gregwhitworth](../../people/gregwhitworth.md) distinguished filtering from
searching (find-and-highlight) and wanted a 90%-case default with a bail-out; scott warned that
without an attribute naming the searchable term, rich option content (image alt text?) makes
matching ambiguous; [lwarlow](../../people/lukewarlow.md) worried about synchronous author JS running per keystroke; [masonf](../../people/mfreed7.md)
floated attaching a promise to a cancellable beforefilter event to keep debounced fetches safe.
[jarhar](../../people/josepharhar.md) closed by moving search/filter design to a separate issue ([openui/open-ui#931](https://github.com/openui/open-ui/issues/931)). No new resolution was
recorded.

## Some thoughts and questions about combobox ([openui/open-ui#1273](https://github.com/openui/open-ui/issues/1273))

Related to the customizable `<select>` family of form-control work — see
[customizable select](../../features/customizable-select.md). [jarhar](../../people/josepharhar.md) asked for the group's
blessing to rewrite the combobox explainer around `<input>` + `<datalist>` with
`appearance: base`. The minutes record [gregwhitworth](../../people/gregwhitworth.md) as unenthusiastic ("I want to grab off the
shelf what I want"), [masonf](../../people/mfreed7.md) as won over by the customizable-select precedent, and sarah as
raising serious accessibility problems with the datalist pattern — users need an explicit
open/close affordance beyond typing, which today's datalist lacks and which may not be solvable —
while [lwarlow](../../people/lukewarlow.md) called existing datalist implementations a nightmare of divergence but was open if
behaviour can change under the new opt-in. No resolution was recorded.

## [menu] Should an event be fired when a `<menuitem>` is selected? Which event? ([openui/open-ui#1312](https://github.com/openui/open-ui/issues/1312))

Menus (and Mac-style native selects) let a user mousedown on the trigger, drag to an item, and
release — but a plain `click` event would fire on the common ancestor, not the item. The minutes
record [masonf](../../people/mfreed7.md) as preferring to redefine `click` to work for this case rather than mint a new
event; [lwarlow](../../people/lukewarlow.md) agreed (joking about resurrecting DOMActivate) and noted a new event was unlikely
to fly at WHATWG; sarah and domfarolino asked about preventDefault and event-timing semantics,
which [masonf](../../people/mfreed7.md) will pin down with tests. The resolution also applies the fix to customizable
`<select>` — see [customizable select](../../features/customizable-select.md).

> RESOLVED: just make `click` work in this case, and for customizable-<select> also

([resolution](https://github.com/openui/open-ui/issues/1312#issuecomment-3469585173))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
