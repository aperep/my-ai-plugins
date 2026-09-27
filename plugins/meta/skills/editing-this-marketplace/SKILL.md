---
name: editing-this-marketplace
description: Use when adding, changing, renaming, removing, validating, or locally testing a skill or plugin in the aperep my-ai-plugins marketplace, especially when an edit does not appear in Codex.
---

# Edit this marketplace

Each plugin has Codex and portable wrappers around one skill tree:

```text
.agents/plugins/marketplace.json
plugins/<plugin>/.codex-plugin/plugin.json
plugins/<plugin>/plugin.json
plugins/<plugin>/skills/<skill>/SKILL.md
```

Shared skills belong only under `skills/`. Adding one needs no catalog edit.
Adding a plugin needs a catalog entry plus both manifests. Copy an existing
first-party plugin's shape; keep catalog sources as `./plugins/<plugin>`.

Before editing, run `git check-attr guard -- <path>`. Obey the repository's
`AGENTS.md` guard policy.

## Dev loop

1. Make the smallest change.
2. Bump the synchronized version in `.codex-plugin/plugin.json` and root
   `plugin.json` when plugin content changes.
3. Parse all changed JSON, validate root `plugin.json` against its declared
   Agent Plugins schema, and run `skills-ref validate` on each skill.
4. Reinstall it from the local Codex marketplace:

```sh
codex plugin marketplace add /path/to/my-ai-plugins # once
codex plugin add <plugin>@aperep
```

Start a new thread before judging changed skill routing or text. If an edit is
missing, first confirm that `codex plugin list` points to this checkout and that
the manifest version changed.

Before pushing, perform at least one local install. Install additional changed
plugins when their Codex-specific shape or source layout differs; parsing the
catalog alone does not prove that sources resolve.

Agent Plugins 1.0 discovers skills only from immediate children of `skills/`
and does not define marketplaces or plugin dependencies. Keep portable
packages self-contained or document them as unavailable.

Agent Skills allow repository-specific data only inside `metadata`. Keep a
guard mirror at `metadata.human-revised`, never as a custom top-level field.
Read `metadata.reviewed` as a legacy alias, but do not write new stamps there.

## Names

Treat plugin and skill names as stable IDs. Prefer changing display text. For a
real rename, search the whole repo and update every catalog, manifest,
cross-reference, and consumer instruction.
