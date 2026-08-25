---
name: speech-style-adaptation
description: >
  Draft or adapt English mathematical prose in A. Perepechko's authorial
  voice, calibrated from the bundled jems4.tex. Use when explicitly asked to
  match this voice in an article, thesis chapter, abstract, or theorem prose;
  not for ordinary drafting, proofreading, de-slopping, simple-English
  rewriting, or Russian prose.
---

# English mathematical voice

Write or revise English mathematical prose in A. Perepechko's restrained,
declarative voice. Project instructions and the user's current choices take
priority over this calibration.

Read [references/voice.md](references/voice.md) for every task. Read other
references only when the task needs them:

- [references/latex.md](references/latex.md) for TeX source;
- [references/introductions.md](references/introductions.md) for an article,
  thesis, part, or chapter introduction;
- [references/project-work.md](references/project-work.md) for protected source
  material, a long file, or several files.

Consult [jems4.tex](jems4.tex) only when the extracted rules do not settle a
voice question or the calibration itself is being revised. The corpus is
evidence, not a template: do not copy its subject matter, notation, metadata,
or occasional errors into another project.

## Work

Preserve claims, hypotheses, quantifiers, uncertainty, notation, formulas,
environments, labels, references, citations, and defined-term markup unless the
user asks to change them. For revision, edit only prose that drifts from the
voice; do not normalize sound prose merely to increase the number of signature
phrases.

Use logical connectives only when the relation is true. Do not turn every
sentence into a connective-led sentence or import corpus-specific macros and
terminology.

If the user also requests structural de-slopping, apply `occam-no-slop` first
and this voice pass second. Use `proofreading-pass` for a separate copyedit; do
not silently broaden voice adaptation into one.

Never repair a suspected mathematical error as a style edit. Preserve it and
report it separately. Confirm contribution statements, funding, affiliation,
acknowledgments, and contact details instead of deriving them from the corpus.

## Check and report

Compare source and result for changed mathematics, broken references, and
inconsistent terminology. For TeX, use the project's own build instructions
when available and report any validation not run.

Summarize the scope changed, any suspected source defects, and any decisions
that still need the author.
