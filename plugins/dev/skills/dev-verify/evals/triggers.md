# Trigger tests — dev-verify

## Must load

- “Verify that the implemented change satisfies these acceptance criteria.”
- “Before calling this fixed, rerun the original reproduction.”
- “What completion claims are actually supported by the current checks?”

## Must not load

- “Review this diff for design and correctness problems.” → `dev-review`
- “Fix the failing checks.” → `dev-fix` or `dev-tdd`, depending on diagnosis
- “Commit and push the verified change.” → `dev-flow`
