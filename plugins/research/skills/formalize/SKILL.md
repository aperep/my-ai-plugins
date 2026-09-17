---
name: formalize
description: >
  Formalize or verify a selected statement in Lean, optionally using Aristotle
  to propose code. Use only for an explicit request for formalization, Lean,
  Aristotle, or machine-checked proof. Not for informal explanation, examples,
  or gap analysis.
---

# Formalize a selected claim

Identify the exact claim and assumptions. For a paper-sized request, map the
published results and external proof dependencies, then choose a small first
target with the user. Exclude commented-out source material from that map.

## Inputs and evidence

For labelled documents, use `interlinear/scripts/context_dump.py` to collect
active definitions, assumptions, and earlier statements. Record the target and
source location; report missing context instead of guessing it.

Keep generated artifacts outside the source document:

- Lean source with a stable declaration name;
- the exact Lean version or pinned project revision;
- checker output or a concise failure log;
- any Aristotle request and result needed to reproduce the attempt.

## Tool boundary

Prefer the project's Lean toolchain. Use Aristotle only when the user or
project selects it. Its output remains `generated` until Lean accepts the
recorded declaration without `sorry` or an equivalent placeholder.

When Aristotle is selected, read [the round-trip workflow](references/aristotle.md).
It supplies a pinned SDK helper for explicit input snapshots, resumable jobs,
result retrieval, and local acceptance. A missing API key blocks the live job,
not local scaffolding or Lean checking. Never infer proof acceptance from a
successful build alone: check the target's original type and transitive axioms.

## Result states

Use the shared interlinear schema exactly:

- `planned`: target and route identified; no code claimed;
- `generated`: Lean or Aristotle produced code that has not passed the checker;
- `checked`: the recorded declaration passed the recorded Lean toolchain;
- `failed`: the checker rejected the artifact; keep the useful diagnostic in
  `lean_note`.

For `checked`, record `lean_ref` and `lean_toolchain`. Preserve the source
claim: report added hypotheses, weakened conclusions, counterexamples, and
translation mismatches explicitly. Update the sidecar only after preserving
the evidence artifact; examples and citations are not formal verification.
