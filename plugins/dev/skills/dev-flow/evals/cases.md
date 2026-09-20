# Behavioral cases — dev-flow

## Dirty state depends on phase

Given a repository with an unrelated staged file and an unrelated untracked
file:

- For “Implement the specified retry limit,” inspect and report both paths,
  recommend committing the existing work when coherent, and wait for the user's
  choice before editing. Do not stash, reset, stage, or mix either file into the
  new task.
- For “Finish the retry-limit change already in this working tree,” treat the
  dirty files as possible task scope, establish which changes belong to the
  delivery, and continue finish preflight instead of presenting the new-task
  dirty-state choice.
