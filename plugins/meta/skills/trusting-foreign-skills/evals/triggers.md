# Trigger tests — trusting-foreign-skills

Only the frontmatter `description` is read when deciding to load. These lists
test that text, nothing else. This skill exists because these phrasings
previously loaded nothing.

## Must load

- "is this GitHub skill safe to install?"
- "should I vendor this skill or pin it?"
- "pin this third-party skill by sha"
- "install failed with conflicting manifests"
- "git-subdir or strict:false for this entry?"
- "self-learning just wrote a skill, now what?"
- "this skill was written automatically, has anyone read it?"
- "what does this plugin actually execute?"
- "update the pinned sha for defuddle"

## Must not load

Each line names the skill that should win instead.

| phrasing | should load |
|---|---|
| "is this skill any good?" | `skill-quality` |
| "run RED/GREEN on this skill" | `skill-quality` |
| "why does my skill never fire?" | `skill-quality` |
| "add a plugin of mine to the catalog" | `editing-this-marketplace` |
| "my own skill doesn't show up" | `editing-this-marketplace` |
| "how do I push this?" | `editing-this-marketplace` |
| "rename my plugin" | `editing-this-marketplace` |
| "write a new skill for X" | `superpowers:writing-skills` |
| "harvest this session into a skill" | `self-learning` |

## Boundary worth watching

`self-learning` *writes* the harvested skill; this skill decides what happens to
it afterwards. If "remember this as a skill" starts loading this one instead of
`self-learning`, the description has over-reached — it must claim the arrival of
an unread skill, never the act of harvesting.
