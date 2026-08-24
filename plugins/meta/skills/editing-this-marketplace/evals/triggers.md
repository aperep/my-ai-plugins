# Trigger tests — editing-this-marketplace

## Must load

- "add a plugin to this marketplace"
- "my edited skill does not show up in Codex"
- "check this Codex plugin before pushing; there is no validate command"
- "rename a marketplace plugin"
- "where does SKILL.md go in this repo?"
- "does the meta plugin own Claude guard hooks, or are they user-wide?"

## Must not load

| phrasing | should load |
|---|---|
| "is this skill useful?" | `skill-quality` |
| "is this third-party plugin safe?" | `trusting-foreign-skills` |
| "write a new Codex skill" | `skill-creator` |
| "create a new Codex plugin" | `plugin-creator` |
