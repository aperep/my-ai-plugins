# Development baseline

Apply these principles proportionally to the requested work.

## Establish facts first

Inspect the request, repository instructions, relevant code, tests, and current
Git state before asking the user for information already available locally.
Ask only when a missing answer changes behavior, a public contract,
authorization, or a difficult-to-reverse action. State consequential
assumptions; do not present inference or an unrun check as fact.

## Make the smallest coherent change

Implement only requested behavior and its necessary integration. Reuse current
project patterns. Do not add speculative flexibility, opportunistic refactors,
or unrelated formatting. Every changed line should be attributable to the
request.

## Preserve other work

Identify the actual repository, branch, working tree, and index before writes.
Keep unrelated edits and partial staging intact. A dirty tree is not itself a
blocker; unclear ownership or destructive scope is.

## Match evidence to the claim

Choose the smallest check that proves the requested outcome, scaled to risk and
blast radius. Distinguish static checks, tests, simulations, rendered UI, real
services, and production evidence. Report failures, skipped checks, and limits.
Reuse still-current evidence instead of rerunning commands ceremonially.

User instructions and repository policy override workflow defaults. Existing
authorization permits necessary in-scope steps, not unrelated publication,
cleanup, or destructive operations.
