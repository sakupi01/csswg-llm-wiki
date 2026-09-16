---
date: 2023-02-16
group: openui
type: telecon
topics_count: 3
issues: [77, 115, 526]
generated_by: llm
---

# Open UI CG telecon — 2023-02-16

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [w3.org/2023/02/16-openui-minutes.html](https://www.w3.org/2023/02/16-openui-minutes.html) (dated-URL convention for CG minutes).

Both detailed topics concern `<selectmenu>`, the precursor of the customizable `<select>`
(see [customizable select](../../features/customizable-select.md)).

## `<select>` naming of button and its capabilities ([openui/open-ui#77](https://github.com/openui/open-ui/issues/77))

One of Open UI's oldest select issues. The minutes record [jarhar](../../people/josepharhar.md) as ready to close it until
[masonf](../../people/mfreed7.md) raised the remaining concern: interactive content inside the selectmenu button would be
an accessibility problem, and the two parts inside it (marker and selected value) could break if
interactive content were allowed there. [jh3y](../../people/jhey.md) agreed that interactive elements inside marker and
selected-value would be odd; [masonf](../../people/mfreed7.md) noted that authors replacing the entire button already take
over managing the selected value themselves. [gregwhitworth](../../people/gregwhitworth.md) added that only a string — not
innerHTML — is copied, and that he did not want to push HTML to allow interactive content
inside buttons.

> RESOLVED: The existing behavior is ok as-is.

([resolution](https://github.com/openui/open-ui/issues/77#issuecomment-1433598979))

## [SELECT] Usecases & solution for filtering ([openui/open-ui#115](https://github.com/openui/open-ui/issues/115))

Filtering options in a selectmenu — combobox territory. The minutes record [jarhar](../../people/josepharhar.md) as noting the
early Edge demos included a combobox-like selectmenu, and [masonf](../../people/mfreed7.md) as recalling the group already
resolved v1 is a plain single select (JavaScript can approximate the rest). [gregwhitworth](../../people/gregwhitworth.md) argued
design systems treat combobox as a separate component and that surveys show combobox is the most
wished-for control. lea floated automatic browser-provided filtering once the option count grows
beyond a threshold; [jh3y](../../people/jhey.md) warned about the virtualization rabbit hole and asked for accessibility
review. The group punted filtering past v1, keeping the discussion alive under a v2-style label.

> RESOLVED: The ability to filter options should continue to be discussed, but not in the context of the "v1" <selectmenu> control.

([resolution](https://github.com/openui/open-ui/issues/115#issuecomment-1433591574))

## Other topics

- [openui/open-ui#526](https://github.com/openui/open-ui/issues/526) — "interest"-based triggering for popovers, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
