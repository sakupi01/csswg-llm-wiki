---
date: 2026-03-19
group: openui
type: telecon
topics_count: 3
issues: [1319, 1389, 1414]
generated_by: llm
---

# Open UI CG telecon — 2026-03-19

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/03/19-openui-minutes.html](https://www.w3.org/2026/03/19-openui-minutes.html) (dated-URL convention for CG minutes).

## [combobox] supporting autocomplete use cases in aria practices guide ([openui/open-ui#1319](https://github.com/openui/open-ui/issues/1319))

On combobox behavior for the customizable `<select>` family
(see [customizable select](../../features/customizable-select.md)). The minutes record [jarhar](../../people/josepharhar.md) as
asking whether arrowing through combobox options should commit the highlighted option's text into
the input, as Wikipedia's search does. [lwarlow](../../people/lukewarlow.md) is recorded as opposing value changes on arrow
(Escape should be able to leave the value untouched), and [masonf](../../people/mfreed7.md) noted Wikipedia only shows a
visual placeholder rather than changing the real value — otherwise filtering would collapse to
one option. Jacques recounted enjoying the committing behavior for autocompleting long strings;
sarah and scott0 suggested search fields with popups may deserve different semantics than
comboboxes (HTML-AAM currently maps any `list` attribute to role combobox). [jarhar](../../people/josepharhar.md) closed by
saying he may prototype an `input type=search` variant. No resolution was recorded.

([discussion](https://github.com/openui/open-ui/issues/1319#issuecomment-4092585535))

## [toolbar] Should radio inputs behave differently inside of a toolbar? ([openui/open-ui#1414](https://github.com/openui/open-ui/issues/1414))

The minutes record [lwarlow](../../people/lukewarlow.md) as noting radio groups in toolbars usually do not use
selection-follows-focus, and citing text-alignment buttons as the canonical case. scott0 is
recorded as initially skeptical that anyone nests radios in toolbars — and as objecting to radios
"magically" behaving differently by context, preferring an explicit opt-in — while sarah reported
Fluent ships a dedicated toolbar radio button precisely because native radios break there, and
argued the semantics should stay radios rather than press buttons. Jacques leaned toward locking
the pattern down unless a real need exists. The group agreed the pattern is real and worth
exploring, with specifics (opt-in mechanism vs. heuristics) left open.

> RESOLVED: this behavior (radio groups inside a toolbar) is a real one, which we should explore further.

([resolution](https://github.com/openui/open-ui/issues/1414#issuecomment-4092433405))

## Other topics

- [openui/open-ui#1389](https://github.com/openui/open-ui/issues/1389) — after experimenting with automated minuting, the group resolved to "go back to manual (human) scribing" and collect improvement suggestions on the issue ([resolution](https://github.com/openui/open-ui/issues/1389#issuecomment-4092273314)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
