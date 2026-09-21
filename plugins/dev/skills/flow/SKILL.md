---
name: flow
description: Govern an end-to-end development change from a safe start through requirements, investigation, implementation, and verified delivery. Use when asked to begin, perform, resume, or finish a code change, including explicit Ponytail, YAGNI, or simplest-solution requests that change code. Do not use for review-only, verification-only, or commit-message-only requests.
---

# Flow

Carry one development change from its actual current phase to the requested
outcome. Enter at start, continuation, or finish; do not replay completed phases
or turn the flow into ceremony.

## Start safely

Read the request and repository instructions first. If the user explicitly
selected `no-git`, do not run Git commands. Otherwise inspect the repository
root, branch or detached HEAD, working tree, index, remotes, upstream, and
worktrees only as relevant.

Before changing files for a new task, stop on pre-existing staged, unstaged, or
untracked work. Report its paths and staging state, recommend committing it
first when it forms a coherent checkpoint, and ask whether to commit it,
preserve it while continuing, or isolate the new task in a worktree. Do not
stash, reset, discard, or mix it into the new task. If the new task overlaps
those files, resolve ownership before editing. Dirty state that belongs to work
being continued or finished is input to the task, not a reason to restart this
choice.

Establish or reuse one session-scoped Git mode:

- `no-git`: run no Git commands.
- `approval`: the default; read-only Git inspection is allowed, but branch,
  worktree, staging, commit, push, merge, and PR mutations require approval.
- `checkpoint-push`: commit only task-owned, coherent passing checkpoints and
  push them to the established upstream.
- `branch`: create or use a task branch and commit coherent passing
  checkpoints; push only when the selected delivery requires it.
- `worktree`: create an isolated task branch and worktree, then use `branch`
  semantics there.

An explicit mode selection authorizes its listed routine actions for the
session; do not ask for the same permission again. Preserve narrower user and
repository constraints. Establish base branch, task branch, worktree path,
remote, and final destination only when the selected mode needs them. The final
destination may remain undecided until delivery.

## Align and route

Briefly establish the observable outcome, evidence that will count as done, and
active Git mode. Inspect relevant code and documentation before asking
questions. Ask one focused question at a time, and only when the answer changes
behavior, scope, acceptance, or the safe working setup.

- Use `grill-docs` when intended behavior or material scope remains unclear.
- Use `debug` when established behavior is broken and the cause needs
  investigation.
- Use `tdd` when the desired behavior and correction are understood.
- Use `review` or `verify` directly when the request is limited to that
  phase.
- When choosing or changing implementation structure, read
  [Occam](../../references/occam.md).

A feasibility spike produces findings, not production code. Keeping a
prototype is a new implementation decision. If implementation uncovers a
material product decision or substantially larger scope, stop the affected
work, explain the change, and return to the appropriate route. Do not interrupt
for routine implementation details supported by repository conventions.

The active Git mode remains binding in downstream work. In
`checkpoint-push`, checkpoint after a cohesive passing behavior, before a risky
pivot, or before a handoff—not after every edit. Never include unrelated user
changes.

## Finish the actual result

Inspect the exact files or commits being delivered. Verify the promised outcome
against the current state with checks proportional to its risk, and obtain any
requested or repository-required review. Existing evidence is reusable only
when it covers that exact state. A failed required check blocks a claim of
verified delivery, but explicitly requested preservation or a draft PR may
still proceed with the failure disclosed.

Apply the active mode:

- `no-git`: perform no Git operation; report files and evidence.
- `approval`: perform only already authorized mutations. If the user gave a
  generic finish request, complete preflight and ask for the single missing
  delivery decision.
- `checkpoint-push`: make and push any final coherent checkpoint to the known
  upstream.
- `branch` or `worktree`: execute the already selected local merge, push/PR, or
  preservation. If none was selected, ask once which outcome is wanted.

For a commit, inspect the exact staged diff, stage only authorized paths or
hunks, and preserve unrelated index entries. A commit does not imply a push
outside modes that authorize one. Never force-push by default.

For a local merge, establish the real target, verify the target checkout, merge
only the intended work, and check the merged result. Do not hide a pull or push
inside the merge. For a PR, confirm remote, source branch, and base; avoid a
duplicate PR; use the repository template; and disclose unresolved failures.
A requested PR authorizes the push needed to publish its branch.

Preserve a worktree after opening a PR. Remove only a task-owned worktree after
verified integration or explicitly confirmed discard, and never force removal
over uncommitted or untracked files. Destructive cleanup requires the exact
branch, commits, path, contents at risk, and user authorization.

Report the achieved outcome, verification evidence, Git destination or retained
location, and any material unfinished work. A launched command, existing PR, or
passing check on a different state is not completion evidence.
