---
date: 2025-08-14
group: openui
type: telecon
topics_count: 8
issues: [1228, 1229, 1238, 1244, 1245, 1254, 1255, 1256]
generated_by: llm
---

# Open UI CG telecon — 2025-08-14

Eight topics, five resolutions. Minutes recorded by the CSS meeting bot on the linked issues.
Official minutes: [www.w3.org/2025/08/14-openui-minutes.html](https://www.w3.org/2025/08/14-openui-minutes.html) (dated-URL convention for CG minutes).

## [select] listbox toggle/beforetoggle ([openui/open-ui#1228](https://github.com/openui/open-ui/issues/1228))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). The minutes record [jarhar](../../people/josepharhar.md) as
noting `toggle`/`beforetoggle` stopped being exposed for customizable select after the
replaceable-popover design was removed, and proposing to fire them on the `<select>` element
itself, including for the `appearance: auto` picker; [keithamus](../../people/keithamus.md) agreed the events should not
depend on `appearance: base` ("events based on style" would feel strange); [masonf](../../people/mfreed7.md) was supportive
pending no timing issues relative to cloning behaviour.

> RESOLVED: add toggle and beforetoggle events to the select element

([resolution](https://github.com/openui/open-ui/issues/1228#issuecomment-3189418498))

## [select] Specifying direction for arrow key navigation ([openui/open-ui#1229](https://github.com/openui/open-ui/issues/1229))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). una proposed letting authors
specify arrow-key direction for pickers that open upward or sideways, arguing keyboard behaviour
should follow the visual layout. The minutes record scott as sceptical: selects have behaved one
way for 30 years, changing keyboard behaviour to match visuals frustrates power keyboard users,
and grid-like pickers are really a separate (grid role) conversation; sarah warned that behaviour
changes affect users who aren't looking at the screen and that orientation is poorly communicated
by AT today. The group asked una for user feedback and prototypes before going further. No
resolution was recorded.

## [select] checkmark for select multiple ([openui/open-ui#1238](https://github.com/openui/open-ui/issues/1238))

Part of the customizable `<select>` work — see
[customizable select](../../features/customizable-select.md). [aleventhal](../../people/aleventhal.md) had suggested
checkbox-style UI for multi-select options; the minutes record [jarhar](../../people/josepharhar.md) as reporting that the
available unicode checkbox characters render inconsistently, and una and [masonf](../../people/mfreed7.md) as preferring
consistency with single-select styling, leaving richer affordances to authors.

> RESOLVED: Keep the single-select styles which just show a checkmark for selected options and an empty space for not-selected options

([resolution](https://github.com/openui/open-ui/issues/1238#issuecomment-3189488787))

## [Range] What is the label? ([openui/open-ui#1244](https://github.com/openui/open-ui/issues/1244))

The bot posted a comment for this topic, but its IRC log records essentially no discussion (the
item was deferred; see the [2025-08-21 telecon](2025-08-21-openui-telecon.md)). No resolution was
recorded. ([bot comment](https://github.com/openui/open-ui/issues/1244#issuecomment-3189491249))

## [Range] Attribute disagreements ([openui/open-ui#1245](https://github.com/openui/open-ui/issues/1245))

What happens when `min`/`max` on inner range inputs conflict with the wrapping rangegroup. The
minutes record sarah as asking whether inner `min`/`max` should be allowed at all; [masonf](../../people/mfreed7.md)'s first
instinct was that the group's bounds should clamp the inner values; una offered easing-curve
editors as a real use case for differing bounds. Discussion continued on
[2025-09-11](2025-09-11-openui-telecon.md). No resolution was recorded.

## Other topics

- [openui/open-ui#1254](https://github.com/openui/open-ui/issues/1254) — [Link delegation] modifier key passthrough; resolved to pass along the modifier keys ([resolution](https://github.com/openui/open-ui/issues/1254#issuecomment-3189546477)).
- [openui/open-ui#1255](https://github.com/openui/open-ui/issues/1255) — [Link delegation] does the target get :hover, :active styles?; resolved to add dedicated pseudo-classes instead ([resolution](https://github.com/openui/open-ui/issues/1255#issuecomment-3189559899)).
- [openui/open-ui#1256](https://github.com/openui/open-ui/issues/1256) — [Link delegation] additional element support; resolved to shelve for now ([resolution](https://github.com/openui/open-ui/issues/1256#issuecomment-3189535736)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
