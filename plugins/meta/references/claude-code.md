# Claude Code compatibility

Read this only when changing or testing the Claude wrapper. Shared skills stay
Codex-first.

## Layout

```text
.claude-plugin/marketplace.json
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/
```

Claude and Codex share `skills/`; do not fork skill bodies by host.

## Local development

The Git marketplace is `aperep`; the checkout is registered separately as
`aperep-dev`. Keep those names distinct.

```sh
claude plugin marketplace update aperep-dev
claude plugin install <plugin>@aperep-dev -s project
```

`marketplace update` refreshes only the catalog. Reinstall to copy changed
plugin content. Always use project scope; a bare install changes user scope.

Validate both the catalog and each changed plugin, then install once to prove
that source paths resolve:

```sh
claude plugin validate .
claude plugin validate ./plugins/<plugin>
claude plugin install <plugin>@aperep-dev -s project
```

Claude manifests stay unversioned. Catalog sources are full paths from the
marketplace root: `./plugins/<plugin>`. Do not add `metadata.pluginRoot`.

For a real rename or removal, append the old-to-new mapping to the catalog's
top-level `renames` map.

## Third-party sources

- No upstream `.claude-plugin/plugin.json`: use a pinned `github` source with
  `strict: false` and an explicit `skills` list.
- Upstream has that manifest: use a pinned `git-subdir` source. Combining its
  manifest with `strict: false` causes a conflicting-manifests error.
- A subdirectory is usable only if it is self-contained.

Inspect `claude plugin details <plugin>@aperep-dev`. Plugins with hooks must be
enabled per project, not at user scope.

Claude-only dependencies belong in `.claude-plugin/plugin.json`; never imply
that Codex installs them.

## Auto-evolution

Claude uses the `self-learning` dependency to harvest useful session behavior
into skills. Keep that dependency in `plugins/meta/.claude-plugin/plugin.json`.
Codex instead uses the meta plugin's `SessionStart` hook and `evolving-plugins`
skill. Both produce drafts: review them, run `skill-quality`, and leave them
unstamped until the user confirms them.

`skillforge` may handle large rewrites and `superpowers:writing-skills` may
handle authoring. These are Claude routing names, not shared dependencies.

Claude guard hooks are user-scoped in `~/.claude/settings.json`; they are not
bundled with `meta`. Repository `AGENTS.md` and `.gitattributes` remain
authoritative here.
