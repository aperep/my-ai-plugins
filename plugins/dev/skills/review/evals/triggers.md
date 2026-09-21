# Trigger tests — review

## Must load

- “Review the staged diff for bugs before I commit.”
- “Check whether this change introduces regressions or integration gaps.”
- “Review this diff only for over-engineering and tell me what can be deleted.”
- “Review this patch for both correctness and unnecessary complexity.”

## Must not load

- “Write a commit message for this diff.” → ordinary message composition
- “Fix the failing parser test.” → `flow` and `debug`
- “Run the test suite and tell me whether it passes.” → `verify`
- “Audit the whole repository for over-engineering.” → `audit`
