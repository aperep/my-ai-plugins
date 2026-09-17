# Formalize baseline cases

## Executable pipeline (2026-09-17)

In `comal-lean`, the 0.4.1 skill supplied evidence states but no executable
Aristotle workflow. The installed official SDK 2.1.0 has no
`Project.prove_from_file`; its CLI `show` waits on running tasks, and
`Project.get_files` can return the input archive when no result exists.

Expected: explicit immutable upload, persisted project ID, single status poll,
result-only fetch, and local target/axiom checks before proof acceptance.
Test request/result boundaries in `scripts/test_aristotle.py`. A live round
trip still requires credentials; offline tests are not live service evidence.

## Generated is not checked

**Task.** Send a labelled lemma to Aristotle and record the result.

**Failure without the skill.** Mark the lemma verified when Aristotle returns
plausible Lean code that has not been checked locally.

**Expected behavior.** Store the artifact as `generated`; use `checked` only
after the recorded Lean toolchain accepts the exact declaration.

## Preserve the source statement

**Task.** Formalize a claim whose proof needs an extra hypothesis.

**Failure without the skill.** Add the hypothesis in Lean and report that the
source claim was verified.

**Expected behavior.** Keep the changed formal theorem separate, record the
hypothesis mismatch, and leave the source claim unchecked.

## Limit formalization scope

**Task.** Formalize one selected statement in a long labelled section.

**Failure without the skill.** Attempt to translate the whole section or its
background prose into Lean.

**Expected behavior.** Load only the target and active dependencies, then
produce one stable declaration and its evidence.
