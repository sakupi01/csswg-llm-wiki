# CSSWG LLM Wiki — Catalog

> *This wiki is an unofficial, LLM-maintained synthesis. It is not a product of the CSS
> Working Group. Verify against the linked primary sources.*

Entry point for every query. One line per page; update on every ingest.

## Features

| Feature | Status | Specs | Summary |
|---|---|---|---|
| [Absolute Lengths & the Pixel Unit](features/absolute-lengths.md) | shipped | css-values-3, css-values-4 | `px` is an angular measure (the reference pixel), not a physical dot; on screen it is the *anchor* and physical units fall out of it — physical-size units repeatedly rejected (#614/#708/#5221) |
| [CSS Nesting](features/css-nesting.md) | shipped | css-nesting-1 | Native nesting of style rules; history dominated by the "syntax wars" (Option 3 + parser lookahead) and the `&`-as-`:is()` specificity tail |
| [CSS Masonry (Grid Lanes)](features/masonry.md) | in-discussion | css-grid-3 | Pinterest-style layout; 5-year debate over Grid-integration vs a separate `display: masonry` settled as `display: grid-lanes` (Nov 2025) — a compromise keeping "grid" in the name |
| [:heading() Selector](features/heading-selector.md) | specified | selectors-5 | Select headings by computed level (not tag), driven by HTML `headingoffset`; fights over class- vs tag-level specificity, `an+b`→list-of-integers reversal (#12599), and whether it follows the a11y tree (#12412) |
| [Scroll-driven Animations](features/scroll-driven-animations.md) | shipping | scroll-animations-1 | Drive animations by scroll/view timelines; 2021 declarative reboot (fantasai/Miriam) replaced the offset+ID model with `animation-timeline: scroll()`/named timelines; 2026 work aligns timeline-name scoping with view transitions |
| [CSS Anchor Positioning](features/anchor-positioning.md) | shipping | css-anchor-position-1, css-anchor-position-2 | Tether a popover/tooltip to an anchor in CSS (`anchor()`, `position-area`, `@position-try`); heavy post-ship renaming (`inset-area`→`position-area`, `anchor-default`→`position-anchor`) and a contested 2025 reversal to follow transforms (#8584) |
| [Container Queries](features/container-queries.md) | shipped | css-conditional-5 | Query an ancestor container's size/style/scroll-state (`@container`, `container-type`, `cq*` units); solved the decade-old circularity by querying a contained ancestor; `@container` picks its container from the query (#6644); moved contain-3→conditional-5 (#10433) |

## Specs

| Spec | Maturity | Features tracked |
|---|---|---|
| [css-nesting-1](specs/css-nesting-1.md) | WD | css-nesting |
| [css-values-3](specs/css-values-3.md) | CRD | absolute-lengths |
| [css-values-4](specs/css-values-4.md) | WD | absolute-lengths |
| [css-grid-3](specs/css-grid-3.md) | WD | masonry |
| [selectors-5](specs/selectors-5.md) | FPWD | heading-selector |
| [scroll-animations-1](specs/scroll-animations-1.md) | WD | scroll-driven-animations |
| [css-anchor-position-1](specs/css-anchor-position-1.md) | WD | anchor-positioning |
| [css-anchor-position-2](specs/css-anchor-position-2.md) | FPWD | anchor-positioning |
| [css-conditional-5](specs/css-conditional-5.md) | WD | container-queries |

## Families

| Family | Members | Theme |
|---|---|---|
| *(none yet)* | | |

## Recent meetings

| Date | Type | Summary |
|---|---|---|
| [2026-07-01](meetings/2026/2026-07-01-telecon.md) | telecon | `:nav-source` pseudo, web-animations range parse-error, non-existing pseudo inheritance, anchor `flip-self-*` for `::picker(select)` |
| [2026-06-25](meetings/2026/2026-06-25-telecon.md) | telecon | `::interest-button` media-query gating voided (reverses 06-11) |
| [2026-06-24](meetings/2026/2026-06-24-telecon.md) | telecon | functional-notation serialization, `@position-try` global scope, `sibling-index()` returns 1, `outline-offset: inset`, `<meta text-scale>` limit reverted |
| [2026-06-17](meetings/2026/2026-06-17-telecon.md) | telecon | scroll-snap physics, logical `caption-side`, `zoom: normal`, `::picker(select)` fallbacks, `param()` ≥2 values |
| [2026-06-11](meetings/2026/2026-06-11-telecon.md) | telecon | `::interest-button` gated behind an inline media condition (later voided) |
| [2026-06-10](meetings/2026/2026-06-10-telecon.md) | telecon | `<a-n-plus-b>` rename, `random()` caching, loosely-matched timeline names, Link Params FPWD, mixins return type |
| [2026-06-03](meetings/2026/2026-06-03-telecon.md) | telecon | `align-content: baseline` unshipped, scroll-timeline async source/fragmented subject, animation-triggers `play-always` |
| [2026-05-28](meetings/2026/2026-05-28-telecon.md) | telecon | shadow-DOM inheritance survey tasked to emilio; `::interest-button` discussed |
| [2026-05-27](meetings/2026/2026-05-27-telecon.md) | telecon | inactive scroll timelines, orthogonal-flow `justify-self: normal`, anchor transforms feature-detect, typed-OM all-or-nothing reification |
| [2026-05-20](meetings/2026/2026-05-20-telecon.md) | telecon | masonry repeat heuristic, highlight shadow cascade, `SnapEvent` nullable init, `path-length` |
| [2026-05-13](meetings/2026/2026-05-13-telecon.md) | telecon | `getTriggers()`, `animation-delay-start/-end` longhands |
| [2026-05-06](meetings/2026/2026-05-06-telecon.md) | telecon | elementFromPoint shadow retargeting, scroll-into-view snap, `light-dark(…, none)`, unresolved timelines as null |

## Digests

Narrative digests published as [RSS/Atom](https://sakupi01.github.io/csswg-llm-wiki/feed.xml)
and [JSON Feed](https://sakupi01.github.io/csswg-llm-wiki/feed.json). Sources in `wiki/digests/`.
Selected by developer impact (would a working web developer want to know this?), not comment count; each topic in a
scannable Background/Why-it-matters/Summary/Related format. Weekly = "This week in CSSWG";
monthly = deeper arcs/contention (`/monthly-digest`).

| Digest | Period |
|---|---|
| [2026-W27](digests/2026-W27.md) (weekly) | 2026-06-28 – 2026-07-05 |
| [June 2026](digests/2026-06.md) (monthly) | 2026-06-01 – 2026-06-30 |

## Not yet ingested

Pilot order complete. Next candidates come from `/triage` — recent leaders without a page
include `scroll-animations` (done), `css-align-3` (align-content baseline unship), `css-forms-1`
(select/`::picker`), `css-values-5` (`random()`, `sibling-index()`). They land here before pages.
