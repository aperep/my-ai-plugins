# Trigger tests — skill-quality

Only the frontmatter `description` is read when deciding to load. These lists
test that text, nothing else.

## Must load

- "is this skill any good?"
- "should I write a skill for this at all?"
- "why does my skill never fire?"
- "this skill triggers on the wrong things"
- "which model was this skill tested on?"
- "run the gate before I ship this skill"
- "the description isn't specific enough"
- "add evals for this skill"

## Must not load

Each line names the skill that should win instead.

| phrasing | should load |
|---|---|
| "where does the SKILL.md file go?" | `editing-this-marketplace` |
| "my new skill doesn't show up" | `editing-this-marketplace` |
| "how do I push this plugin?" | `editing-this-marketplace` |
| "rename a plugin without breaking installs" | `editing-this-marketplace` |
| "is this GitHub skill safe to install?" | `trusting-foreign-skills` |
| "pin this third-party skill by sha" | `trusting-foreign-skills` |
| "self-learning just wrote a skill" | `trusting-foreign-skills` |
| "install failed with conflicting manifests" | `trusting-foreign-skills` |
| "write a skill that does X" | `superpowers:writing-skills` |
| "rewrite this skill from scratch" | `skillforge` (this skill hands off) |
| "audit our CLAUDE.md" | `claude-md-management` |
| "simplify this code" | `code-simplifier` |

## Known collision

`skillforge`'s description claims "create a skill", "improve the X skill" and
"which skill should I use", which covers most of the must-load list above. The
cost is accepted, not solved — see the catalog entry. If routing goes wrong in
practice, that is the first place to look, not this description.
