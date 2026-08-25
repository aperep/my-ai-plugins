# Trigger cases

## Must load

- “Adapt this algebraic-geometry abstract to Perepechko's English voice.”
- “Rewrite this theorem discussion in my established English authorial style.”
- “Bring this thesis chapter into the voice calibrated from `jems4.tex`.”
- “Draft the local motivation for this chapter in Perepechko's style.”

## Must not load

| Request | Expected handling |
|---|---|
| “Proofread this paper for grammar and LaTeX errors.” | `proofreading-pass` |
| “Cut the AI slop and needless case splits from this proof.” | `occam-no-slop` |
| “Rewrite this paragraph in simple English.” | `simple-english` |
| “Translate this theorem into Russian in Perepechko's voice.” | `russian-translation` |
| “Check whether this proof is correct.” | mathematical review |
| “Write a generic cover letter for this submission.” | ordinary drafting unless voice matching is explicit |

## Behavioral cases

- Preserve a genuine hedge expressing an unproved expectation.
- Retain project notation that differs from `jems4.tex`.
- Improve voice locally without reorganizing an otherwise sound proof.
- Use a connective only when its logical relation is supported.
- Ask for or flag unknown contribution, funding, affiliation, or contact facts.
- Use only project-supplied build and source-ownership rules.
