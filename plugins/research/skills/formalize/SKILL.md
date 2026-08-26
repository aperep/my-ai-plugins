---
name: formalize
description: >
  Formalize or verify an explicitly selected mathematical statement in Lean,
  optionally using Aristotle to propose Lean code. Use only when the user
  explicitly asks for formalization, Lean, Aristotle, or machine-checked proof.
  Not for ordinary proof explanation, examples, or informal gap analysis.
---

# Formalize a selected claim

Formal work is opt-in. Identify the exact claim and assumptions before writing
code; a nearby informal theorem is not permission to formalize the whole
document.

## Inputs and evidence

For a labelled interlinear document, use the sibling
`interlinear/scripts/context_dump.py` helper to collect the active definitions,
assumptions, and earlier statements. Record the target label and the source
location. If the context is insufficient, report the missing definition or
hypothesis instead of guessing it.

Keep generated artifacts outside the source document:

- Lean source with a stable declaration name;
- the exact Lean version or pinned project revision;
- checker output or a concise failure log;
- any Aristotle request/result needed to reproduce the attempt.

## Tool boundary

Prefer the project's existing local Lean toolchain. Use Aristotle only when the
user names it or project instructions select it. Treat Aristotle output as a
proposal: it becomes checked evidence only after Lean accepts the recorded
declaration without `sorry` or an equivalent placeholder.

## Result states

Use the shared interlinear schema exactly:

- `planned`: target and route identified; no code claimed;
- `generated`: Lean or Aristotle produced code that has not passed the checker;
- `checked`: the recorded declaration passed the recorded Lean toolchain;
- `failed`: the checker rejected the artifact; keep the useful diagnostic in
  `lean_note`.

For `checked`, record `lean_ref` and `lean_toolchain`. Never change the
mathematical statement merely to make the checker pass. Report added
hypotheses, weakened conclusions, counterexamples, and translation mismatches
as explicit differences from the source claim.

Update the sidecar only after preserving the evidence artifact. Do not convert
an informal example check or a cited theorem into formal verification.
