---
name: reason
description: >
  Analyze a mathematical claim or proof informally or semiformally from its
  labelled local context. Use to explain a proof step, expose assumptions, test
  an example, find a gap, or write informal interlinear metadata. Not for
  copyediting, literature extraction, or Lean/formal prover work.
---

# Reason through mathematics

Keep the claim fixed. An explanation is not evidence that its argument is
correct.

## Context

For an interlinear document, identify the target `\itag`, read its typed
comments from `<jobname>.interlinear.tex`, and inspect the earlier tagged source
lines it actually invokes. An earlier annotation is not automatically a
hypothesis.

State the context actually used:

- definitions and assumptions;
- earlier statements invoked;
- the exact claim or proof step under review.

For unlabelled text, extract the same three parts directly. Do not invent local
conventions.

## Reasoning output

Give the shortest useful chain from the active assumptions to the claim.
Mark separately:

- a valid inference;
- a plausible but unchecked step;
- a missing hypothesis or genuine gap;
- a check on a concrete example, which cannot prove the general claim.

In an interlinear sidecar, write only `explanation`, `context`, or `example`
comments. Update the existing ID/type record rather than adding a duplicate.
Preserve IDs and the source claim; propose stronger hypotheses or corrections
separately.

Never set Lean status. For an explicit Lean or Aristotle request, hand the
exact claim, assumptions, and gap to `formalize`.
