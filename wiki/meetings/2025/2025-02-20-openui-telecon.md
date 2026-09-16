---
date: 2025-02-20
group: openui
type: telecon
topics_count: 1
issues: [1133]
generated_by: llm
---

# Open UI CG telecon — 2025-02-20

One topic, no resolutions. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [www.w3.org/2025/02/20-openui-minutes.html](https://www.w3.org/2025/02/20-openui-minutes.html) (dated-URL convention for CG minutes).

## [Interest invokers] Keyboard inputs ([openui/open-ui#1133](https://github.com/openui/open-ui/issues/1133))

How keyboard users should show and lose interest with `interesttarget`. The minutes record
[masonf](../../people/mfreed7.md) as presenting the explainer's hotkey approach (show interest with a hotkey, lose it with
Escape, with a changed focus ring) and its discoverability downside, versus showing interest on
focus after a delay. nmn described Facebook's shipped alternative: an inert "rich tooltip"
preview shown on focus, with a hotkey to fully activate it. [keithamus](../../people/keithamus.md) questioned whether plain
text tooltips need the heavy treatment at all and whether richness could be auto-detected;
sarah6 argued browsers can't reliably detect richness and that assistive technologies would need
their own way to signal interest. The discussion converged on showing the target on focus after
a delay but forcing it inert, with a hotkey (advertised via a hint to screen readers) to remove
the inertness; [masonf](../../people/mfreed7.md) took an action to summarise in the issue. No resolution was recorded.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
