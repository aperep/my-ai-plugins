---
name: editing-this-marketplace
description: >
  Use when adding, editing, renaming, or removing a skill or plugin in the
  aperep marketplace (the my-claude-marketplace repo), when a skill "doesn't
  show up" after an edit, or when deciding whether a third-party skill should
  be vendored. Covers the local dev loop, validation before push, versioning,
  renames, and the file shape of a skill.
---

# Editing this marketplace

Repo layout: `.claude-plugin/marketplace.json` is the catalog; each plugin is
`plugins/<name>/` with its own `.claude-plugin/plugin.json` and
`skills/<skill-name>/SKILL.md`.

## Adding a skill

```
plugins/<plugin>/skills/<skill-name>/
├── SKILL.md        # frontmatter: name, description
├── references/     # loaded on demand, keeps SKILL.md short
└── scripts/        # referenced by relative path
```

The `description` is the *only* text seen when deciding whether to load the
skill. Name concrete triggers: file types, phrasings actually used, task shape.
Aspirational prose there means the skill never fires. Full template:
`docs/SKILL-template.md`.

Adding a skill to an existing plugin needs no manifest edit. Adding a *plugin*
needs a new entry in `marketplace.json` plus its own `plugin.json`, then a
`scripts/dev-marketplace.sh` re-run.

Each `source` is a full path from the marketplace root: `"./plugins/latex"`.
Do **not** reintroduce `metadata.pluginRoot` — this Claude Code version ignores
it and still resolves sources against the root, so `"./latex"` fails at install
with "Source path does not exist" while passing every validation.

## Dev loop

Editing through the git source means a push per experiment. `dev/` is a second
marketplace over the same working tree: `dev/plugins` symlinks to `../plugins`,
and `dev/.claude-plugin/marketplace.json` is the real catalog with the name
swapped to `aperep-dev`, generated and gitignored.

The name swap is load-bearing. One marketplace per `name` per user, so a local
copy calling itself `aperep` *replaces* the git-hosted one.

```sh
./scripts/dev-marketplace.sh                    # after adding/removing a plugin
claude plugin marketplace add "$PWD/dev"        # once per machine
claude plugin marketplace update aperep-dev && /reload-plugins
```

Skill edits need none of it — the symlink serves them live; `/reload-plugins`
suffices.

If a skill still does not appear, the cause is almost always the manifest, not
the file: wrong `source` path, plugin missing from `plugins[]`, or the plugin
not enabled in this repo's `.claude/settings.json`.

## Before every push

```sh
claude plugin validate .                    # catalog: schema, dupes, path traversal
claude plugin validate ./plugins/latex      # one plugin: skill/agent/hook frontmatter
claude plugin install latex@aperep-dev      # the only check that resolves sources
```

`validate` never checks that a `source` path exists — a catalog pointing at
nothing passes clean. Install from `aperep-dev` before pushing anything that
touched `marketplace.json`; `claude plugin details latex@aperep-dev` then prints
the component inventory it actually loaded.

## Versioning

No `plugin.json` declares a `version`. For a git-hosted marketplace every commit
is then a new version — correct for something edited continuously. Adding
`version` pins the plugin to that string: pushes do nothing for existing installs
until it is bumped. Never set `version` in both `plugin.json` and the marketplace
entry — the manifest value wins, silently.

## Renaming

`name` is the stable identifier; it lives in every consumer's `enabledPlugins`.
To change the label, add `displayName` and leave `name` alone. A real rename or
removal needs an entry in the top-level `renames` map in `marketplace.json` so
existing installs migrate instead of erroring. That map is append-only.

## Third-party skills

Do not vendor them into `plugins/`. This marketplace holds only skills written
here; anything upstream (superpowers, brainstorming, and friends) is added as its
own marketplace, or listed as an entry pointing at its repo with a pinned `sha`
and `strict: false`. A skill is a prompt executed with your tool permissions, and
a plugin can also carry hooks and MCP servers — pin what you did not write.
