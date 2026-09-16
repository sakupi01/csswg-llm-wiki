---
date: 2024-11-07
group: openui
type: telecon
topics_count: 2
issues: [1052, 1114]
generated_by: llm
---

# Open UI CG telecon — 2024-11-07

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2024/11/07-openui-minutes.html](https://www.w3.org/2024/11/07-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

[masonf](../../people/mfreed7.md) brought Google-designed mockups reducing the touch question to two candidates: single-tap
shows the hovercard (with extra affordances to reach the context menu), or long-press. The minutes
record nmn as arguing single-tap adds friction to tap-and-go users and duplicates what `click`
already offers, [sorvell](../../people/sorvell.md) as warning against messing with links ("how many times have we run into
links that aren't links?") and noting iOS previews have trained users that they are *not*
interactive — wanting Apple HIG / Material Design input before shipping — and [flackr](../../people/flackr.md) as making his
"weekly callout" that long-press is already overloaded by text selection and drag-and-drop. The
group resolved only the elimination: single-tap is out.

> RESOLVED: The activation mode for touch needs to be long-press, not single-tap.

([resolution](https://github.com/openui/open-ui/issues/1052#issuecomment-2463106664))

## Other topics

- [openui/open-ui#1114](https://github.com/openui/open-ui/issues/1114) — the utility of the
  `popover=hint` feature
  ([resolution](https://github.com/openui/open-ui/issues/1114#issuecomment-2463048194)):

> RESOLVED: popover=hint is a useful and desirable feature on its own, separate from interesttarget.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
