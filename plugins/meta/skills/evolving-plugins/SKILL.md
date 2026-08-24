---
name: evolving-plugins
description: Use automatically in the my-ai-plugins marketplace when a task produces a validated, reusable suggestion for improving its plugins; harvest the suggestion and draft the smallest guarded, testable skill change before finishing.
reviewed: f690474
---

# Evolve plugins

Turn a useful session lesson into a reviewable draft, not trusted doctrine.

1. State the reusable suggestion in one sentence.
2. Reject it if it is uncertain, obvious, one-off, or unrelated to this
   marketplace.
3. Search existing skills. Prefer a small edit over a new skill.
4. Check the target with `git check-attr guard -- <path>`.
5. Draft the smallest change that would have helped earlier in the task.
6. Add or update one behavioral case that proves the change.
7. Run relevant validation and show the result in the final summary.

For `guard=human-only`, do not edit; propose the diff. For
`guard=human-revised`, edit but do not stamp. Never edit a reviewed stamp on
your own work.

Do not harvest secrets, personal data, transient tool behavior, or claims not
verified in the task. Do not broaden permissions or add dependencies as a side
effect.

Use `skill-quality` for the behavioral gate and `editing-this-marketplace` for
packaging.
