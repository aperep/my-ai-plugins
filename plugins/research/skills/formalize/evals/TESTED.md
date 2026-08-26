# Formalize test status

On 2026-08-26, revision `ac7d6c0` was installed locally as
`research@aperep` version `0.4.1` and tested in fresh context with
`gpt-5.6-sol` under Codex 0.149.1.

- A natural-language request to formalize and compile a selected Lean lemma
  selected `research:formalize`; no `$formalize` spelling was required.
- Given plausible Aristotle output with no checker run, the behavior case used
  `generated`, not `checked`, and required a stable declaration, exact Lean
  toolchain, and successful checker output.
- An ordinary proof-explanation case selected `research:reason`, not
  `formalize`.

No local Lean executable or Aristotle connection was available, so an actual
formal proof run remains untested.
