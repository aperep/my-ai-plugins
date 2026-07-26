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
needs a new entry in `marketplace.json` plus its own `plugin.json`.

## Dev loop

Editing through the git source means a push per experiment. Register the working
copy instead:

```sh
claude plugin marketplace add ./my-claude-marketplace   # names itself from marketplace.json
```

One marketplace per `name` per user: a local copy using `name: "aperep"`
*replaces* the git one. To run both, keep a branch whose `marketplace.json` sets
`"name": "aperep-dev"`, or accept the swap and re-add the git source after.

After edits:

```sh
claude plugin marketplace update aperep
/reload-plugins
```

If a skill still does not appear, the cause is almost always the manifest, not
the file: wrong `source` path, plugin missing from `plugins[]`, or the plugin
not enabled in this repo's `.claude/settings.json`.

## Before every push

```sh
claude plugin validate .                    # catalog: schema, dupes, path traversal
claude plugin validate ./plugins/latex      # one plugin: skill/agent/hook frontmatter
```

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
