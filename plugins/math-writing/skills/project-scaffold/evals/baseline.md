# Baseline failure

Recorded 2026-09-03 against reviewed revision `d9f00dd` while merging four
recent arXiv source bundles.

The skill did not say how to merge package lists. The sources used both
`fullpage` and `geometry`, and both `enumerate` and `enumitem`; a literal union
would silently choose overlapping layout and list controls. The revision
passes when it preserves the current baseline, groups additions, and comments
out new or mutually exclusive packages by default.
