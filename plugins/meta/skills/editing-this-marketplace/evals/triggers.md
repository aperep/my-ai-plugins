# Trigger tests — editing-this-marketplace

Only the frontmatter `description` is read when deciding to load. These lists
test that text, nothing else.

## Must load

- "add a new plugin to the marketplace"
- "my skill doesn't show up after editing it"
- "the plugin isn't loading"
- "how do I test this before pushing?"
- "rename this plugin"
- "remove a skill from the catalog"
- "where does SKILL.md go in this repo?"
- "install says source path does not exist"

## Must not load

Each line names the skill that should win instead.

| phrasing | should load |
|---|---|
| "is this skill any good?" | `skill-quality` |
| "why does this skill never fire?" | `skill-quality` |
| "add evals for this skill" | `skill-quality` |
| "should this skill exist at all?" | `skill-quality` |
| "should I vendor this third-party skill?" | `trusting-foreign-skills` |
| "pin kepano's skill by sha" | `trusting-foreign-skills` |
| "conflicting manifests on install" | `trusting-foreign-skills` |
| "self-learning wrote a skill, now what?" | `trusting-foreign-skills` |
| "how do I write a good skill?" | `superpowers:writing-skills` |
| "set up a hook in settings.json" | `update-config` |

## Note

This skill is scoped to one repository by name. It is enabled per project, so it
should not be loadable at all outside `my-claude-marketplace` and `dotfiles`.
Absence elsewhere is the correct behaviour, not a trigger failure.
