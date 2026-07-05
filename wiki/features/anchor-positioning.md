---
title: CSS Anchor Positioning
slug: anchor-positioning
kind: feature
status: shipping   # Chrome 125 + Safari 26 shipped; Firefox behind a flag; spec still WD (L1) / FPWD (L2)
specs: [css-anchor-position-1, css-anchor-position-2]
spec_history:
  - {spec: css-anchor-position-1, from: "2022-09"}   # ED adopted (#7282); the problem originated in css-position #5952
  - {spec: css-anchor-position-2, from: "2025-08"}    # Level 2 diff spec created (#12390)
key_people: [tabatkins, fantasai, xiaochengh, bfgeek, kizu, andruud, emilio, jensimmons]
key_issues: [5952, 7282, 8929, 8979, 9145, 10209, 10004, 9149, 10321, 10999, 8584, 8675, 7758, 10258, 12390]
first_seen: "2021-02"               # #5952 opened 2021-02-08
resolutions_count: 113              # labeled css-anchor-position-1 in resolutions-index; +13 more labeled css-anchor-position-2
families: []
coverage: {github: full, www-style: none, member_era: n/a}   # entirely post-2021 GitHub era
generated_by: llm
---

# CSS Anchor Positioning

CSS Anchor Positioning lets an absolutely-positioned element be tethered to one or
more other elements — its *anchors* — declaratively, without JavaScript. The classic
case is placing a tooltip, popover, or `<select>` menu next to the thing that opened it,
and re-placing it when it would overflow the viewport. The feature is built from a small
set of primitives: `anchor-name` marks an element as an anchor; `position-anchor` names
the default anchor for a positioned element; the `anchor()` and `anchor-size()` functions
read an anchor's edges and dimensions inside `inset`/sizing properties; `position-area`
gives a 3×3-grid keyword shorthand for the common placements; and `@position-try` +
`position-try-fallbacks` + `position-visibility` handle what happens when the preferred
position doesn't fit. It is the CSS-native replacement for JS libraries like Floating UI /
Popper.js — a framing the WG made explicit when authors pointed out those libraries follow
transforms and the spec, at the time, did not
([#8584](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-2214423804)).

The feature grew out of Lea Verou's 2021 request to "set a positioned element's containing
block to another element" ([#5952](https://github.com/w3c/csswg-drafts/issues/5952)), and
its history is shaped by two forces. First, a **CSS-vs-HTML** tension — should anchoring be
a magic top-layer attribute, or expressible in CSS? — that resolved toward a CSS function
(`anchor()`) restricted to the anchor's containing-block subtree so cycles are impossible.
Second, a merge of two competing designs: Chrome's inset-based `anchor()` proposal absorbed
the best parts of an Apple grid-based exploration (named position areas, built-in centering)
([#9117](https://github.com/w3c/csswg-drafts/issues/9117)). Because Chrome shipped early
(Chrome 125, May 2024) while the spec kept evolving, an unusually large amount of the WG's
work has been **renaming shipped syntax**: `inset-area` → `position-area`, `anchor-default`
→ `position-anchor`, `position-try-options` → `position-try-fallbacks`, and
`anchors-visible` → `anchor-visible`.

Two decisions define the feature's later history and are still not fully settled: the 2025
reversal from "anchor positioning **ignores** transforms" to "it **follows** them"
([#8584](https://github.com/w3c/csswg-drafts/issues/8584)) — shipped with no opt-out and
sharply contested afterwards ([#13782](https://github.com/w3c/csswg-drafts/issues/13782)) —
and the popover/dialog UA-default-styles saga, where a bespoke `dialog` alignment value was
added and then removed ([#10258](https://github.com/w3c/csswg-drafts/issues/10258)). The
spec is a Working Draft at Level 1 with a Level 2 diff spec at FPWD; see
[css-anchor-position-1](../specs/css-anchor-position-1.md) and
[css-anchor-position-2](../specs/css-anchor-position-2.md).

## Milestones

| Date | Milestone | Source |
|---|---|---|
| 2021-02-08 | Earliest GitHub-era trace — [#5952](https://github.com/w3c/csswg-drafts/issues/5952) "[css-position] Ability to set a positioned element's containing block to another element" ([lea](../people/lea.md)) | [#5952](https://github.com/w3c/csswg-drafts/issues/5952) |
| 2022-09-16 | Adopted as an Editor's Draft; editors Tab Atkins, Ian Kilpatrick, Jhey Tompkins | [#7282 res](https://github.com/w3c/csswg-drafts/issues/7282#issuecomment-1249591201) |
| 2023-06-29 | First Public Working Draft of css-anchor-position-1 | [/TR/](https://www.w3.org/TR/2023/WD-css-anchor-position-1-20230629/) |
| 2024-05-14 | Chrome 125 ships anchor positioning — the first engine (with `inset-area`, no `position-visibility` yet) | [Chrome for Developers](https://developer.chrome.com/blog/anchor-positioning-api) |
| 2024-07-10 | `inset-area` renamed back to `position-area` | [#10209 res](https://github.com/w3c/csswg-drafts/issues/10209#issuecomment-2221005001) |
| 2024-09 | The renames (`position-area`, `position-try-fallbacks`) ship in Chrome 129 | [Chrome for Developers](https://developer.chrome.com/blog/anchor-syntax-changes) |
| 2024-09-27 | "Document containing block" adopted into position-4; FPWD of css-position-4 resolved | [#10861 res](https://github.com/w3c/csswg-drafts/issues/10861#issuecomment-2379849260) |
| 2025-07-23 | WG reverses course: anchor positioning **will** take transforms into account | [#8584 res](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-3109444615) |
| 2025-08-13 | Level 2 diff spec created (`anchored()` container queries) | [#12390 res](https://github.com/w3c/csswg-drafts/issues/12390#issuecomment-3184660869) |
| 2025-09 | Safari 26.0 ships anchor positioning — the second engine | [WebKit](https://webkit.org/blog/17333/webkit-features-in-safari-26-0/) |
| 2025-10-21 | First Public Working Draft of css-anchor-position-2 | [/TR/](https://www.w3.org/TR/2025/WD-css-anchor-position-2-20251021/) |
| 2025-11 | Firefox 145 ships anchor positioning in Nightly, behind a flag | [Bugzilla #1838746](https://bugzilla.mozilla.org/show_bug.cgi?id=1838746) |

*Shipping rows cite vendor primary sources; "the minutes record" phrasing is used for WG
intent, which is not the same as an implementation claim.*

## Resolutions

A curated set of the narrative-carrying resolutions; text is verbatim from
`_generated/resolutions-index.jsonl` (113 carry the `css-anchor-position-1` label, 13 more
`css-anchor-position-2`).

| Date | Resolution (verbatim) | Issue | Permalink |
|---|---|---|---|
| 2022-09-16 | ED of Anchor Positioning, editor [TabAtkins](../people/tabatkins.md) [iank_](../people/bfgeek.md) jhey | [#7282](https://github.com/w3c/csswg-drafts/issues/7282) | [link](https://github.com/w3c/csswg-drafts/issues/7282#issuecomment-1249591201) |
| 2023-06-14 | FPWD of css-anchor-positioning | [#8929](https://github.com/w3c/csswg-drafts/issues/8929) | [link](https://github.com/w3c/csswg-drafts/issues/8929#issuecomment-1591593743) |
| 2023-08-02 | add the anchor-center value | [#8979](https://github.com/w3c/csswg-drafts/issues/8979) | [link](https://github.com/w3c/csswg-drafts/issues/8979#issuecomment-1663086600) |
| 2023-08-23 | make the anchor-name property a comma-separated list of idents | [#8837](https://github.com/w3c/csswg-drafts/issues/8837) | [link](https://github.com/w3c/csswg-drafts/issues/8837#issuecomment-1690145010) |
| 2023-08-23 | add a separate property (can bikeshed name in future), not merely a shorthand, but interacts with inset properties in current draft | [#9145](https://github.com/w3c/csswg-drafts/issues/9145) | [link](https://github.com/w3c/csswg-drafts/issues/9145#issuecomment-1690207503) |
| 2024-03-06 | switching center-* keywords to span-* and all to span-all | [#9862](https://github.com/w3c/csswg-drafts/issues/9862) | [link](https://github.com/w3c/csswg-drafts/issues/9862#issuecomment-1981462866) |
| 2024-03-13 | rename anchor-default to position-anchor | [#10004](https://github.com/w3c/csswg-drafts/issues/10004) | [link](https://github.com/w3c/csswg-drafts/issues/10004#issuecomment-1994624254) |
| 2024-03-13 | Add position-visibility as proposed in the issue with concerns noted as issues in the draft, to the editors draft *after* publication of working draft. | [#7758](https://github.com/w3c/csswg-drafts/issues/7758) | [link](https://github.com/w3c/csswg-drafts/issues/7758#issuecomment-1994765991) |
| 2024-03-20 | fallback styles live in a new "Position Fallback Origin". They revert like Animation styles (back to User origin) | [#9149](https://github.com/w3c/csswg-drafts/issues/9149) | [link](https://github.com/w3c/csswg-drafts/issues/9149#issuecomment-2009875182) |
| 2024-05-15 | Make position a shorthand of position-anchor and a new position-type property. The shorthand resets both. | [#10321](https://github.com/w3c/csswg-drafts/issues/10321) | [link](https://github.com/w3c/csswg-drafts/issues/10321#issuecomment-2112965730) |
| 2024-06-26 | rename position-try-options to position-try-fallbacks | [#10395](https://github.com/w3c/csswg-drafts/issues/10395) | [link](https://github.com/w3c/csswg-drafts/issues/10395#issuecomment-2192127524) |
| 2024-07-10 | Change inset-area back to position-area | [#10209](https://github.com/w3c/csswg-drafts/issues/10209) | [link](https://github.com/w3c/csswg-drafts/issues/10209#issuecomment-2221005001) |
| 2024-09-04 | undo the previous resolution and not add position-anchor and position-type to the position shorthand for now | [#10321](https://github.com/w3c/csswg-drafts/issues/10321) | [link](https://github.com/w3c/csswg-drafts/issues/10321#issuecomment-2330338181) |
| 2024-09-27 | Adopt the concept of document containing block (better name TBD) into position-4 and have anchor positioning use it by default instead of ICB | [#10861](https://github.com/w3c/csswg-drafts/issues/10861) | [link](https://github.com/w3c/csswg-drafts/issues/10861#issuecomment-2379849260) |
| 2024-10-16 | accept what I said in the thread with caveat from here. when an anchor position element is first rendered or change fallback position, use the current scroll offset to calculate its position area | [#10999](https://github.com/w3c/csswg-drafts/issues/10999) | [link](https://github.com/w3c/csswg-drafts/issues/10999#issuecomment-2417388395) |
| 2025-07-23 | Anchor positioning will take transforms into account. | [#8584](https://github.com/w3c/csswg-drafts/issues/8584) | [link](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-3109444615) |
| 2025-08-13 | create level 2 diff spec for anchor pos and define an anchored keyword for container-type there | [#12390](https://github.com/w3c/csswg-drafts/issues/12390) | [link](https://github.com/w3c/csswg-drafts/issues/12390#issuecomment-3184660869) |
| 2025-10-15 | remove the dialog value of the alignment properties and revert the UA default styles for [popover] and dialog | [#10258](https://github.com/w3c/csswg-drafts/issues/10258) | [link](https://github.com/w3c/csswg-drafts/issues/10258#issuecomment-3407215102) |
| 2026-05-06 | rename anchors-visible to anchor-visible | [#10201](https://github.com/w3c/csswg-drafts/issues/10201) | [link](https://github.com/w3c/csswg-drafts/issues/10201#issuecomment-4390233490) |
| 2026-05-27 | Add an anchor-position-follows-transforms keyword to feature-detect whether anchor positioning follows transforms | [#13678](https://github.com/w3c/csswg-drafts/issues/13678) | [link](https://github.com/w3c/csswg-drafts/issues/13678#issuecomment-4556655505) |
| 2026-06-24 | @position-try uses a globally scoped name like @keyframes | [#13567](https://github.com/w3c/csswg-drafts/issues/13567) | [link](https://github.com/w3c/csswg-drafts/issues/13567#issuecomment-4791554191) |
| 2026-07-01 | add flip-self-inline and flip-self-block to position-try | [#14062](https://github.com/w3c/csswg-drafts/issues/14062) | [link](https://github.com/w3c/csswg-drafts/issues/14062#issuecomment-4857805306) |

## Key debates

### From "set the containing block" to a dedicated module

The origin issue, [#5952](https://github.com/w3c/csswg-drafts/issues/5952) (2021), was
[lea](../people/lea.md)'s request to let a positioned element's containing block be another
element, so popups could be placed relative to an anchor "without the flimsy JS." The core
tension was **CSS vs HTML**: [chrishtr](../people/chrishtr.md) argued a `<popup>`/top-layer
HTML attribute would be far simpler to implement, since the top layer "avoids all of the
complexity of whatever filters, clips, scrolls, transforms" above it
([comment](https://github.com/w3c/csswg-drafts/issues/5952#issuecomment-778538065)).
[lea](../people/lea.md) pushed back on principle: an HTML attribute "violates separation of
concerns, as well as the Extensible Web Manifesto (by adding new magic that cannot be
specified in CSS)"
([comment](https://github.com/w3c/csswg-drafts/issues/5952#issuecomment-780028498)). The
resolution of that tension is the design's keystone: [bfgeek](../people/bfgeek.md)'s
restriction that the anchor "needs to be contained within the same containing-block subtree"
([comment](https://github.com/w3c/csswg-drafts/issues/5952#issuecomment-776351769)), which
makes reference cycles impossible and became the reason `anchor()` is a CSS function rather
than DOM magic.

When [bfgeek](../people/bfgeek.md) and [tabatkins](../people/tabatkins.md) formalized this as
[#7282](https://github.com/w3c/csswg-drafts/issues/7282) (adopted as ED 2022-09-16), the
recurring complaint was **complexity**: FremyCompany objected that "the 'basic' use case
requires dozens of lines of code"
([comment](https://github.com/w3c/csswg-drafts/issues/7282#issuecomment-1249587665)), and
[emilio](../people/emilio.md) floated a simpler declarative model where the author names an
anchor-side and popup-side and the UA guarantees on-screen placement. [bfgeek](../people/bfgeek.md)
resisted, arguing (the minutes record) that such a model "covers the 60-70% case, but you
start to lose out on some of the slightly more advanced cases"
([minutes](https://github.com/w3c/csswg-drafts/issues/7282#issuecomment-1249591201)). At FPWD
([#8929](https://github.com/w3c/csswg-drafts/issues/8929), 2023-06), the friction was not the
design but **shipping velocity**: the minutes record [jensimmons](../people/jensimmons.md)
(Apple) asking for "more time for review before folks ship it" given Chrome's ~2-month
timeline, with tantek adding "+1 … this feels unusual for the 'normal' CSSWG workmode"
([minutes](https://github.com/w3c/csswg-drafts/issues/8929#issuecomment-1591593743)).

### The `position-area` naming saga

The 3×3-grid keyword property — write `position-area: top` instead of a pair of `anchor()`
calls — has been renamed twice, and the churn is emblematic of the feature. It began in
[#9145](https://github.com/w3c/csswg-drafts/issues/9145) (2023-08) as **`inset-area`**, a
name [tabatkins](../people/tabatkins.md) admitted (the minutes record) was "the first name
that came to mind"; [jensimmons](../people/jensimmons.md) immediately flagged that the team's
own exploration had called it `position-area` and that `inset-area` implies the wrong mental
model ([minutes](https://github.com/w3c/csswg-drafts/issues/9145#issuecomment-1690207503)).
The WG deferred the name ("can bikeshed name in future") and resolved it as a standalone
property, not a mere shorthand, because — [fantasai](../people/fantasai.md)'s argument — a
shorthand loses fallbacks, the container's writing mode, and conditional styling.

Two later cleanups closed the loop. In [#9862](https://github.com/w3c/csswg-drafts/issues/9862)
the ambiguous value grammar (interchangeable axis order, single value implying `/ all`, and
`center` meaning two different things) was reworked: [una](../people/una.md) reported finding
"the syntax very confusing thus far"
([comment](https://github.com/w3c/csswg-drafts/issues/9862#issuecomment-1915666082)), and the
group adopted [miriam](../people/miriam.md)'s `span-*` idea over a rejected `span()` function
(which collided with grid's `span 2`) and [mfreed7](../people/mfreed7.md)'s `-and-` infix. Then
[#10209](https://github.com/w3c/csswg-drafts/issues/10209) reverted the name: [nt1m](../people/ntim.md) argued
"the `inset-*` naming … implies overriding the other `inset` properties. It's not obvious you
can use both `inset-area` and `inset` together"
([comment](https://github.com/w3c/csswg-drafts/issues/10209#issuecomment-2125988059)) — the
property actually chooses the *containing block*, which is a `position-*` job. [tabatkins](../people/tabatkins.md)
lightly objected to a value-neutral rename this late but did not block; the WG changed it back
to `position-area`. A final polish in [#12749](https://github.com/w3c/csswg-drafts/issues/12749)
(2025) normalized `self-` to a consistent prefix (`x-self-start` → `self-x-start`).

### Position fallback: `@position-try`, flip tactics, and the cascade origin

If the preferred placement overflows, the UA tries alternatives. The machinery went through
its own rename chain: the original `@position-fallback` at-rule with `@try` blocks became
`@position-try` + `position-try-fallbacks`. The last rename
([#10395](https://github.com/w3c/csswg-drafts/issues/10395)) followed a semantic change —
once the property was defined to always include the base styles first, [fantasai](../people/fantasai.md)
noted "it's really fallbacks … so I think we should actually name it by what we call it"
([issue](https://github.com/w3c/csswg-drafts/issues/10395)).

Two deeper design points settled here. **Where fallback styles sit in the cascade**
([#9149](https://github.com/w3c/csswg-drafts/issues/9149)): because the UA must run layout to
pick a fallback, [xiaochengh](../people/xiaochengh.md) explained "everything is done at used
value time" ([comment](https://github.com/w3c/csswg-drafts/issues/9149#issuecomment-1699929804)),
and Chromium initially made fallbacks win over everything, including `!important`. The WG first
resolved `!important` must win, then adopted [andruud](../people/andruud.md)'s proposal of a
dedicated **"Position Fallback Origin"** (between the author and animation origins) rather than
"claiming they're animations"
([comment](https://github.com/w3c/csswg-drafts/issues/9149#issuecomment-1790514033)). **How
the `flip-*` tactics work** ([#10049](https://github.com/w3c/csswg-drafts/issues/10049)):
a `flip-block`/`flip-inline`/`flip-start` keyword synthesizes a virtual `@position-try` by
swapping values, flipping them (the design settled) after `var()`/`env()` substitution but
before style/layout interleaving. The newest additions extend the same idea —
`flip-self-inline`/`flip-self-block` were added for `::picker(select)` in
[#14062](https://github.com/w3c/csswg-drafts/issues/14062) (2026-07).

### `position-anchor` and the `position` shorthand that wasn't

The property naming follows a dichotomy — `position-*` on the positioned element, `anchor-*`
on the anchor element — so [tabatkins](../people/tabatkins.md) renamed the outlier
`anchor-default` (set on the positioned element) to **`position-anchor`** in
[#10004](https://github.com/w3c/csswg-drafts/issues/10004). That immediately raised a
follow-up he deferred as "a problem for future Tab to solve": should `position` become a
shorthand that resets `position-anchor`? [#10321](https://github.com/w3c/csswg-drafts/issues/10321)
is a clean example of the WG reversing itself. It **first resolved** (2024-05-15) to make
`position` a shorthand of `position-anchor` plus a new `position-type`. Then Chrome objected on
web-compat grounds — [bfgeek](../people/bfgeek.md) cited the `white-space` precedent where
authors "assume the property will read back the same as the property they set", and
[chrishtr](../people/chrishtr.md) delivered the formal objection: "Given all the compat risk,
implementation difficulty and potential for developer confusion, Google doesn't think
shorthand-ifying `position` is feasible or worth doing"
([comment](https://github.com/w3c/csswg-drafts/issues/10321#issuecomment-2272165809)).
[tabatkins](../people/tabatkins.md), reviewing the full property list, found the
prefix-implies-shorthand "expectation is actually broken a lot more than I thought"
([comment](https://github.com/w3c/csswg-drafts/issues/10321#issuecomment-2136102979)). The
WG **undid** the resolution (2024-09-04); `position` remains a plain longhand.

### Should anchor positioning follow transforms?

This is the feature's most contested decision and it is a full reversal. Originally, transforms
were *intentionally* ignored — as late as 2024 [tabatkins](../people/tabatkins.md) told an
author "Chrome's implementation should *entirely* ignore transforms; if you're seeing any
effect of transforms on anchorpos, that's a bug"
([#10555](https://github.com/w3c/csswg-drafts/issues/10555#issuecomment-2240515926)). The
reason was performance: [bfgeek](../people/bfgeek.md) and [emilio](../people/emilio.md) warned
a layout dependency on transforms would break compositor acceleration —
[emilio](../people/emilio.md): "it'd force the transform animations on such elements (and any
of their ancestors) to not be off-main-thread, and affect layout, which is a no-no"
([#8584](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-2450877440)).

Authors pushed back hard in [#8584](https://github.com/w3c/csswg-drafts/issues/8584):
canvas-style UIs rely on transforms, and jonrimmer pointed out that "the most popular JS
library for achieving anchored positioning, Floating UI (the successor to Popper.js), *does*
take CSS transforms into account, so as it stands anchor-positioning will not be adequate to
replace it" ([comment](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-2214423804)).
[chrishtr](../people/chrishtr.md) found the compromise that unlocked the reversal: "treat
transform the same as layout-affecting properties — if it changes, then schedule a re-render.
This will get behind by a frame or so during a threaded animation of transform, but that's
better than breaking when transform+layout changes at the same time"
([comment](https://github.com/w3c/csswg-drafts/issues/8584#issuecomment-3105053563)). The WG
resolved (2025-07-23) that "Anchor positioning will take transforms into account," with
[emilio](../people/emilio.md) noting a standing Mozilla perf caveat but not blocking.

The fallout is unresolved. Because the change shipped in Chrome with **no opt-out** on a
Baseline feature, [lea](../people/lea.md) called it "rushed and hacky … a breaking change on
how a Baseline feature works, with no opt-out, which is unprecedented"
([#13782](https://github.com/w3c/csswg-drafts/issues/13782#issuecomment-4556836871)) — the
motivating case being an author's shake animation on a button that now also shook its tethered
tooltip. The WG shipped feature detection (`anchor-position-follows-transforms`,
[#13678](https://github.com/w3c/csswg-drafts/issues/13678)); a general opt-out
([#13782](https://github.com/w3c/csswg-drafts/issues/13782)) remains open.

### The death of `anchor-scroll`: automatic scroll compensation

An anchored element must track its anchor when the anchor scrolls, even though it may live
outside the anchor's scroller. The original design exposed an `anchor-scroll` property — until
[xiaochengh](../people/xiaochengh.md) filed [#8675](https://github.com/w3c/csswg-drafts/issues/8675)
noting the name collides with the unrelated "scroll anchoring" (`overflow-anchor`), and the
discussion escalated from *rename it* to *remove it*: "let's hide `anchor-scroll` and just use
the default/implicit anchor element"
([comment](https://github.com/w3c/csswg-drafts/issues/8675#issuecomment-1602967617)). Scroll
compensation became **automatic**. [#10999](https://github.com/w3c/csswg-drafts/issues/10999)
then formalized the model around the compositor constraint [tabatkins](../people/tabatkins.md)
identified: you can *shift* an anchored element by scroll position (cheap, compositor-side) or
*select a fallback* by it, but you can never *size* by it. The resolution (2024-10-16) uses the
current scroll offset to compute the `position-area` only at first layout and on fallback
changes, tracking scroll thereafter as a post-layout "default scroll shift." A later
spec-vs-implementation divergence surfaced when [mstensho](../people/mstensho.md) found Blink
recalculated every frame while the spec recalculates only on overflow — resolved in the spec's
favor for stability and performance.

### Conditional hiding, popover defaults, and centering

Three author-facing behaviors settled together. **`position-visibility`**
([#7758](https://github.com/w3c/csswg-drafts/issues/7758)) hides an anchored element when its
anchor scrolls away, so a tooltip doesn't hover in empty space. The debate was clip-vs-hide
([xiaochengh](../people/xiaochengh.md) preferred clipping as "a better/smoother UX") against
[tabatkins](../people/tabatkins.md)'s "fail visible/open policy in CSS"; the property later had
its values renamed to the singular `anchor-*` prefix (`anchors-visible` → `anchor-visible`,
[#10201](https://github.com/w3c/csswg-drafts/issues/10201)) since only the default anchor
matters. **`anchor-center`** ([#8979](https://github.com/w3c/csswg-drafts/issues/8979)) added a
built-in centering value after [kizu](../people/kizu.md) showed centering otherwise required
verbose `calc()`/`min()` math; [tabatkins](../people/tabatkins.md) reframed it as an
`align-self: anchor-center` value borrowed from the grid-based proposal.

**Popover/dialog UA styles** ([#10258](https://github.com/w3c/csswg-drafts/issues/10258)) is
another add-then-remove arc. The HTML UA styles that center `[popover]`/`dialog`
(`inset: 0; margin: auto`) silently defeat anchor positioning until authors reset margins, so
the WG invented a conditional `dialog` value for `align/justify-self`, shipped it, then reversed
course (2025-10-15) — removing the `dialog` value and instead simply disabling auto margins when
`position-area` is set or `align-self: anchor-center` is used. [nt1m](../people/ntim.md) had objected to the special
value from the start ("Not a fan of a special 'dialog' value")
([comment](https://github.com/w3c/csswg-drafts/issues/10258#issuecomment-3120535476)).

### Level 2: what got deferred

The Level 2 diff spec was created by [#12390](https://github.com/w3c/csswg-drafts/issues/12390)
(2025-08-13) to host features too experimental or too late for Level 1. Chief among them:
`container-type: anchored` + an `anchored()` `@container` query
([#12390](https://github.com/w3c/csswg-drafts/issues/12390),
[#12391](https://github.com/w3c/csswg-drafts/issues/12391)) so descendants can style
themselves based on which fallback an anchored element chose —
[tabatkins](../people/tabatkins.md) noted (the minutes record) it must be a container query,
not an element query, "for bad cyclic reasons." The `::tether` pseudo-element for drawing
connector arrows ([#9271](https://github.com/w3c/csswg-drafts/issues/9271)) was the first
feature flagged too-experimental — kept in Level 1 as *at risk* in 2023 after
[tabatkins](../people/tabatkins.md) called it "the [#1](https://github.com/w3c/csswg-drafts/issues/1) feature for the next level," and it now
sits in the Level 2 bucket. Also deferred to Level 2: taking transforms into account was first
tracked here, `anchor-size()` in more properties, anchoring to pointer/fragment, and multiple
names in `position-anchor` for fallback.

## Related features

- **Popover / `<selectmenu>` / customizable `<select>`** — the primary consumers; the
  `::picker(select)` work drives recent anchor changes
  ([#14062](https://github.com/w3c/csswg-drafts/issues/14062)).
- **[css-position-3/4](../specs/css-anchor-position-1.md)** — anchor positioning depends on the
  "document containing block" adopted into position-4
  ([#10861](https://github.com/w3c/csswg-drafts/issues/10861)).
- **css-align-3** — `anchor-center` and alignment safety interact throughout
  (e.g. [#12020](https://github.com/w3c/csswg-drafts/issues/12020),
  [#10860](https://github.com/w3c/csswg-drafts/issues/10860)).
- **css-contain / container queries** — containment vs anchor-name scoping
  ([#10040](https://github.com/w3c/csswg-drafts/issues/10040)) and the Level 2 `anchored()` query.
- **scroll-driven animations / view transitions** — share the tree-scoped-name lookup rules
  ([#13364](https://github.com/w3c/csswg-drafts/issues/13364)).

## Sources

Primary (GitHub issue threads, mirrored):

- [#5952 set the containing block to another element](../../raw/data/github/csswg-drafts/issues/05xxx/05952.md) — the origin.
- [#7282 Introduce CSS Anchor Positioning](../../raw/data/github/csswg-drafts/issues/07xxx/07282.md) — became the ED.
- [#9145 Grid-based anchoring syntax](../../raw/data/github/csswg-drafts/issues/09xxx/09145.md) / [#10209 rename inset-area](../../raw/data/github/csswg-drafts/issues/10xxx/10209.md) — the `position-area` saga.
- [#9149 cascade / Position Fallback Origin](../../raw/data/github/csswg-drafts/issues/09xxx/09149.md), [#10321 position shorthand](../../raw/data/github/csswg-drafts/issues/10xxx/10321.md) — fallback machinery.
- [#8584 transforms](../../raw/data/github/csswg-drafts/issues/08xxx/08584.md), [#13782 opt-out](../../raw/data/github/csswg-drafts/issues/13xxx/13782.md) — the transforms reversal.
- [#8675 anchor-scroll](../../raw/data/github/csswg-drafts/issues/08xxx/08675.md), [#10999 scroll compensation](../../raw/data/github/csswg-drafts/issues/10xxx/10999.md).
- [#7758 position-visibility](../../raw/data/github/csswg-drafts/issues/07xxx/07758.md), [#10258 popover defaults](../../raw/data/github/csswg-drafts/issues/10xxx/10258.md), [#12390 Level 2](../../raw/data/github/csswg-drafts/issues/12xxx/12390.md).

Resolution text from `_generated/resolutions-index.jsonl`. Status:
`raw/data/w3c-api/specifications/css-anchor-position-1.json` and `-2.json` (`snapshot_at: 2026-07-04`);
Editor's Drafts <https://drafts.csswg.org/css-anchor-position-1/> and
<https://drafts.csswg.org/css-anchor-position-2/>. Shipping: vendor primary sources linked in
Milestones ([Chrome](https://developer.chrome.com/blog/anchor-positioning-api),
[WebKit](https://webkit.org/blog/17333/webkit-features-in-safari-26-0/),
[Firefox Bugzilla](https://bugzilla.mozilla.org/show_bug.cgi?id=1838746)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
Working Group. Verify against the linked primary sources.*
