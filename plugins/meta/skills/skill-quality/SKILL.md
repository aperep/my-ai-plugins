---
name: skill-quality
description: >
  Use when shipping a new skill or changing an existing one, and when asked
  whether a skill is any good, whether it is worth writing at all, why it never
  fires or fires on the wrong thing, or which model it was tested on. Runs a
  RED/GREEN behavioral gate with fresh subagents, checks the description for
  trigger collisions against the installed roster, and records the result per
  model in the skill's evals/ directory. For where the files go and how to ship
  them, see editing-this-marketplace.
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

Assume the model already knows the skill format — Anthropic's authoring guidance
says so outright. Content that a fresh Claude could have derived is dead weight;
what earns its place is this repo's traps and the bar set here. File shape and
paths: `editing-this-marketplace`. Frontmatter: `docs/SKILL-template.md`.

## GREEN

Dispatch a second fresh subagent on sonnet, skill loaded, same task. It must
clear every line of `evals/baseline.md`. For a line that survives, fix the skill
or delete the line and admit the skill does not cover it. A partial pass is not
a pass.

## Trigger tests

The `description` is the only text read when deciding whether to load, so the
tests target it. Name concrete triggers — file types, phrasings the user
actually says, the task shape. Aspirational prose there means the skill never
fires.

Two lists in `evals/triggers.md`: phrasings that **must** load the skill, and
phrasings that **must not**.

Build the second list from the installed roster, not from imagination. A skill
about writing competes with `superpowers:writing-skills`. One about repo layout
competes with `editing-this-marketplace`. `skillforge` competes with anything
skill-shaped, by its own admission in the catalog entry. Stealing a trigger is
worse than never firing, because it displaces something that worked.

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

## Skills nobody has read

A skill written by a harvester or lifted from elsewhere is a prompt that steers
the next session without having been read. It earns a stamp the way any other
does — it clears the gates above, the user reads it, the user confirms. Never
stamp a skill you wrote yourself.

The guard rules themselves are in the global `CLAUDE.md`; do not restate them.
Where such skills come from and what to do on arrival: `trusting-foreign-skills`.
