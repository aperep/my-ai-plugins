# my-claude-marketplace

Private Claude Code plugin marketplace, named `aperep`. Skill sets, enabled per repository on demand. 

```
.claude-plugin/marketplace.json   catalog
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

## Setup on a new machine

Use an SSH remote. A key loaded in `ssh-agent` authenticates both manual installs and background auto-updates; HTTPS does not, because the background refresh disables credential helpers for its pull.

```sh
claude plugin marketplace add aperep/my-claude-marketplace
claude plugin install meta@aperep
```

The repo is `aperep/my-claude-marketplace`; the marketplace it declares is
`aperep`, which is the half that shows up in `enabledPlugins` as `latex@aperep`.

For per-repository enabling, see `docs/consumer-snippets.md`.
For Claude Code on the web, see `docs/cloud-setup.md`.

## Versioning

No `plugin.json` declares a `version`. For a git-hosted marketplace this means every commit is treated as a new version, 
which is what you want for something edited continuously.

If you ever add a `version` field, the plugin is pinned to that string and pushing commits does nothing for existing installs until you bump it. 
Also avoid setting `version` in both `plugin.json` and the marketplace entry: the manifest value always wins, silently.

## Development loop

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

## Third-party skills

Do not vendor them. Either add the upstream marketplace alongside this one, or
list their repo as an entry here:

```json
{
  "name": "their-skills",
  "source": { "source": "github", "repo": "someone/skills-repo", "sha": "…" },
  "strict": false,
  "skills": ["./skills/wanted-one", "./skills/wanted-two"]
}
```

`strict: false` plus an explicit `skills` array works when the upstream repo
ships bare `SKILL.md` files with no manifest of its own, and lets you expose only
the subset you want. Pin `sha` for anything you did not write: a skill is a
prompt executed with your tool permissions, and a plugin can also carry hooks and
MCP servers.

## Migration checklist

- [ ] Move each skill set out of its old repo into the matching `plugins/*/skills/`
- [ ] Delete the submodules and the injection script from every target repo
- [ ] Add `.claude/settings.json` to each target repo (`docs/consumer-snippets.md`)
- [ ] Remove any now-stale `.claude/skills/` copies the script left behind
- [ ] Confirm `.gitignore` in target repos does not exclude `.claude/settings.json`
