---
date: 2024-12-19
group: openui
type: telecon
topics_count: 3
issues: [1052, 1130, 1133]
generated_by: llm
---

# Open UI CG telecon — 2024-12-19

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/12/19-openui-minutes.html](https://www.w3.org/2024/12/19-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

[masonf](../../people/mfreed7.md) presented a new synthesis for the long-press model resolved on
[2024-11-07](2024-11-07-openui-telecon.md): on long-press the hovercard is invoked *and* the UA
menu appears keyboard-style at the screen edge, with CSS environment variables telling the
developer which area stays unobscured. The minutes record [brecht_dr](../../people/brechtDR.md) as worried this is one more
thing developers must learn and test on-device, wishing for a good default, and scott2 as pressing
for at least a UA guarantee that interest-invoked content stays within the viewport — [masonf](../../people/mfreed7.md)
recalling that UA defaults were "roundly rejected" for customizable select, and converging on a
possible pseudo-class for popovers invoked this way. [masonf](../../people/mfreed7.md) deferred resolving pending more
thought. No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1052#issuecomment-2555629033))

## [Interest invokers] Keyboard inputs ([openui/open-ui#1133](https://github.com/openui/open-ui/issues/1133))

The keyboard leg: [masonf](../../people/mfreed7.md) recapped that focus-as-activation had been rejected (tabbing through a
document would fire interest everywhere), so a key combination is needed — plus discoverability.
The minutes record scott2 as wanting a UA-default visual indicator distinct from the focus ring
(an information icon having been "universally shunned" earlier) and noting a modifier key is needed
so arrow-key scrolling survives, and [brecht_dr](../../people/brechtDR.md) as preferring a customizable pseudo-element
indicator over a subtle outline change. bkardell_ preferred on-by-default with only limited
customization.

> RESOLVED: add a UA stylesheet rule that indicates (when focused) that interesttarget elements are special. No need for anything more, e.g. a popup describing how to activate it. This indicator can't just be a change of the :focus outline style, because developers commonly override that.

([resolution](https://github.com/openui/open-ui/issues/1133#issuecomment-2555808408))

## Other topics

- [openui/open-ui#1130](https://github.com/openui/open-ui/issues/1130) — meter element states,
  continuing from the 2024-12-12 pseudo-class resolution
  ([resolution](https://github.com/openui/open-ui/issues/1130#issuecomment-2555588318)):

> RESOLVED: we think it should include a term that as unambiguously as possible describes that this is some kind of area, region, range, etc., but not pick those exact words.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
