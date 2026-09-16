---
date: 2023-11-16
group: openui
type: telecon
topics_count: 5
issues: [930, 933, 935, 941, 945]
generated_by: llm
---

# Open UI CG telecon — 2023-11-16

Five topics, three resolutions captured by the bot. Minutes recorded by the CSS meeting bot on
the linked issues.
Official minutes: [w3.org/2023/11/16-openui-minutes.html](https://www.w3.org/2023/11/16-openui-minutes.html) (dated-URL convention for CG minutes).

## Naming combobox Element ([openui/open-ui#930](https://github.com/openui/open-ui/issues/930))

Naming the element from the combobox explainer incubated since
[2023-11-02](2023-11-02-openui-telecon.md) (a sibling of the `<selectlist>` work — see
[customizable select](../../features/customizable-select.md)). The minutes record Sudheer as
reporting "combobox" leading the vote; [brecht_dr](../../people/brechtDR.md) asked whether the vote should reach a wider
audience. [masonf](../../people/mfreed7.md) raised the alternative history: `<input type=datalist>`-style approaches already
approximate a combobox, and warned from experience to "plan on changing it 3-5 times" once WHATWG
weighs in. Luke_W favoured combobox — it matches the ARIA role, "dropdown" had been voted out,
and design systems' varying names often describe different components anyway. The outcome was
typed as "Resolved: The name for the new element will be combobox" (lower-case, so not captured
in the bot's resolution summary — see the
[discussion comment](https://github.com/openui/open-ui/issues/930#issuecomment-1815175574)).

## Other topics

- [openui/open-ui#933](https://github.com/openui/open-ui/issues/933) — resolved to rename the invoker "mute" action to "toggleMuted" ([resolution](https://github.com/openui/open-ui/issues/933#issuecomment-1815200434)).
- [openui/open-ui#935](https://github.com/openui/open-ui/issues/935) — resolved that `toggle`/`toggleModal` close open dialogs regardless of mode ([resolution](https://github.com/openui/open-ui/issues/935#issuecomment-1815164252)).
- [openui/open-ui#945](https://github.com/openui/open-ui/issues/945) — resolved to require user gestures only for advanced invoker APIs ([resolution](https://github.com/openui/open-ui/issues/945#issuecomment-1815229335)).
- [openui/open-ui#941](https://github.com/openui/open-ui/issues/941) — initially-open non-modal dialogs, discussed without resolution.

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
