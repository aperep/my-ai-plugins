---
name: editing-this-marketplace
description: >
  Use when adding, editing, renaming, or removing a skill or plugin in the
  aperep marketplace (the my-claude-marketplace repo), and when a skill or
  plugin "doesn't show up" after an edit. Covers the local dev loop, the
  validation that must run before every push, versioning, renames, and where the
  files go. For third-party or harvested skills, see trusting-foreign-skills.
---

# Editing this marketplace

Repo layout: `.claude-plugin/marketplace.json` is the catalog; each plugin is
`plugins/<name>/` with its own `.claude-plugin/plugin.json` and
`skills/<skill-name>/SKILL.md`. Frontmatter template: `docs/SKILL-template.md`.
Whether a skill is any good: `skill-quality`.

Adding a skill to an existing plugin needs no manifest edit. Adding a *plugin*
needs a new entry in `marketplace.json` plus its own `plugin.json`.

Each `source` is a full path from the marketplace root: `"./plugins/latex"`.
Do **not** reintroduce `metadata.pluginRoot` — this Claude Code version ignores
it and still resolves sources against the root, so `"./latex"` fails at install
with "Source path does not exist" while passing every validation.

## Dev loop

The same catalog is registered twice: `aperep` from github (`origin/main`) and
`aperep-dev` as a directory source on the working tree.

```sh
claude plugin marketplace update aperep-dev      # catalog only
claude plugin install meta@aperep-dev -s project # re-copies the plugin content
```

`marketplace update` refreshes the *catalog* and nothing else. Cached plugin
content lives in a directory named for HEAD's sha
(`~/.claude/plugins/cache/aperep-dev/<plugin>/<sha>/`), so with HEAD unchanged it
is considered current and an uncommitted edit does not propagate — the skill
keeps loading its previous text while the file on disk says otherwise. Re-install
to force the copy. Verified: editing a `description`, running `marketplace
update`, and re-linting showed the old string until the install ran.

Always pass `-s project`. A bare `claude plugin install` writes
`enabledPlugins` at **user** scope, which silently re-enables a plugin that is
deliberately scoped per repo.

The two names must differ — one marketplace per `name` per user, so a local copy
calling itself `aperep` *replaces* the git-hosted one. The name comes from the
key under `extraKnownMarketplaces` in `~/.claude/settings.json`, which overrides
the `name` in `marketplace.json`; `claude plugin marketplace add <path>` has no
`--name` flag and would register the working tree as `aperep`. Never edit the
`name` field to get a dev copy — that changes what every consumer installs.

`meta` and `skillforge` are enabled per repo, in this repo's
`.claude/settings.json` and in `dotfiles`, not at user scope. A description is
preloaded into every session exactly when its plugin is enabled, and these three
skills are useful only where prompt content is edited. Consumer repos declare
`aperep` and enable what they use; see `docs/LOG.md`.

If a skill still does not appear, the cause is almost always the manifest, not
the file: wrong `source` path, plugin missing from `plugins[]`, or the plugin
not enabled in this repo's `.claude/settings.json`.

## Before every push

```sh
claude plugin validate .                          # catalog: schema, dupes, path traversal
claude plugin validate ./plugins/latex            # one plugin: skill/agent/hook frontmatter
claude plugin install latex@aperep-dev -s project # the only check that resolves sources
```

Expect one "No version specified" warning per plugin. That is deliberate; see
Versioning.

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

A skill that names another skill in prose is not type-checked. After any rename
or move, grep for the old path — a stale cross-reference is this layout's
characteristic failure.
