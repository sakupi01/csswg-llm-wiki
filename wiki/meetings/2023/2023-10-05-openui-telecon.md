---
date: 2023-10-05
group: openui
type: telecon
topics_count: 4
issues: [827, 845, 849, 854]
generated_by: llm
---

# Open UI CG telecon — 2023-10-05

Four topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/10/05-openui-minutes.html](https://www.w3.org/2023/10/05-openui-minutes.html) (dated-URL convention for CG minutes).

## selectlist: pseudo-class to style the selected option ([openui/open-ui#827](https://github.com/openui/open-ui/issues/827))

A styling hook for `<selectlist>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)). The minutes record lukew as
observing the existing `:checked` pseudo-class already works on options — including in
`select[multiple]` and current selectlist prototypes — questioning whether a new `:selected`
pseudo is needed. scotto_ unpacked the ARIA distinction: in a single select the selected option
is the focused option, but in a multiselect selection and focus diverge, and listbox selection
states are handled inconsistently across browsers and assistive technologies. sarah_h_
recommended checked for multiselect and noted that since selectlist's selection no longer follows
focus ([jarhar](../../people/josepharhar.md) had removed that), checked could serve everywhere; [kizu](../../people/kizu.md) added the wrinkle of
submitted vs not-yet-submitted states. [masonf](../../people/mfreed7.md) judged a duplicate pseudo unlikely to fly in
CSSWG/WHATWG.

> RESOLVED: The :checked pseudo should work for selectlist. Wait to think about :selected until we're discussing <selectlist multiple>.

([resolution](https://github.com/openui/open-ui/issues/827#issuecomment-1749437642))

## Other topics

- [openui/open-ui#849](https://github.com/openui/open-ui/issues/849) — responsive popovers to inline content: resolved this needs JavaScript/`display` overrides; author guidance to be added ([resolution](https://github.com/openui/open-ui/issues/849#issuecomment-1749460397)).
- [openui/open-ui#845](https://github.com/openui/open-ui/issues/845) — improving the design-system anatomy JSON schema, discussed without resolution this day.
- [openui/open-ui#854](https://github.com/openui/open-ui/issues/854) — call for research on tooltip nestability.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
