# Trigger tests — dev-review

## Must load

- “Review the staged diff for bugs before I commit.”
- “Check whether this change introduces regressions or integration gaps.”

## Must not load

- “Write a commit message for this diff.” → ordinary message composition
- “Fix the failing parser test.” → `dev-flow` and `dev-fix`
- “Run the test suite and tell me whether it passes.” → `dev-verify`
