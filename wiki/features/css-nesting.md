---
title: CSS Nesting
slug: css-nesting
kind: feature
status: shipped
specs: [css-nesting-1]
spec_history:
  - {spec: css-nesting-1, from: "2018-07"}
key_people: [tabatkins, fantasai, mirisuzanne, plinss, emilio, andruud, lea]
key_issues: [2701, 4748, 7834, 8248, 8249, 7961, 5745, 8310, 9492, 8662, 8738, 10234]
first_seen: "2017-02"
resolutions_count: 48
families: []
coverage: {github: full, www-style: none, member_era: n/a}
generated_by: llm
---

# CSS Nesting

Native CSS nesting lets a style rule contain other style rules, so descendant
and related selectors can be written inside their context instead of repeated:

```css
.card {
  color: black;
  & .title { font-weight: bold; }
  &:hover { color: blue; }
}
```

The feature was long provided by preprocessors (Sass, Less, PostCSS), and that
pre-existing author muscle memory shaped almost every WG decision below. Its
history is dominated by **two multi-year debates**: what the *syntax* should be
(resolved by adopting "Option 3" plus a parser lookahead relaxation) and what
`&` *means* (resolved by aliasing it to `:is()`/`:scope`, which then created a
long tail of specificity and CSSOM problems). It shipped in all three engines
during 2023 and reached its current form (`CSSNestedDeclarations`) in late 2024.

The spec is still a Working Draft despite universal implementation — see
[css-nesting-1](../specs/css-nesting-1.md).

## Milestones

