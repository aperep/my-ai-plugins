# aperep skill marketplace

Codex-first marketplace with Claude Code compatibility. Each plugin is a
selectable skill group; both hosts share `plugins/<name>/skills/`.

```text
.agents/plugins/marketplace.json       Codex catalog
.claude-plugin/marketplace.json        Claude compatibility catalog
plugins/<name>/.codex-plugin/          Codex manifest
plugins/<name>/.claude-plugin/         Claude manifest
```

## Codex

```sh
codex plugin marketplace add git@github.com:aperep/my-claude-marketplace.git --ref main
codex plugin add meta@aperep
```

Install one plugin per skill group. Installation is currently user-level; list a
repository's expected plugins in its `AGENTS.md`.

Only `meta` is currently available. `latex`, `biblio`, and `typst` have invalid
YAML descriptions; `obsidian` depends on Claude-only third-party plugins. See
`docs/DUAL.md`.

For local development, register the checkout instead of the Git source:

```sh
codex plugin marketplace add /path/to/my-claude-marketplace
```

Do not register both sources under the `aperep` name.

## Claude Code compatibility

```sh
claude plugin marketplace add aperep/my-claude-marketplace
claude plugin install meta@aperep
```

See `docs/consumer-snippets.md` for project scope and `docs/cloud-setup.md` for
Claude Code on the web.

## Validation

1. Parse both catalogs and all manifests as JSON.
2. Validate every plugin with both hosts.
3. Install from the local marketplace; catalog validation does not resolve
   plugin sources.
4. Bump a Codex manifest version when its content changes.
