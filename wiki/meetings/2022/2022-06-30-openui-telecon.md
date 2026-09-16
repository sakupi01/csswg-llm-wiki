---
date: 2022-06-30
group: openui
type: telecon
topics_count: 2
issues: [540, 548]
generated_by: llm
---

# Open UI CG telecon — 2022-06-30

Two topics, no bot-recorded resolutions (both IRC logs end in lowercase "Resolved" lines that
the bot did not surface as resolution bullets — a participant even noted in the log that
all-caps RESOLVED is required). Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-06-30](https://www.w3.org/2022/06/30-openui-minutes.html) (dated-URL convention).

## [selectmenu] Restricting interactive content in `<selectmenu>` listbox ([openui/open-ui#540](https://github.com/openui/open-ui/issues/540))

Continuation from 2022-06-09. The minutes record [dandclark](../../people/dandclark.md) restating the goal — `<selectmenu>`
accessible by default — and proposing a dev-tools warning when interactive content appears
inside a listbox's options, since accessibility APIs expect only options and groupings there;
future ARIA work (aria-action) could later relax it. The minutes record una confirming a
dev-tools warning is "totally doable", [sarah_higley](../../people/smhigley.md) confirming the scope (inside options) and
sharing screen-reader testing where nested buttons mostly degrade rather than break — except
VoiceOver, which could not reach them at all, per [scotto](../../people/scottaohara.md)'s macOS/iOS testing. The scribe
recorded a resolution adopting the warning approach (with content outside options left to be
decided); it does not appear in the resolutions index because it was not recorded as a bot
resolution bullet. Part of the
[customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/540#issuecomment-1171554379))

## [selectmenu] Method to change arrow icon? ([openui/open-ui#548](https://github.com/openui/open-ui/issues/548))

The minutes record hdv, who filed the issue after trying to rebuild a production select,
asking for a way to change the button's dropdown arrow. The minutes record [scotto](../../people/scottaohara.md) strongly
opposing a `::marker`-style pseudo (in details/summary the marker leaks into the accessible
name) and favoring a slot; [dandclark](../../people/dandclark.md) agreed a slot is simplest; [masonf](../../people/mfreed7.md), [chrishtr](../../people/chrishtr.md), [JonathanNeal](../../people/jonathanneal.md)
and [tantek](../../people/tantek.md) pushed to *also* expose the icon via CSS `::part()`, since resizing/recoloring via
CSS covers most use cases (una). The scribe recorded a resolution to add a slot around the
default arrow icon, also exposed as a CSS `::part()`; it does not appear in the resolutions
index because it was not recorded as a bot resolution bullet (the slot was named "marker" on
2022-09-29). Part of the [customizable select](../../features/customizable-select.md) history.

([discussion](https://github.com/openui/open-ui/issues/548#issuecomment-1171536146))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
