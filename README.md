---
parent: AGENTS.md
---

# aperep skill marketplace

Codex marketplace whose plugins also implement the portable Agent Plugins 1.0
format. Both formats discover the same `plugins/<name>/skills/` tree.

```text
.agents/plugins/marketplace.json          Codex catalog
plugins/<name>/.codex-plugin/plugin.json  Codex manifest
plugins/<name>/plugin.json                Agent Plugins manifest
plugins/<name>/skills/                    shared Agent Skills
```

## Codex

```sh
codex plugin marketplace add git@github.com:aperep/my-ai-plugins.git --ref main
codex plugin add meta@aperep
```

Install one plugin per skill group. Installation is currently user-level; list a
repository's expected plugins in its `AGENTS.md`.

All functional plugins are available. `obsidian` is intentionally unavailable:
it is an empty placeholder while the need for a separate Obsidian-specific
technical plugin is evaluated.

For local development, register the checkout instead of the Git source:

```sh
codex plugin marketplace add /path/to/my-ai-plugins
```

Do not register both sources under the `aperep` name.

## Agent Plugins

Every plugin directory has a root `plugin.json` targeting Agent Plugins 1.0.
A compatible client can load that directory and discover its immediate
`skills/*/SKILL.md` children. The portable specification does not define a
marketplace or installation command; use the client's package-loading flow.

See [packaging compatibility](docs/DUAL.md) and
[consumer setup](docs/consumer-snippets.md).

## Plugins

### `meta`

Repository documentation trees, maintenance, skill quality, marketplace
editing, trust review, and guarded plugin evolution.

### `dev`

A restrained development workflow covering intake, requirements, debugging,
test-driven implementation, verification, review, and authorized delivery.

### `research`

Precise result extraction, contextual mathematical reasoning, interlinear
review, and opt-in Lean formalization.

### `math-writing`

LaTeX project scaffolding, proofreading, plain English, style cleanup,
authorial voice adaptation, and Russian mathematical translation.

### `biblio`

Bibliography verification, MathSciNet lookup, Zotero maintenance, and personal
publication records.

### `typst`

Idiomatic Typst authoring, LaTeX migration, academic templates, and migration
checks.

### `knowledge`

[Knowledge management](plugins/knowledge/README.md): canonical placement,
safe moves, capture, inbox processing, cross-storage boundaries, and audits.
This plugin subsumes general knowledge-management work.

### `obsidian`

Reserved, empty, and unavailable. A separate plugin should exist only if
concrete Obsidian-specific technical workflows cannot live cleanly in
`knowledge`; that decision remains open on the roadmap.

## Validation

1. Parse the Codex catalog and every manifest as JSON.
2. Validate every root `plugin.json` against the Agent Plugins 1.0 schema and
   every `SKILL.md` against the Agent Skills specification.
3. Install a changed plugin from the local Codex marketplace; catalog
   parsing does not prove that sources resolve.
4. Keep portable and Codex manifest versions synchronized and bump both when
   plugin content changes.
