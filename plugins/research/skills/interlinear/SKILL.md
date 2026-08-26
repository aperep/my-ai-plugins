---
name: interlinear
description: >
  Build or maintain sentence-labelled Typst or LaTeX documents whose shared
  sidecar drives translations, explanations, tag-scoped local context,
  references, formalization status, and review views. Use when asked for an
  interlinear research document, labelled claims, active context, annotation
  presentation, or proof-on-example tracks. Not for ordinary document
  formatting, informal proof work, or Lean formalization itself.
---

# Interlinear research

Treat the labelled source and its CSV as one dataset. Preserve stable labels;
renaming a label changes citations, context ranges, and external annotations.

## Workflow

1. Locate the document, metadata CSV, and any local result index. For a new
   adapter, copy either `assets/typst/interlinear.typ` or
   `assets/latex/interlinear.sty`.
2. Read [references/schema.md](references/schema.md) before changing columns,
   labels, context ranges, or proof-example metadata.
3. Wrap complete mathematical sentences or proof steps in
   `sent("label")[...]` (Typst) or `\sent{label}{...}` (LaTeX). Keep fragments
   that cannot be understood independently in one labelled unit.
4. Run `scripts/validate_interlinear.py` before and after metadata changes.
5. Use the deterministic helpers for mechanical work. Run them with `--help`
   when paths differ from the example:
   - `populate_context.py` proposes `active_until`; writing requires `--write`.
   - `context_dump.py` exports active earlier statements, optionally filtered
     with `--tags definition,setup,...`.
   - `stack_lookup.py` searches a supplied local index; filling requires
     `--fill` and writes only `stacks_candidate`, never a confirmed reference.
   - `gap_check.py` reports proof/claim rows without `example_step`.
6. Review semantic suggestions before writing them. A lexical context span or
   token-overlap result is a lead, not mathematical evidence.

For LaTeX, run `render_latex_data.py` after changing the source or CSV, then
input its generated declarations after loading `interlinear.sty`. Use
[references/rendering-modes.md](references/rendering-modes.md) when choosing a
view.

## Invariants

- Every source label is unique and has exactly one CSV row.
- Every CSV label occurs in the source.
- `active_until` is empty or names the same/later source label.
- Tags are semicolon-delimited. Source lifetime and requested tags jointly
  determine local context; `proof` and `claim` mark example-track steps.
- Candidate matches and generated formal code are not evidence. Only checked
  results enter `stacks_ref` or the `checked` Lean status.
- `reason` may write explanations and examples. `formalize` alone writes formal
  status, and only after the user explicitly requests formal work.
- Keep generated PDFs, images, and context dumps outside the skill sources.
