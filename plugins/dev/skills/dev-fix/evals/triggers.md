# Trigger tests — dev-fix

## Must load

- “This request intermittently returns stale data; find the cause and fix it.”
- “Why does this regression happen? Do not edit yet.”
- “Reproduce this failing test and repair the underlying bug.”

## Must not load

- “The cause is the missing null guard; add it with a regression test.” → `dev-tdd`
- “Add the specified export endpoint.” → `dev-tdd`
- “Review the proposed fix.” → `dev-review`
