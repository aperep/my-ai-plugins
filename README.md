# my-claude-marketplace

Private dual-purpose Claude Code and Codex plugin marketplace, named `aperep`.
The skill directories are shared; each host gets only its own catalog and
plugin manifest wrapper. See `docs/DUAL.md` for compatibility boundaries and
installation options.

```
.claude-plugin/marketplace.json   catalog
.agents/plugins/marketplace.json  Codex catalog
plugins/
  meta/                           Rules for self-modifying, editing skills etc
  latex/                          LaTeX proofreading, journal style, formulas
  biblio/                         Bibliography and everything related
  obsidian/                       Working with obsidian vaults
  typst/                          Working with Typst, a lightweight Latex alternative
docs/                             setup snippets, skill template
scripts/setup-cloud-auth.sh       cloud sandbox git auth
```

Each plugin holds its skills under `plugins/<name>/skills/<skill-name>/SKILL.md`.
See `docs/SKILL-template.md` for the file shape.

Each first-party plugin has parallel manifests:

```
plugins/<name>/.claude-plugin/plugin.json
plugins/<name>/.codex-plugin/plugin.json
```

## Setup on a new machine

### Claude Code

Use an SSH remote. A key loaded in `ssh-agent` authenticates both manual installs and background auto-updates; HTTPS does not, because the background refresh disables credential helpers for its pull.

```sh
claude plugin marketplace add aperep/my-claude-marketplace
claude plugin install meta@aperep
```

The repo is `aperep/my-claude-marketplace`; the marketplace it declares is
`aperep`, which is the half that shows up in `enabledPlugins` as `latex@aperep`.

For per-repository enabling, see `docs/consumer-snippets.md`.
For Claude Code on the web, see `docs/cloud-setup.md`.

### Codex

Use the SSH URL so the private repository uses the key already loaded in
`ssh-agent`:

```sh
codex plugin marketplace add git@github.com:aperep/my-claude-marketplace.git --ref main
codex plugin add latex@aperep
```

The Codex catalog contains wrappers for all five local plugins. Only `meta` is
currently installable without changing shared skills. `latex`, `biblio`,
and `typst` remain unavailable because five existing skill descriptions fail
strict YAML parsing in both hosts' per-plugin validators; `obsidian` is
unavailable because it contains only Claude-specific third-party dependencies.
See `docs/DUAL.md` for the blockers and both installation scenarios.

## Versioning

No `plugin.json` declares a `version`. For a git-hosted marketplace this means every commit is treated as a new version, 
which is what you want for something edited continuously.

If you ever add a `version` field, the plugin is pinned to that string and pushing commits does nothing for existing installs until you bump it. 
Also avoid setting `version` in both `plugin.json` and the marketplace entry: the manifest value always wins, silently.

## Claude Code development loop

Two registrations of the same catalog:

| name | source | what it serves |
|---|---|---|
| `aperep` | github `aperep/my-claude-marketplace` | `origin/main` |
| `aperep-dev` | directory `~/my-claude-marketplace` | the on-device working tree |

They coincide most of the time; `aperep-dev` is what makes a skill edit visible
without a commit. Add the dev one by hand in `~/.claude/settings.json` — the
name under `extraKnownMarketplaces` wins over the `name` in `marketplace.json`,
which `claude plugin marketplace add <path>` does not let you override:

```json
"aperep-dev": {
  "source": { "source": "directory", "path": "/home/sage/my-claude-marketplace" }
}
```

After edits: `claude plugin marketplace update aperep-dev` then `/reload-plugins`.

Before pushing anything that touched `marketplace.json`, install from
`aperep-dev`. `claude plugin validate` does not check that `source` paths exist;
install is the only thing that resolves them.

The rest of the rules — renames, versioning, why `metadata.pluginRoot` must stay
out — live in the `meta` plugin as
`plugins/meta/skills/editing-this-marketplace/SKILL.md`, so they are in context
when a session is actually editing a skill.

## Claude Code third-party skills

Do not vendor them. Either add the upstream marketplace alongside this one, or
list their repo as an entry here. Which form depends on what upstream ships.

**Upstream has no manifest** (bare `SKILL.md` files) — `strict: false` plus an
explicit `skills` array exposes only the subset you want:

```json
{
  "name": "their-skills",
  "source": { "source": "github", "repo": "someone/skills-repo", "sha": "…" },
  "strict": false,
  "skills": ["./skills/wanted-one", "./skills/wanted-two"]
}
```

**Upstream has its own `plugin.json`** — the above fails at load with
"conflicting manifests", because components are then declared on both sides. Use
`git-subdir` to take one skill directory instead, as `defuddle` does:

```json
{
  "name": "defuddle",
  "source": {
    "source": "git-subdir",
    "url": "git@github.com:kepano/obsidian-skills.git",
    "path": "skills/defuddle",
    "sha": "…"
  }
}
```

It sparse-clones that path alone, so nothing else from their repo lands on disk.
Use the SSH URL — git over HTTPS to github.com is blocked in this environment.

Pin `sha` either way for anything you did not write: a skill is a prompt executed
with your tool permissions, and a plugin can also carry hooks and MCP servers.
A plugin of yours can then `dependencies: ["their-entry"]` to pull it in
automatically — same marketplace, so no cross-marketplace allowlist is needed.

## Migration checklist

- [ ] Move each skill set out of its old repo into the matching `plugins/*/skills/`
- [ ] Delete the submodules and the injection script from every target repo
- [ ] Add `.claude/settings.json` to each target repo (`docs/consumer-snippets.md`)
- [ ] Remove any now-stale `.claude/skills/` copies the script left behind
- [ ] Confirm `.gitignore` in target repos does not exclude `.claude/settings.json`
