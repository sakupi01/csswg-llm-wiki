---
date: 2023-12-14
group: openui
type: telecon
topics_count: 2
issues: [897, 963]
generated_by: llm
---

# Open UI CG telecon — 2023-12-14

Two topics, four resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/12/14-openui-minutes.html](https://www.w3.org/2023/12/14-openui-minutes.html) (dated-URL convention for CG minutes).

## Further selection refinements for collapsed selectlist ([openui/open-ui#897](https://github.com/openui/open-ui/issues/897))

A keyboard-behavior follow-up for the customizable select work (see
[customizable select](../../features/customizable-select.md)), after selection stopped following
focus. The minutes record scotto_ as reporting that typeahead on a collapsed control behaved
unexpectedly in the demo, with macOS and Windows differing on when `change` fires, and asking
whether the new control must stay in line with classic `<select>` or may deviate. [masonf](../../people/mfreed7.md) argued
the new thing is a new thing — developers opt in, the old behavior is barely specified, and known
problems should not be copied; opening the listbox during typeahead both clarifies what is
happening and cleans up the event model (`input` without `change`). scotto_ added that comboboxes
firing `change` on arrow-down is a recurring accessibility-audit failure.

> RESOLVED: when doing typeahead when the listbox is closed, the listbox should open to show the newly selected option without firing a change event or committing the newly selected option

([resolution](https://github.com/openui/open-ui/issues/897#issuecomment-1856507379))

## Other topics

- [openui/open-ui#963](https://github.com/openui/open-ui/issues/963) — three resolutions on a "safe area" mechanism and developer/user-controllable delays for interest triggering, to be researched and specified, with the delay idea taken to the CSSWG ([resolutions](https://github.com/openui/open-ui/issues/963#issuecomment-1856462744)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
