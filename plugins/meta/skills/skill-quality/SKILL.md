---
name: skill-quality
description: >
  Use before shipping a new skill or changing an existing one, and when asked
  whether a skill is any good, whether it is worth writing at all, why it never
  fires, or which model it was tested on. Runs a RED/GREEN behavioral gate with
  fresh subagents, checks triggers for collisions against the installed roster,
  and records the result per model in the skill's evals/ directory. This is the
  proof step, not the authoring step: superpowers:writing-skills covers how to
  write one, editing-this-marketplace covers where the files go.
---

# Skill quality

A skill is done when a fresh agent demonstrably does better with it than
without it. The gates below produce that evidence.

## RED

Dispatch one subagent on sonnet, ignorant of the proposed skill, on the real
task.

- **It succeeded.** There is no gap. Say so and stop. Do not write the skill.
- **It failed.** Record each failure in `evals/baseline.md` as the wrong action
  it took, never as "it lacked context". A failure you cannot state that way is
  not testable. This list is now the whole specification.

## Write against the failures

Write from `evals/baseline.md` alone. Anything that traces to no recorded
failure is speculation. Cut it.

Two rules the authoring skills do not cover:

- One skill, one job. Two jobs means two triggers competing for one description.
- Say what to do, not what to avoid. A prohibition with no replacement gets
  rationalized around.

File shape, paths and manifests: `editing-this-marketplace`.

## GREEN

Dispatch a second fresh subagent on sonnet, skill loaded, same task. It must
clear every line of `evals/baseline.md`. For a line that survives, fix the skill
or delete the line and admit the skill does not cover it. A partial pass is not
a pass.

## Trigger tests

The `description` is the only text read when deciding whether to load, so the
tests target it. Two lists in `evals/triggers.md`: phrasings that **must** load
the skill, and phrasings that **must not**.

Build the second list from the installed roster, not from imagination. A skill
about writing competes with `superpowers:writing-skills`. One about repo layout
competes with `editing-this-marketplace`. Stealing a trigger is worse than never
firing, because it displaces something that worked.

## Adversarial pass

Findings confirmed by the reasoning that produced them are worthless. Dispatch
one subagent to **refute** the GREEN result: a phrasing where the skill
misfires, an instruction it contradicts, a case where following it gives the
worse answer. What it refutes returns to RED. What survives is evidence.

## Model records

One row per run in `evals/TESTED.md`. A skill tested on one model is tested on
one model.

| model | date | skill commit | RED reproduced | GREEN cleared | notes |
|---|---|---|---|---|---|
| claude-sonnet-5 | 2026-08-02 | a1b2c3d | 3/3 | 3/3 | — |
| claude-haiku-4-5 | 2026-08-02 | a1b2c3d | 3/3 | 1/3 | ignores condition-first rule |

A row behind HEAD is stale. Re-run the gates, or mark the row.

## Hand off a large rewrite

For a rewrite from nothing, or one that restructures a skill rather than
correcting it, hand the build to `skillforge`. It carries the triage, tiered
spec, lint and ecosystem-collision stages this skill does not. Then return here:
the gates above decide whether the result ships, and `evals/` is where this
marketplace keeps the evidence.

## Harvested skills

`self-learning` writes skills without asking, so its output is a prompt the user
has never read that already steers the next session. It lands on
`surface=human-revised` with **no stamp**, which makes it report as never
reviewed at every session start.

Do not stamp it. A harvested skill earns a stamp the way any other does: it
clears the gates above, the user reads it, the user confirms. Until then the
reminder is the only thing between an unread guess and a permanent instruction.

`SKILL.md` and `references/` are `surface=human-revised`, so a review falls due
once they drift. See the global `CLAUDE.md`.
