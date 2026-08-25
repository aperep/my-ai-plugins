---
name: russian-translation
description: Translate, draft, or revise Russian mathematical prose in A. Perepechko's authorial voice. Use for articles, thesis chapters, abstracts, theorem prose, and explicit voice adaptation; not for ordinary Russian copyediting or non-mathematical translation.
reviewed: 116b54e
---

# Russian mathematical prose

Produce faithful Russian mathematical prose in A. Perepechko's restrained,
declarative voice. Project instructions and the user's terminology choices take
priority over this calibration.

Read [references/voice.md](references/voice.md) for every task. For TeX,
also read [references/latex.md](references/latex.md). Read other references only
when the task needs them:

- [references/terminology.md](references/terminology.md) for disputed terms,
  glossary work, or systematic terminology changes;
- [references/metadata.md](references/metadata.md) for contribution statements,
  affiliation, funding, acknowledgments, or other author metadata;
- [references/corpus/P18_ru.tex](references/corpus/P18_ru.tex) only when the
  extracted rules do not settle a voice question or the calibration itself is
  being revised.

The corpus is evidence, not a template. Do not copy its subject matter,
notation, metadata, or occasional errors into another project.

## Work

Translate directly into the calibrated voice. Preserve paragraph and statement
boundaries, formulas, environments, labels, references, citations, and
defined-term markup unless the user asks to restructure them. Remove literal
English syntax without adding claims, emphasis, or logical transitions.

For revision or voice adaptation, change only prose that drifts.

Resolve terminology in this order: the project's glossary and prior usage, the
user's current choice, the terminology reference, then standard Russian
mathematical literature. Flag a real ambiguity instead of choosing silently.

Never repair a suspected mathematical error as a language edit. Preserve it and
report it separately.

## Check

Compare source and result for lost hypotheses, changed quantifiers, altered
negation, renamed symbols, broken references, and inconsistent terms. Validate
TeX with the project's build instructions when available.

Report what changed, unresolved terminology, suspected source errors, and any
validation not run.
