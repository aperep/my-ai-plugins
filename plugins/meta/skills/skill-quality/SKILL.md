---
name: skill-quality
description: Use when deciding whether a skill is needed, reviewing a new or changed skill, diagnosing missed or false triggers, or recording behavioral eval results before shipping it.
---

# Skill quality

A skill earns its place only when it fixes a repeatable failure.

## Gate

1. Run representative tasks without the skill. If they already succeed, stop.
2. Record observable failures in `evals/baseline.md`.
3. Write the least instruction that addresses those failures.
4. Run the same tasks with the skill. Every recorded failure must clear.
5. Try one nearby task that must not load the skill.

Use fresh context for meaningful tests. A subagent is useful when contamination
would invalidate the result; otherwise test directly.

## Writing rules

- One skill, one job.
- Put concrete trigger phrases and task shapes in `description`; routing sees it
  before the body.
- Prefer positive actions to bare prohibitions.
- Delete advice that does not trace to a baseline failure or a repository trap.
- Check nearby installed skills for trigger collisions.

Keep must-load and must-not-load cases in `evals/triggers.md`. When model
behavior matters, record the exact model, date, skill revision, and result in
`evals/TESTED.md`. Results become stale when the skill changes.

Use `skill-creator` for a substantial build or rewrite, then apply this gate.
Use `editing-this-marketplace` for packaging and installation.

Repository `AGENTS.md` and `.gitattributes` define content-guard policy.
