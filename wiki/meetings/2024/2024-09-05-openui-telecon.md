---
date: 2024-09-05
group: openui
type: telecon
topics_count: 2
issues: [1052, 1086]
generated_by: llm
---

# Open UI CG telecon — 2024-09-05

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/09/05-openui-minutes.html](https://www.w3.org/2024/09/05-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

With the extra-button idea rejected on [2024-08-29](2024-08-29-openui-telecon.md) (visual clutter,
extra tab stops), [masonf](../../people/mfreed7.md) proposed speccing long-press: where a context menu would appear, its first
item shows interest. The minutes record [flackr](../../people/flackr.md) as noting Android buttons already show tooltips on
long-press so buttons could just show the popover directly; [keithamus](../../people/keithamus.md) as challenging the "we can't
co-opt long-press" premise — native apps show a context menu *and* a preview together, and the web
should match native's power; una as finding precedent in Facebook's custom long-press menu;
and scott as warning that long-press is genuinely hard for users with motor disabilities and
screen-reader users, favoring an actions-available context menu for TalkBack. [keithamus](../../people/keithamus.md) also framed
focus as the interest modality for D-pads and eye tracking. No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1052#issuecomment-2332399460))

## [select] removing pseudo element for fallback button ([openui/open-ui#1086](https://github.com/openui/open-ui/issues/1086))

Acting on Apple feedback, [jarhar](../../people/josepharhar.md) proposed deleting the fallback UA button and its
`::select-fallback-button` pseudo from the [customizable
select](../../features/customizable-select.md): authors style the button by styling the `<select>`
itself, with no magic UA rendering. The minutes record [masonf](../../people/mfreed7.md) as hearing "no downsides", sanketj_
as checking the split-button use case is unaffected, and scott as raising how authors would style
customized versus uncustomized selects (answered with `@supports`/style queries) and questioning
whether diverging keyboard behavior between the two modes still makes sense now that it is one
element — [jarhar](../../people/josepharhar.md) noting [annevk](../../people/annevk.md) had objected to non-platform keyboard conventions.

> RESOLVED: remove ::select-fallback-button and the fallback UA button element in the UA shadowroot of select

([resolution](https://github.com/openui/open-ui/issues/1086#issuecomment-2332603903))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
