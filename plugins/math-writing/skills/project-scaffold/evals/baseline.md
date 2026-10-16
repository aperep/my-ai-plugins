# Baseline failure

Recorded 2026-09-03 against reviewed revision `d9f00dd` while merging four
recent arXiv source bundles.

The skill did not say how to merge package lists. The sources used both
`fullpage` and `geometry`, and both `enumerate` and `enumitem`; a literal union
would silently choose overlapping layout and list controls. The revision
passes when it preserves the current baseline, groups additions, and comments
out new or mutually exclusive packages by default.

## Typst scaffold, 2026-10-16

At `12c9682`, `assets/typst/` contained only reserved comments and no usable
article or notation.
The separate Typst skill's pattern scanner passed its full slide example,
but Typst 0.15.1 rejected `angle.l` and `angle.r` as unknown symbol modifiers.
Checking only for LaTeX patterns could not establish that the templates worked.

The scaffold now needs real English and Russian builds exercising every
notation macro, theorem counters across sections and subsections, native
references and citations, and proof symbols without changes leaking to
later proofs.
