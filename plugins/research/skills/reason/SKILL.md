---
name: reason
description: >
  Analyze a mathematical claim or proof informally or semiformally using its
  labelled local context. Use when asked to explain a proof step, expose hidden
  assumptions, work through an example, find a gap, or write explanation and
  example metadata for an interlinear document. Not for copyediting,
  literature-result extraction, or Lean/formal prover work.
---

# Reason through mathematics

Keep the claim fixed while testing the route to it. Distinguish an explanation
of an argument from evidence that the argument is correct.

## Context

For an interlinear document, identify the target label and read the source plus
its CSV schema. Use the sibling `interlinear/scripts/context_dump.py` helper to
collect earlier rows whose source span is active. Filter by the tags relevant
to the task; do not treat every earlier annotation as a hypothesis.

State the context actually used:

- definitions and assumptions;
- earlier statements invoked;
- the exact claim or proof step under review.

If the document is not labelled, extract the same three parts directly from
the supplied text. Do not invent missing local conventions.

## Reasoning output

Give the shortest useful chain from the active assumptions to the claim.
Mark separately:

- a valid inference;
- a plausible but unchecked step;
- a missing hypothesis or genuine gap;
- a check on a concrete example, which cannot prove the general claim.

When asked to update an interlinear sidecar, write only informal fields such as
`explanation`, `example_subject`, and `example_step`. Preserve labels and the
source claim. Suggest stronger hypotheses or corrected claims as separate
proposals rather than silently editing them in.

Do not set Lean status or describe a statement as formally verified. If the
user explicitly asks for Lean or Aristotle, hand the exact claim, assumptions,
and identified gap to `formalize`.
