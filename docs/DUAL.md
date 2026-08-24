# Codex and Claude Code compatibility

Skills have one copy. Host-specific catalogs and manifests wrap it:

```text
.agents/plugins/marketplace.json
.claude-plugin/marketplace.json
plugins/<plugin>/
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  skills/
```

Keep host-specific commands and paths out of shared skills. Prefer capability
wording such as “run a command” or “search the web,” and resolve bundled files
relative to `SKILL.md`.

## Status

| plugin | Codex | Claude Code | blocker |
|---|---|---|---|
| `meta` | available | available | shared text still contains some Claude terminology |
| `latex` | unavailable | validation fails | two invalid YAML descriptions |
| `biblio` | unavailable | validation fails | two invalid YAML descriptions |
| `typst` | unavailable | validation fails | one invalid YAML description |
| `obsidian` | unavailable | available | Claude-only third-party dependencies |

The invalid descriptions are in:

- `latex/russian-translation`;
- `latex/speech-style-adaptation`;
- `biblio/bibliography-check`;
- `biblio/extracting-precise-results`;
- `typst/typst`.

## Packaging differences

Codex plugin installation is user-level. A consumer repository may record its
required plugins in `AGENTS.md`; it does not install them automatically.

Claude supports project-scoped enablement and plugin dependencies. Codex
manifests currently have no matching dependency field, so do not claim that a
companion skill is installed. Keep dependent plugins unavailable or provide a
fallback.

Claude manifests remain unversioned. Codex manifests use semantic versions and
must be bumped when shared content or Codex metadata changes.

## Before enabling a Codex plugin

1. Make its shared skills host-neutral.
2. Validate both host wrappers.
3. Change its catalog policy to `AVAILABLE`.
4. Bump its Codex version.
5. Test a local install and start a new session.
