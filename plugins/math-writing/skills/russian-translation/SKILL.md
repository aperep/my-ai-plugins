---
name: russian-translation
description: Translate, draft, or revise Russian mathematical prose in A. Perepechko's authorial voice. Use for articles, thesis chapters, abstracts, theorem prose, and explicit voice adaptation; not for ordinary Russian copyediting or non-mathematical translation.
---

# Russian mathematical prose

Produce faithful Russian mathematical prose in A. Perepechko's restrained,
declarative voice. Project instructions and the user's terminology choices take
priority over this calibration.

## Before writing

Determine the task:

- **translation**: preserve the source's mathematical meaning and structure;
- **revision**: improve existing Russian without silently changing claims;
- **voice adaptation**: change phrasing only, leaving content and notation fixed.

Read [references/voice.md](references/voice.md) for all three modes. For TeX,
also read [references/latex.md](references/latex.md). Read other references only
when the task needs them:

- [references/terminology.md](references/terminology.md) for disputed terms,
  glossary work, or systematic terminology changes;
- [references/long-documents.md](references/long-documents.md) for a long file or
  several files;
- [references/dissertations.md](references/dissertations.md) for dissertation
  structure, contribution statements, acknowledgments, or personal metadata;
- [references/corpus/P18_ru.tex](references/corpus/P18_ru.tex) only when the
  extracted rules do not settle a voice question or the calibration itself is
  being revised.

The corpus is evidence, not a template. Do not copy its subject matter,
notation, metadata, or occasional errors into another project.

## Work

For translation, use two passes:

1. Translate for meaning. Preserve paragraph and statement boundaries, formulas,
   environments, labels, references, citations, and defined-term markup unless
   the user asks to restructure them.
2. Calibrate the Russian prose against the voice reference. Remove literal
   English syntax, but do not add claims, emphasis, or logical transitions that
   are absent from the source.

For revision or voice adaptation, first mark the prose spans that actually
drift. Leave already suitable text alone.

Resolve terminology in this order: the project's glossary and prior usage, the
user's current choice, the terminology reference, then standard Russian
mathematical literature. Flag a real ambiguity instead of choosing silently.

Never repair a suspected mathematical error as a language edit. Preserve it and
report it separately. Make no repository, network, bibliography, or
version-control changes beyond the user's request.

## Check

Compare source and result for lost hypotheses, changed quantifiers, altered
negation, renamed symbols, broken references, and inconsistent terms. For TeX,
use the project's documented build command when available; otherwise discover
the entry point and ask before making a consequential guess. Put generated
files in the project's ignored output directory.

Report what changed, unresolved terminology, suspected source errors, and any
validation not run.
