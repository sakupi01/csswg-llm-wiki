---
date: 2026-04-09
group: openui
type: telecon
topics_count: 2
issues: [1319, 1425]
generated_by: llm
---

# Open UI CG telecon — 2026-04-09

Two topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2026/04/09-openui-minutes.html](https://www.w3.org/2026/04/09-openui-minutes.html) (dated-URL convention for CG minutes).

## [combobox] supporting autocomplete use cases in aria practices guide ([openui/open-ui#1319](https://github.com/openui/open-ui/issues/1319))

Returning topic on whether comboboxes should copy the highlighted option into the input as the
user arrows (see [customizable select](../../features/customizable-select.md)). The minutes
record [jarhar](../../people/josepharhar.md) as reporting his survey: Wikipedia and google.com do this, but GitHub's search and
every React combobox component he found do not. sarah added that major search engines don't even
use `input type=search`, and search fields in Gmail/Outlook/Slack/Discord/Teams don't autocomplete
on arrow — so keying the behavior on `type` would be "too magic". Side threads covered datalist
styling ([brecht_dr](../../people/brechtDR.md)), textarea + datalist for canned messages ([lwarlow](../../people/lukewarlow.md), split to
[openui/open-ui#1432](https://github.com/openui/open-ui/issues/1432)), and ghost text (sarah).
The group chose not to add an API for now, noting an attribute can be added later.

> RESOLVED: dont provide an api to automatically copy the active option into the input on comboboxes unless there is more feedback that we need it

([resolution](https://github.com/openui/open-ui/issues/1319#issuecomment-4216677726))

## Base appearance color input questions ([openui/open-ui#1425](https://github.com/openui/open-ui/issues/1425))

Review of the revised `appearance: base` design for `<input type=color>` from the joint task
force. The minutes record [lwarlow](../../people/lukewarlow.md) as presenting the new proposal — the color swatch fills the
whole element rather than sitting inside padding, with a 24×24px minimum for WCAG touch-target
sizing — and asking whether it should be rounded, square, or circular. [keithamus](../../people/keithamus.md) is recorded as
applying the rule from the base `<select>` discussion (border-radius signals destructive buttons,
so no radius here). Remaining polish items were noted: a stray grey pixel (likely a gradient
artifact), baseline alignment of the swatch with surrounding text, and minimum sizing.

> RESOLVED: no issues for now. After prototyping, we can examine it further. More work to do on the grey pixel, minimum sizing, and baseline alignment.

([resolution](https://github.com/openui/open-ui/issues/1425#issuecomment-4216457047))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
