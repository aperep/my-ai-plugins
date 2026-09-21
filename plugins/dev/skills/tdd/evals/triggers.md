# Trigger tests — tdd

## Must load

- “Implement these acceptance criteria, with meaningful tests first.”
- “Refactor this behavior without changing its observable result.”
- “We know the defect is the off-by-one boundary; fix it with a regression test.”

## Must not load

- “Something corrupts this state; investigate why.” → `debug`
- “Clarify what this feature should do.” → `grill-docs`
- “Verify the existing implementation without editing it.” → `verify`
