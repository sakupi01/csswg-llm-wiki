---
date: 2024-05-02
group: openui
type: telecon
topics_count: 2
issues: [1045, 1046]
generated_by: llm
---

# Open UI CG telecon — 2024-05-02

Two topics, two resolutions, both on `<input type=checkbox switch>`. Minutes recorded by the CSS
meeting bot on the linked issues. Official minutes:
[2024/05/02-openui-minutes.html](https://www.w3.org/2024/05/02-openui-minutes.html)
(dated-URL convention for CG minutes).

## [switch] Should the switch element support swipe actions? ([openui/open-ui#1045](https://github.com/openui/open-ui/issues/1045))

[gregwhitworth](../../people/gregwhitworth.md) asked whether the switch should support drag/swipe gestures. The minutes record
[brecht_dr](../../people/brechtDR.md) as opposed ("I don't think it's something that should be standardized"), [masonf](../../people/mfreed7.md) as softly
agreeing until [keithamus](../../people/keithamus.md) tried it live and found iOS switches do respond to dragging, and [scotto](../../people/scottaohara.md) as
disliking the interaction after testing it ("after holding it just goes to the next state … you
can't undo it") and warning against gimmicks given WCAG's dragging rules. bkardell_ questioned
whether platform-convention behavior can even be specced; the group aligned on the range-control
precedent and deferred normative text.

> RESOLVED: Switch should support gesture support akin to the range control; normative text to be defined at a later point

([resolution](https://github.com/openui/open-ui/issues/1045#issuecomment-2091232376))

## [switch] Should the switch have a toggle() method? ([openui/open-ui#1046](https://github.com/openui/open-ui/issues/1046))

[gregwhitworth](../../people/gregwhitworth.md) relayed the request for a `toggle()` method that flips the switch's value. The
minutes record bkardell_ as wanting the answer to be "no" for the `<input>` variant ("input is
already weird with all the variants"), while noting he would like a `toggle()` on a hypothetical
`<switch>` element, and [masonf](../../people/mfreed7.md) as pointing out `click()` already does the job. The group declined
the method.

> RESOLVED: input type="checkbox" switch will not have a toggle() method

([resolution](https://github.com/openui/open-ui/issues/1046#issuecomment-2091200975))

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