| Date | Milestone | Source |
|---|---|---|
| 2017-02 | Earliest trace in the GitHub era — [#998](https://github.com/w3c/csswg-drafts/issues/998) "[css-nesting] Status?" (the proposal predates GitHub as an unofficial Tab Atkins draft) | [#998](https://github.com/w3c/csswg-drafts/issues/998) |
| 2018-07-04 | Adopted as an Editor's Draft, Tab Atkins editor | [#2701](https://github.com/w3c/csswg-drafts/issues/2701#issuecomment-402392212) |
| 2021-08-31 | First Public Working Draft | [/TR/](https://www.w3.org/TR/2021/WD-css-nesting-1-20210831/) |
| 2023-01-11 | Syntax settled: "Option 3" adopted | [#8249](https://github.com/w3c/csswg-drafts/issues/8249#issuecomment-1379326665) |
| 2023-03-29 | Chrome 112 ships (strict syntax) | [Chrome for Developers](https://developer.chrome.com/blog/css-nesting) |
| 2023-05 | Safari 16.5 ships (strict syntax) | [WebKit blog](https://webkit.org/blog/14571/css-nesting-and-the-cascade/) |
| 2023-04-19 | Parser lookahead relaxation adopted (bare type selectors allowed) | [#7961](https://github.com/w3c/csswg-drafts/issues/7961#issuecomment-1514955984) |
| 2023-08-29 | Firefox 117 ships — with the relaxed syntax from the start | [MDN / Firefox 117 notes](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/117) |
| 2023-12 | Relaxed syntax reaches Chrome 120 and Safari 17.2 | [Chrome for Developers](https://developer.chrome.com/blog/css-nesting-relaxed-syntax-update) |
| 2024-10 | `CSSNestedDeclarations` fixes declaration/at-rule ordering — Chrome 130, Firefox 132 | [web.dev](https://web.dev/blog/css-nesting-cssnesteddeclarations) |
| 2024-12 | Safari 18.2 ships `CSSNestedDeclarations` | [web.dev](https://web.dev/blog/css-nesting-cssnesteddeclarations) |

*Shipping rows cite vendor primary sources; "the minutes record" phrasing is used
for WG intent, which is not the same as an implementation claim.*

## Resolutions

Verbatim from `_generated/resolutions-index.md` (css-nesting-labeled; 48 total).
The load-bearing ones:

| Date | Resolution | Issue |
|---|---|---|
| 2018-07-04 | add css-nesting as an ED, Tab Atkins as editor, file issues until ppl are overall kinda happy with what it's like before we consider FPWD | [#2701](https://github.com/w3c/csswg-drafts/issues/2701#issuecomment-402392212) |
| 2021-11-03 | change nesting draft to use open/close brackets, and add a note to show that syntax vs. what Tab would prefer | [#4748](https://github.com/w3c/csswg-drafts/issues/4748#issuecomment-960145492) |
| 2021-11-03 | don't have nesting om using its own interface; instead, just allow style rule to contain a list of style rule | [#4748](https://github.com/w3c/csswg-drafts/issues/4748#issuecomment-960145492) |
| 2022-08-31 | Revert the previous resolution from Nov 2021 mandating bracket-nesting syntax, and the WG preference for a single nesting syntax. | [#4748](https://github.com/w3c/csswg-drafts/issues/4748#issuecomment-1233176065) |
| 2022-10-12 | Accept to make & valid everywhere, maps to :scope where not otherwise defined | [#5745](https://github.com/w3c/csswg-drafts/issues/5745#issuecomment-1276466934) |
| 2022-10-26 | We're taking option 3 over option 1 | [#7834](https://github.com/w3c/csswg-drafts/issues/7834#issuecomment-1292277520) |
| 2022-12-21 | Reject options 4 and 5, go with option 3 with continuing refinement | [#8248](https://github.com/w3c/csswg-drafts/issues/8248#issuecomment-1361749264) |
| 2023-01-11 | Adopt Option 3 | [#8249](https://github.com/w3c/csswg-drafts/issues/8249#issuecomment-1379326665) |
| 2023-04-19 | Keep the current spec parsing behavior in an Appendix, update the spec to use the lookahead option | [#7961](https://github.com/w3c/csswg-drafts/issues/7961#issuecomment-1514955984) |
| 2023-04-19 | type selector remains required first; &div is invalid | [#8662](https://github.com/w3c/csswg-drafts/issues/8662#issuecomment-1514977935) |
| 2023-07-19 | limits on nesting is ua-defined | [#2881](https://github.com/w3c/csswg-drafts/issues/2881#issuecomment-1642793638) |
| 2023-07-12 | Change CSSStyleRule to inherit from CSSGroupingRule, modulo any discovered compat impact | [#8940](https://github.com/w3c/csswg-drafts/issues/8940#issuecomment-1632829763) |
| 2023-10-18 | We will address ths issue, and fix nesting to allow for bare declarations after nested rules without moving them above. | [#8738](https://github.com/w3c/csswg-drafts/issues/8738#issuecomment-1768977689) |
| 2024-01-17 | contextually-invalid selectors have a specificity of zero | [#9600](https://github.com/w3c/csswg-drafts/issues/9600#issuecomment-1896300197) |
| 2024-05-29 | Introduce a CSSNestedDeclarations object inheriting from CSSRule … It serializes as a raw declaration list. … | [#10234](https://github.com/w3c/csswg-drafts/issues/10234#issuecomment-2137832089) |
| 2025-09-03 | publish new WD of css-nesting | [#12704](https://github.com/w3c/csswg-drafts/issues/12704#issuecomment-3249801090) |

## Key debates

### The syntax wars: five options over two years

The central question of [#7834](https://github.com/w3c/csswg-drafts/issues/7834)
("Syntax Invites Errors") was how to tell a nested *selector* apart from a
*declaration*, given that both can begin with an identifier (`color: …` vs
`color { … }`). The WG enumerated competing options:

- **Option 1** — every nested rule must start with `&` or `@nest` (the
  then-current spec). Backed by [argyleink](../people/argyleink.md),
  [Loirooriol](../people/loirooriol.md), [futhark](../people/futhark.md) and others.
- **Option 3** — a nested selector is recognized because it starts with
  something *other than* an identifier (`&`, `.`, `#`, `:`, a combinator); a
  bare type selector needs `&` or `:is()`. Backed by
  [tabatkins](../people/tabatkins.md), [fantasai](../people/fantasai.md),
  [lea](../people/lea.md), [mirisuzanne](../people/miriam.md).
- **Option 4** (FremyCompany) — a style rule gains an optional third part,
  `selector { declarations } { nested rules }`, chaining nesting *after* the
  declaration block.
- **Option 5** ([plinss](../people/plinss.md)) — an `@nest` at-rule whose body
  holds only nested rules, requiring "no parsing changes, no extra lookahead, no
  changes to OM."

The minutes record [jensimmons](../people/jensimmons.md) arguing against leaving syntax unsettled — *"I
don't really like the idea of us coming up with syntax now and changing later"* —
with [tabatkins](../people/tabatkins.md) adding *"adding new functionality later is fine, adding new
syntaxes for no new functionality is bad"*
([#7834](https://github.com/w3c/csswg-drafts/issues/7834#issuecomment-1292277520)).
The WG took Option 3 over 1 on 2022-10-26, rejected 4 and 5 on 2022-12-21 after
a WebKit author survey ran roughly 80% for Option 3, and formally adopted
Option 3 on 2023-01-11 (straw poll ≈16–2). [plinss](../people/plinss.md) sustained a lone objection
throughout: *"We're blocking ourselves from prepending a property with anything
that's not an ident, and I think we'll regret that"*
([#8248](https://github.com/w3c/csswg-drafts/issues/8248#issuecomment-1361749264)).

### Why the 2021 bracket decision was reverted

In November 2021 the WG had resolved to use a bracket/`@nest`-block syntax and to
prefer *a single* nesting syntax
([#4748](https://github.com/w3c/csswg-drafts/issues/4748#issuecomment-960145492)).
Ten months later it reversed both
([#4748](https://github.com/w3c/csswg-drafts/issues/4748#issuecomment-1233176065)).
Three forces converged: Adam Argyle's author poll came back "incredibly
one-sided" for `&`/`@nest`; and the bracket idea's own co-author,
[mirisuzanne](../people/miriam.md), changed her mind — the minutes record her
saying *"As I was writing it I foudn the brackets more confusing than expected,
and I actually added ampersands for clarity."* [fantasai](../people/fantasai.md)
thought the poll was invalid (it still showed `&`, defeating the purpose of
brackets) but declined to block; the WG resolved only to *undo* the 2021
decision, not to bless the current syntax.

### The parser lookahead relaxation (the technical crux)

Adopting Option 3 left one wart: a bare type selector like `h1 { … }` still
needed `& h1` or `:is(h1)`, because distinguishing `strong:hover { … }` (a rule)
from `strong: hover` (a declaration) needs the parser to read arbitrarily far
ahead — historically avoided for performance
([#7961](https://github.com/w3c/csswg-drafts/issues/7961)). Implementer signals
were split: Gecko's `rust-cssparser` could already restart cheaply
([emilio](../people/emilio.md)), but Blink initially NAK'd it, estimating ~2% of
page-load time (sesse). The breakthrough came from
[andruud](../people/andruud.md) (Blink) on 2023-03-30: rather than infinite
lookahead, *try to parse as a declaration; if that fails, rewind and re-parse as
a rule* — a bounded restart, only triggered when the lookahead token is an
identifier. The earlier blockers had dissolved ("substantial performance
improvements to the tokenizer … removed the CachedTokenizer"). The WG adopted the
lookahead option on 2023-04-19, documenting three future-syntax restrictions (no
semicolons in selectors; nothing after `{}` in a declaration; `--ident` always
starts declaration parsing). This also dissolved [plinss](../people/plinss.md)'s forward-compat
objection, letting [#8249](https://github.com/w3c/csswg-drafts/issues/8249) close
"no change." A side effect: with infinite lookahead available, `&div` was made
invalid again (`div&` required) to protect Sass's `&`-suffix concatenation
([#8662](https://github.com/w3c/csswg-drafts/issues/8662#issuecomment-1514977935)) —
[tabatkins](../people/tabatkins.md) noting the WG *"intentionally do not pay attention to preprocessors
that attempt to lead the spec before browser support is solidified."*

### What `&` means, and the specificity tail it created

`&` was defined broadly: within nesting it is the nesting selector, and
elsewhere it aliases `:scope`
([#5745](https://github.com/w3c/csswg-drafts/issues/5745#issuecomment-1276466934)),
so rules stay portable between nesting, `@scope` and `querySelector`.
Crucially, `&` is implemented as an `:is()`-style reference to the parent
selector list. [emilio](../people/emilio.md)/sesse showed the alternative
(Sass-style textual expansion) is *exponential* — "n rules can cost O(2^n)
memory" — and unimplementable when the parent is a selector list, which killed
the Sass-semantics proposal in
[#8310](https://github.com/w3c/csswg-drafts/issues/8310#issuecomment-1383810771).
But `:is()` flattens specificity, producing author-visible surprises
([#9492](https://github.com/w3c/csswg-drafts/issues/9492)): `button, a.button { … }`
unexpectedly beats `button.primary`, and `& { }` around a pseudo-element parent
breaks because `:is()` can't contain pseudo-elements. [lea](../people/lea.md)
argued to minimize the wart; tabatkins/andruud insisted on uniformity (*"& , &.foo,
& .foo, and .foo & should all be identical wrt specificity"*) and showed real
desugaring is impossible ("3^4 = 81 unique specificities" at depth 4). The one
clean win: contextually-invalid nested selectors were given **zero** specificity
([#9600](https://github.com/w3c/csswg-drafts/issues/9600#issuecomment-1896300197)).
Relatedly, nesting depth was left UA-defined after data showed even the `:is()`
model is exponential in depth (WebKit caps at 128 levels)
([#2881](https://github.com/w3c/csswg-drafts/issues/2881#issuecomment-1642793638)).

### The `@nest` arc: required → removed → CSSOM-only

`@nest` began as a *required* keyword in the 2018 draft (a nested rule started
with `&` or `@nest`). Adopting Option 3 in 2022–2023 removed it as author syntax —
[tabatkins](../people/tabatkins.md) later confirmed *"the removal of @nest and loosening of restrictions on
selectors"*
([#8662](https://github.com/w3c/csswg-drafts/issues/8662#issuecomment-1490915615)).
Note there is **no resolution literally named "remove @nest"**; the removal is
implicit in the Option 3 choice. It then briefly returned as an *internal* CSSOM
`@nest` rule to fix declaration ordering — Chrome 130 and earlier hoisted a bare
declaration written *after* a nested rule above it, silently changing the cascade
([#8738](https://github.com/w3c/csswg-drafts/issues/8738)). The WG resolved to
stop hoisting (2023-10-18), then to represent it in the CSSOM (2024-04-17), and
finally settled on a **non-author-facing** object, `CSSNestedDeclarations`, that
serializes as a bare declaration list
([#10234](https://github.com/w3c/csswg-drafts/issues/10234#issuecomment-2137832089)).
This capped a related CSSOM cleanup: `CSSRuleList` redefined as a read-only
`ObservableArray`
([#8350](https://github.com/w3c/csswg-drafts/issues/8350#issuecomment-1497776457))
and `CSSStyleRule` made to inherit `CSSGroupingRule`
([#8940](https://github.com/w3c/csswg-drafts/issues/8940#issuecomment-1632829763)).

## Related features

- Interacts with `@scope`, `:is()`/`:where()`, `@layer` (cascade layers), and
  Selectors 4 — several nesting resolutions are cross-labeled with those specs.

## Sources

- Discussion & resolutions: the issues linked above, mirrored in
  `raw/data/github/csswg-drafts/`; resolution text from
  `_generated/resolutions-index.md`.
- Status: `raw/data/w3c-api/specifications/css-nesting-1.json`.
- Shipping: vendor primary sources linked in Milestones
  ([WebKit](https://webkit.org/blog/14571/css-nesting-and-the-cascade/),
  [Chrome for Developers](https://developer.chrome.com/blog/css-nesting-relaxed-syntax-update),
  [web.dev](https://web.dev/blog/css-nesting-cssnesteddeclarations)).

---

*This page is an unofficial, LLM-maintained synthesis. It is not a product of
the CSS Working Group. Verify against the linked primary sources.*
