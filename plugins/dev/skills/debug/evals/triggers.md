# Trigger tests — debug

## Must load

- “This request intermittently returns stale data; find the cause and fix it.”
- “Why does this regression happen? Do not edit yet.”
- “Reproduce this failing test and repair the underlying bug.”

## Must not load

- “The cause is the missing null guard; add it with a regression test.” → `tdd`
- “Add the specified export endpoint.” → `tdd`
- “Review the proposed fix.” → `review`
