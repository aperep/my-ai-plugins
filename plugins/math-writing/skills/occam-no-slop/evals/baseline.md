# Baseline failures

Recorded 2026-08-25 against the pre-refactor skill at revision `4420972`.

1. The overview says to check sentence-level slop before structure, while the
   workflow says the reverse. The agent cannot follow both orders.
2. The description loads the skill before finalizing any LLM-assisted passage.
   This catches ordinary drafting and voice work without a de-slopping request.
3. The skill says that `simple-english` is pulled in, but Codex does not install
   that dependency.
4. The generalization rule can change a theorem while mathematical correctness
   is declared out of scope.
5. The skill treats emphasis and lists as suspect without preserving valid
   warnings, orientation, or genuinely parallel items.

The refactor passes when it has one check order, narrow routing, no unavailable
dependency, and an explicit boundary around mathematical changes.
