---
name: speech-style-adaptation
description: >
  Draft or adapt English mathematical prose in A. Perepechko's authorial
  voice, calibrated from the bundled jems4.tex. Use when explicitly asked to
  match this voice in an article, thesis chapter, abstract, or theorem prose;
  not for ordinary drafting, proofreading, de-slopping, simple-English
  rewriting, or Russian prose.
metadata:
  reviewed: 1ee66dd
---

# English mathematical voice

Write or revise English mathematical prose in A. Perepechko's restrained,
declarative voice. Project instructions and the user's current choices take
priority over this calibration.

Read [references/voice.md](references/voice.md) for every task. Read other
references only when the task needs them:

- [references/latex.md](references/latex.md) for TeX source;
- [references/introductions.md](references/introductions.md) for an article,
  thesis, part, or chapter introduction.

Consult [jems4.tex](references/corpus/jems4.tex) only when the extracted rules
do not settle a voice question or the calibration itself is being revised. The
corpus is evidence, not a template: do not copy its subject matter, notation,
metadata, or occasional errors into another project.

## Work

Preserve mathematical content, notation, TeX structure, references, and the
source's uncertainty unless the user asks to change them. Change only prose
that does not match the voice. Leave prose that already fits it alone.

Use a connective only when its logical relation is true. Never import
corpus-specific notation or terminology.

If the user also requests structural de-slopping, apply `occam-no-slop` first
and this voice pass second.

Preserve and report suspected mathematical errors. Confirm contribution claims
and factual metadata; never derive them from the corpus.

## Check and report

Check for changed mathematics, broken references, and inconsistent terms. For
TeX, use the project's build instructions. Report the scope, validation,
suspected defects, and unresolved author decisions.
