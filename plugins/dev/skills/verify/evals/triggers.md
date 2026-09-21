# Trigger tests — verify

## Must load

- “Verify that the implemented change satisfies these acceptance criteria.”
- “Before calling this fixed, rerun the original reproduction.”
- “What completion claims are actually supported by the current checks?”

## Must not load

- “Review this diff for design and correctness problems.” → `review`
- “Fix the failing checks.” → `debug` or `tdd`, depending on diagnosis
- “Commit and push the verified change.” → `flow`
