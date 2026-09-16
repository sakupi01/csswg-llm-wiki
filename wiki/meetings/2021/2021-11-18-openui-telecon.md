---
date: 2021-11-18
group: openui
type: telecon
topics_count: 2
issues: [409, 410]
generated_by: llm
---

# Open UI CG telecon — 2021-11-18

Two topics, one resolution. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2021-11-18](https://www.w3.org/2021/11/18-openui-minutes.html).

## [Popup] popup="" is supported on `<button type=submit>` but not `<input type=submit>` ([openui/open-ui#409](https://github.com/openui/open-ui/issues/409))

The minutes record [masonf](../../people/mfreed7.md) arguing the declarative `popup` triggering attribute should work from
any button-like element that is not in the submit or reset state, and [domenic](../../people/domenic.md) pointing out that
image buttons behave like submit buttons (they submit the form with coordinates), so they must be
excluded too. The minutes record briankardell asking about buttons with a form owner and
[scottohara](../../people/scottaohara.md) asking whether support should be explicit to `type=button`; the resolution text was
iterated live in IRC to cover all form-submitting variants.

> RESOLVED: <input type=button> should be supported for the popup attribute, except for submit, reset, and other buttons that would submit or reset a form.

([resolution](https://github.com/openui/open-ui/issues/409#issuecomment-973176547))

## Other topics

- [openui/open-ui#410](https://github.com/openui/open-ui/issues/410) — what the semantic role for `<popup>` should be.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
