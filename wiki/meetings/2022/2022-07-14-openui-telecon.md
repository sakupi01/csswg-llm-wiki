---
date: 2022-07-14
group: openui
type: telecon
topics_count: 3
issues: [382, 420, 557]
generated_by: llm
---

# Open UI CG telecon — 2022-07-14

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-07-14](https://www.w3.org/2022/07/14-openui-minutes.html) (dated-URL convention).

## [Popup] Triggering element support: buttons, text inputs, etc. ([openui/open-ui#420](https://github.com/openui/open-ui/issues/420))

Revisiting the 2022-06-09 resolution that had allowed invoking attributes on text inputs. The
minutes record [masonf](../../people/mfreed7.md) explaining the input case is trickier than buttons — what should happen for
keyboard vs mouse vs touch users, and browsers already overlay their own autofill/datalist UI on
inputs. The minutes record [bkardell](../../people/bkardell.md) and [scotto](../../people/scottaohara.md) describing conflicts with existing UA popups
(password managers, Edge autocomplete that overrides the `autocomplete` attribute), and
[gregwhitworth](../../people/gregwhitworth.md) repeatedly asking why the capability should be prohibited at all, before conceding
the use cases are varied enough to need more research. The group scaled the earlier decision
back to buttons only.

> RESOLVED: only support invoking attributes on buttons (as described in the issue).

([resolution](https://github.com/openui/open-ui/issues/420#issuecomment-1184841802))

## Other topics

- [openui/open-ui#382](https://github.com/openui/open-ui/issues/382) — resolved to rename `togglepopup`/`showpopup`/`hidepopup` to `popuptoggletarget`/`popupshowtarget`/`popuphidetarget` with reflected IDL properties ([resolution](https://github.com/openui/open-ui/issues/382#issuecomment-1184773425)).
- [openui/open-ui#557](https://github.com/openui/open-ui/issues/557) — top layer pseudo class questions.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
