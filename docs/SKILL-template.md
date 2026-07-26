Template for `plugins/<plugin>/skills/<skill-name>/SKILL.md`.
Kept in docs/ so it is not loaded as a real skill.

---
name: skill-name
description: >
  One paragraph. This is the only text Claude sees when deciding whether to
  load the skill, so name the concrete triggers: file types, phrasings the
  user actually uses, the task shape. Be specific rather than aspirational.
---

# Skill name

Instructions go here. Supporting material lives alongside SKILL.md:

    skills/skill-name/
    ├── SKILL.md
    ├── references/     # loaded on demand, keeps SKILL.md short
    └── scripts/        # helper scripts, referenced by relative path
