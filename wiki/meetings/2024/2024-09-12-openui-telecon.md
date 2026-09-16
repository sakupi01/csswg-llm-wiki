---
date: 2024-09-12
group: openui
type: telecon
topics_count: 3
issues: [1052, 1087, 1088]
generated_by: llm
---

# Open UI CG telecon — 2024-09-12

Three topics, no resolutions recorded on the day. Minutes recorded by the CSS meeting bot on the
linked issues. Official minutes:
[2024/09/12-openui-minutes.html](https://www.w3.org/2024/09/12-openui-minutes.html)
(dated-URL convention for CG minutes).

## [interest invokers] Touch inputs ([openui/open-ui#1052](https://github.com/openui/open-ui/issues/1052))

The keyboard leg of the interest question, headed for TPAC. [masonf](../../people/mfreed7.md) reported that using focus itself
as the trigger is noisy for assistive-technology users and floated a hotkey with a discoverability
hint. The minutes record [keithamus](../../people/keithamus.md) as recounting GitHub's iterations (focus was distracting,
`aria-describedby` announcements annoyed users; a Ctrl+? cheatsheet remains) and urging the group
not to run away from a hard problem; [scotto](../../people/scottaohara.md) as describing Microsoft as "hot-key happy" with every
product team inventing its own keys for lack of a standard; [flackr](../../people/flackr.md) as cautioning against
standardizing GitHub's one-off and pointing to access keys' patchy history; and bkardell_ as
recalling the 2018 "interest" proposal (moving interest without moving focus) as prior art.
[gregwhitworth](../../people/gregwhitworth.md) suggested speccing "interest" itself, backed by eye/mouse-correlation research. No
resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1052#issuecomment-2346988232))

## [select] keyboard behavior ([openui/open-ui#1087](https://github.com/openui/open-ui/issues/1087))

[jarhar](../../people/josepharhar.md) proposed simplifying the [customizable
select](../../features/customizable-select.md) keyboard model — the elaborate behaviors dated from
the new-element era, and [annevk](../../people/annevk.md) had argued for platform conventions. The minutes record
[gregwhitworth](../../people/gregwhitworth.md) as disagreeing bluntly ("I disagree. A lot. So much"), sarah as agreeing platform
conventions are often bad, and [scotto](../../people/scottaohara.md) as splitting the difference — the current select keyboard UI
is not the best, but customized and uncustomized selects behaving differently was his own earlier
point. The topic was punted to the joint task force / TPAC with a request to bring data. No
resolution was recorded.

([bot comment](https://github.com/openui/open-ui/issues/1087#issuecomment-2347032084))

## Other topics

- [openui/open-ui#1088](https://github.com/openui/open-ui/issues/1088) — extending `popovertarget`
  to custom elements; its resolution was recorded later, on 2024-09-24
  ([resolution](https://github.com/openui/open-ui/issues/1088#issuecomment-2372520455)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
