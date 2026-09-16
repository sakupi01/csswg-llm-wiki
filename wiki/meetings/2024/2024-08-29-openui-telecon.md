---
date: 2024-08-29
group: openui
type: telecon
topics_count: 1
issues: [1052]
generated_by: llm
---

# Open UI CG telecon — 2024-08-29

One topic, no resolutions. Minutes recorded by the CSS meeting bot on the linked issue.
Official minutes: [2024/08/29-openui-minutes.html](https://www.w3.org/2024/08/29-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

[masonf](../../people/mfreed7.md) reported WebKit pushback on interest invokers being ill-defined for touch and floated a
UA-provided extra button (a stylable pseudo-element, shown for coarse pointers) as the tap target.
The minutes record una as pushing back hard with GitHub's hovercard-dense home page as a
counter-example — auto-injected buttons "would degrade the user experience if we cluttered up the
UI" — and as preferring author ownership of when the affordance appears; scott as insisting the
user comes first and suggesting authors may hide it but users should be able to override via a
setting; sanketj_ as warning that multi-input devices make pointer heuristics risky; and
[gregwhitworth](../../people/gregwhitworth.md) as doubting standardization of UA hover behavior would survive. [masonf](../../people/mfreed7.md) closed by
saying the feedback had shifted him toward a globally-consistent default icon rather than a
per-platform one. No resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1052#issuecomment-2318600585))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
