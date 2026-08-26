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

For an interlinear document, identify the target label and use
`interlinear/scripts/context_dump.py` to collect active earlier rows. Filter by
relevant tags; an earlier annotation is not automatically a hypothesis.

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

In an interlinear sidecar, write only informal fields such as `explanation`,
`example_subject`, and `example_step`. Preserve labels and the source claim;
propose stronger hypotheses or corrections separately.

Never set Lean status. For an explicit Lean or Aristotle request, hand the
exact claim, assumptions, and gap to `formalize`.
