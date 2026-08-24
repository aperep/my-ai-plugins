---
name: editing-this-marketplace
description: Use when adding, changing, renaming, removing, validating, or locally testing a skill or plugin in the aperep my-ai-plugins marketplace, especially when an edit does not appear in Codex.
---

# Edit this marketplace

Codex owns the primary wrappers:

```text
.agents/plugins/marketplace.json
plugins/<plugin>/.codex-plugin/plugin.json
plugins/<plugin>/skills/<skill>/SKILL.md
```

Shared skills belong only under `skills/`. Adding one needs no catalog edit.
Adding a plugin needs both a catalog entry and a Codex manifest. Copy an
existing first-party plugin's shape; keep catalog sources as
`./plugins/<plugin>`.

Before editing, run `git check-attr guard -- <path>`. Obey the repository's
`AGENTS.md` guard policy.

## Dev loop

1. Make the smallest change.
2. Bump the version in `.codex-plugin/plugin.json` when plugin content changes.
3. Parse all changed JSON.
4. Reinstall it from the local marketplace:

```sh
codex plugin marketplace add /path/to/my-ai-plugins # once
codex plugin add <plugin>@aperep
```

Start a new thread before judging changed skill routing or text. If an edit is
missing, first confirm that `codex plugin list` points to this checkout and that
the manifest version changed.

Before pushing, perform one local install. Parsing the catalog alone does not
prove that plugin sources resolve.

## Names

Treat plugin and skill names as stable IDs. Prefer changing display text. For a
real rename, search the whole repo and update every catalog, manifest,
cross-reference, and consumer instruction.

Claude Code compatibility is isolated in
[`../../references/claude-code.md`](../../references/claude-code.md). Read that
file only when a change affects the Claude wrapper.
