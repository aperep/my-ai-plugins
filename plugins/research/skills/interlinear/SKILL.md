---
name: interlinear
description: >
  Maintain sentence-tagged LaTeX research documents and their typed annotation
  sidecars. Use for interlinear translations, explanations, local context,
  references, formal status, examples, or annotation views. Not for ordinary
  formatting, informal reasoning, or Lean work.
---

# Interlinear research

Keep three concerns separate:

- `<jobname>.tex` contains author text and stable `\itag` IDs;
- `<jobname>.interlinear.tex` contains document-specific `\ic` records;
- `interlinear.sty` is stable package code and contains no document data.

## Workflow

1. Copy `assets/latex/interlinear.sty` into the LaTeX project or load an
   installed copy. The package automatically inputs
   `<jobname>.interlinear.tex` at the start of the document.
2. Put each labelled sentence or independently meaningful clause on one
   physical source line and append `\itag{dJ2z}`. Generate each four-character
   alphanumeric ID once, keep it unique, and never rewrite it.
3. Store each annotation as
   `\ic{dJ2z}{type}[qualifier]{content}` in the sidecar. Read
   [the data contract](references/schema.md) before editing it.
4. Use [the rendering modes](references/rendering-modes.md) to select a view.
   Semantic comment type and display mode are independent.

## Invariants

- Every `\ic` ID names a source `\itag`; each ID/type pair occurs at most once.
- Types are `translation`, `explanation`, `context`, `reference`, `formal`, or
  `example`. Qualifiers carry language, reference trust, or formal status.
- Mark a reference `checked` only after checking it. Mark formal work `checked`
  only after the named declaration passes the recorded Lean toolchain.
- `reason` writes informal comments; `formalize` writes formal comments only
  after an explicit request. Neither rewrites the source claim.
- Keep generated PDFs and prover artifacts outside the skill sources.
