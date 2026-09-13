# Trigger tests — dev-start

## Must load

- “Start by understanding whether this is a bug or a requested behavior change.”
- “Triage this development request before touching code.”
- “I know something is wrong, but I do not yet know whether the requirement or implementation is wrong.”

## Must not load

- “The parser drops escaped commas; reproduce it and find the cause.” → `dev-fix`
- “Add the already-specified retry limit, test first.” → `dev-tdd`
- “Review the staged diff.” → `dev-code-review`
- “Run the relevant checks and tell me whether this is complete.” → `dev-verify`
- “Commit these two files and push the branch.” → `dev-finish`
