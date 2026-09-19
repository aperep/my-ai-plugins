---
parent: README.md
---

# Codex and Agent Plugins compatibility

Skills have one copy. Codex and the portable format wrap it:

```text
.agents/plugins/marketplace.json
plugins/<plugin>/
  .codex-plugin/plugin.json
  plugin.json
  skills/
```

Keep client-specific commands and cache paths out of shared skills. Prefer
capability wording such as “run a command” or “search the web,” and resolve
bundled files relative to `SKILL.md`.

## Status

| plugin | Codex | Agent Plugins 1.0 | note |
|---|---|---|---|
| `meta` | available | compatible | — |
| `math-writing` | available | compatible | — |
| `biblio` | available | compatible | — |
| `research` | available | compatible | — |
| `typst` | available | compatible | — |
| `dev` | available | compatible | — |
| `knowledge` | available | compatible | canonical knowledge-management plugin |
| `obsidian` | unavailable | manifest only | empty pending a justified technical scope |

The previously malformed first-party skill descriptions were normalized during
the academic-workshop migration.

The `extracting-precise-results` skill lives in `research`.

## Packaging differences

Codex plugin installation is user-level. A consumer repository may record its
required plugins in `AGENTS.md`; it does not install them automatically.

Agent Plugins 1.0 defines a root manifest and fixed discovery locations for
skills and MCP servers. It defines neither a marketplace nor plugin
dependencies. Keep dependent plugins unavailable, make them self-contained, or
provide a fallback.

Keep the version in root `plugin.json` synchronized with the Codex manifest.
Bump both when shared content or package metadata changes.

## Before enabling a plugin

1. Make its shared skills client-neutral.
2. Validate the portable manifest, every shared skill, and the Codex wrapper.
3. Change its Codex catalog policy to `AVAILABLE`.
4. Synchronize and bump both manifest versions.
5. Test a local Codex install and start a new session.
