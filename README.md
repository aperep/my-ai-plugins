# my-claude-marketplace

Private Claude Code plugin marketplace. Skill sets, enabled per repository on demand. 

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
claude plugin marketplace add CHANGEME/my-claude-marketplace
claude plugin install meta-tools@my-claude-marketplace
```

For per-repository enabling, see `docs/consumer-snippets.md`.
For Claude Code on the web, see `docs/cloud-setup.md`.

## Versioning

No `plugin.json` declares a `version`. For a git-hosted marketplace this means every commit is treated as a new version, 
which is what you want for something edited continuously.

If you ever add a `version` field, the plugin is pinned to that string and pushing commits does nothing for existing installs until you bump it. 
Also avoid setting `version` in both `plugin.json` and the marketplace entry: the manifest value always wins, silently.

## Development loop

TODO: rules in this section belong to meta plugin. They are suggested by AI, not mine. Feel free to discard, modify etc.

Editing skills through the git source means a push for every experiment. Instead register the working copy under a second, dev-only marketplace name:

```sh
claude plugin marketplace add ./my-claude-marketplace   # names itself from marketplace.json
```

Note that each user can register only one marketplace per `name`, so a local copy
using the same `name` replaces the git one. To run both side by side, keep a
branch whose `marketplace.json` sets `"name": "my-claude-marketplace-dev"`, or
just accept the swap while developing and re-add the git source afterwards.

After edits:

```sh
claude plugin marketplace update my-claude-marketplace
/reload-plugins
```

### Before every push

```sh
claude plugin validate .
```

Validates `marketplace.json` schema, duplicate plugin names, and source path
traversal. Point it at a plugin directory instead to check that plugin's skill,
agent, and hook frontmatter:

```sh
claude plugin validate ./plugins/math-latex
```


### Renaming

A plugin's `name` is its stable identifier — it appears in every consumer's
`enabledPlugins`. To change the displayed label, add `displayName` and leave
`name` alone. If you must rename or remove, add an entry to the top-level
`renames` map in `marketplace.json` so existing installs migrate instead of
erroring. Treat that map as append-only.

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
