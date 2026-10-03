---
name: interlinear
description: >
  Maintain sentence-labelled Typst or LaTeX research documents whose shared
  sidecar drives translations, explanations, tag-scoped context, references,
  formal status, and review views. Use for labelled claims, active-context
  dumps, annotation presentation, or proof-on-example tracks. Not for ordinary
  formatting, informal reasoning, or Lean work.
---

# Interlinear research

Treat the labelled source and its CSV as one dataset. Preserve stable labels;
renaming a label changes citations, context ranges, and external annotations.

## Workflow

1. For a new document, copy `assets/typst/interlinear.typ` or
   `assets/latex/interlinear.sty`. Read
   [references/schema.md](references/schema.md) before changing metadata.
2. Make each labelled unit one complete sentence or independently meaningful
   clause. In LaTeX, keep it on one physical source line and append
   `\itag{dJ2z}`. Generate each four-character alphanumeric ID once,
   keep it unique, and never rewrite it. In Typst, wrap the same unit in
   `sent("dJ2z")[...]`.
3. Run `scripts/validate_interlinear.py` before and after metadata changes.
4. Use the helpers for mechanical work:
   - `populate_context.py` proposes `active_until`; writing requires `--write`.
   - `context_dump.py` exports active earlier statements, optionally filtered
     with `--tags definition,setup,...`.
   - `stack_lookup.py` searches a supplied local index; filling requires
     `--fill` and writes only `stacks_candidate`, never a confirmed reference.
   - `gap_check.py` reports proof/claim rows without `example_step`.
5. Review semantic suggestions before writing them. Lexical spans and
   token-overlap matches are leads, not mathematical evidence.

For LaTeX, run `render_latex_data.py` after changing the source or CSV, then
input its generated declarations after loading `interlinear.sty`. Use
[references/rendering-modes.md](references/rendering-modes.md) when choosing a
view. Keep annotation behavior in `interlinear.sty`; source lines contain only
the author text and `\itag`. Do not use `\tag`, which belongs to
`amsmath` equation numbering.

## Invariants

- Source labels and CSV rows correspond one-to-one; labels are unique and
  stable. New labels are random four-character alphanumeric IDs.
- `active_until` is empty or names the same/later source label.
- Tags are semicolon-delimited. Source lifetime and requested tags jointly
  determine local context; `proof` and `claim` mark example-track steps.
- Only checked results enter `stacks_ref` or the `checked` Lean status.
  `reason` writes informal fields; `formalize` writes formal status after an
  explicit request.
- Keep generated PDFs, images, and context dumps outside the skill sources.
