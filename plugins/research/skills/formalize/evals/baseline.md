# Formalize baseline cases

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
