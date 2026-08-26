---
name: interlinear
description: >
  Build or maintain sentence-labelled mathematical documents whose CSV metadata
  drives translations, research comments, local context, Stacks references,
  proof-on-example tracks, and review views. Use for an interlinear research
  document or when asked to label claims, dump active context, or find proof
  steps that have not been checked on an example. Not for ordinary Typst
  formatting without research metadata.
---

# Interlinear research

Treat the labelled source and its CSV as one dataset. Preserve stable labels;
renaming a label changes citations, context ranges, and external annotations.

## Workflow

1. Locate the document, metadata CSV, and any local result index. If starting a
   project, copy `assets/typst/interlinear.typ` and adapt the Noetherian example.
2. Read [references/schema.md](references/schema.md) before changing columns,
   labels, context ranges, or proof-example metadata.
3. Wrap complete mathematical sentences or proof steps in `sent("label")[...]`.
   Keep prose fragments that cannot be understood independently in the same
   labelled unit.
4. Run `scripts/validate_interlinear.py` before and after metadata changes.
5. Use the deterministic helpers for mechanical work. Run them with `--help`
   when paths differ from the example:
   - `populate_context.py` proposes `active_until`; writing requires `--write`.
   - `context_dump.py` exports the active earlier statements at each label.
   - `stack_lookup.py` searches a supplied local index; filling requires
     `--fill` and is only a candidate match, not verification.
   - `gap_check.py` reports proof/claim rows without `example_step`.
6. Review semantic suggestions before writing them. A lexical context span or
   token-overlap result is a lead, not mathematical evidence.

Use [references/rendering-modes.md](references/rendering-modes.md) when choosing
a Typst view. Read [references/roadmap.md](references/roadmap.md) only when
extending the system beyond its implemented phases.

## Invariants

- Every source label is unique and has exactly one CSV row.
- Every CSV label occurs in the source.
- `active_until` is empty or names the same/later source label.
- Tags are semicolon-delimited; `proof` and `claim` mark steps that should have
  an example track.
- Do not present a Stacks tag as confirmed without checking the linked result.
- Keep generated PDFs, images, and context dumps outside the skill sources.
