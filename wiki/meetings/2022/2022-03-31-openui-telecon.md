---
date: 2022-03-31
group: openui
type: telecon
topics_count: 3
issues: [240, 491, 499]
generated_by: llm
---

# Open UI CG telecon — 2022-03-31

Three topics, two resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [2022-03-31](https://www.w3.org/2022/03/31-openui-minutes.html).

## Light dismiss on page scroll? ([openui/open-ui#240](https://github.com/openui/open-ui/issues/240))

Should a popup light-dismiss when the page or a container scrolls? The minutes record [masonf](../../people/mfreed7.md)
citing a font-preview page where differently-sized previews caused jank that triggered unwanted
dismissals, and una arguing users often scroll away to check information and come back, so
dismiss-on-scroll should at most be an opt-in add-on, never the default. The minutes record
[dandclark](../../people/dandclark.md) noting authors who do want it can add a scroll handler. Broad +1s were recorded
(davatron5000, [scotto](../../people/scottaohara.md), [bkardell](../../people/bkardell.md), [JonathanNeal](../../people/jonathanneal.md), [tantek](../../people/tantek.md)).

> RESOLVED: Proposed resolution: A popup *should not* light-dismiss upon page/container scroll.

([resolution](https://github.com/openui/open-ui/issues/240#issuecomment-1084971517))

## Other topics

- [openui/open-ui#499](https://github.com/openui/open-ui/issues/499) — `<measure>` web component; resolved that Open UI will incubate a solution to semantic measurements ([resolution](https://github.com/openui/open-ui/issues/499#issuecomment-1084962904)).
- [openui/open-ui#491](https://github.com/openui/open-ui/issues/491) — bikeshedding `popup=popup`, continued in later meetings.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
