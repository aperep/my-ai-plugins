# Dual Claude Code and Codex packaging

This repository uses additive host wrappers around one shared skill tree. A
skill, its scripts, references, assets, and evals have one canonical copy under
`plugins/<plugin>/skills/`. Claude Code and Codex metadata do not share a
schema, so each plugin carries two small manifests and the repository carries
two catalogs.

No `SKILL.md` was rewritten as part of the initial dual-wrapper adaptation.
Known portability changes are recorded below for a later content pass.

## Layout and ownership

```text
.claude-plugin/marketplace.json       Claude Code catalog
.agents/plugins/marketplace.json      Codex catalog
plugins/<plugin>/
  .claude-plugin/plugin.json          Claude Code wrapper
  .codex-plugin/plugin.json           Codex wrapper
  skills/<skill>/                     shared implementation
```

Keep host-specific facts in the wrappers or host-specific reference pages. Do
not fork an entire skill merely to rename a tool. A genuine host-specific
workflow, such as marketplace cache management, may use one shared dispatcher
skill with separate Claude and Codex references.

## Support matrix

| plugin | Claude Code | Codex | notes |
|---|---|---|---|
| `meta` | available | available, provisional | Skill-quality ideas are portable; marketplace and third-party packaging instructions still name Claude concepts. |
| `latex` | registered; skill validation fails | wrapper staged, not available | Two skill descriptions are not strict YAML; tool names, paths, and the `simple-english` dependency also need neutral wording. |
| `biblio` | registered; skill validation fails | wrapper staged, not available | Two skill descriptions are not strict YAML; web-tool assumptions and `.claude` paths also need neutral wording. |
| `typst` | registered; skill validation fails | wrapper staged, not available | Its skill description is not strict YAML. The body is otherwise close to portable. |
| `obsidian` | available | not available | The local plugin has no first-party skill. Claude dependencies pull four external skills, while Codex has no equivalent plugin dependency field. |

"Provisional" means the Codex package is structurally valid and installable,
not that every sentence in every shared skill is host-neutral yet. "Wrapper
staged" means `.codex-plugin/plugin.json` exists, but the catalog deliberately
sets `policy.installation: NOT_AVAILABLE` until the untouched shared skill
passes Codex validation.

The strict-YAML blockers are:

- `latex/russian-translation`;
- `latex/speech-style-adaptation`;
- `biblio/bibliography-check`;
- `biblio/extracting-precise-results`;
- `typst/typst`.

Their plain-scalar descriptions contain `: ` sequences. Converting those
descriptions to quoted or folded YAML would preserve the words, but it is still
a `SKILL.md` edit and is deferred by design.

These are pre-existing skill errors, not regressions introduced by the Codex
wrappers. `claude plugin validate .` validates the catalog and passes with the
deliberate version warnings, while validation of the three individual plugin
directories finds the malformed skill metadata. Codex's plugin validator finds
the same five failures.

## Private GitHub repository: use from a project

### Claude Code

Keep using the project-level `.claude/settings.json` snippets in
`docs/consumer-snippets.md`. They register the private marketplace and enable
only the plugins needed by that repository.

### Codex

The current Codex CLI has no `codex plugin add --scope project` equivalent.
Because strict repository isolation is not required, use a user registration
of the private Git marketplace and install only the plugins needed by the
project:

```sh
codex plugin marketplace add git@github.com:aperep/my-claude-marketplace.git --ref main
codex plugin add meta@aperep
```

The repository is cloned by Codex as a marketplace snapshot; no skill copy or
submodule is added to the consumer project. Put the expected plugin names in
the consumer project's onboarding notes or `AGENTS.md` when teammates need
the same setup. Start a new Codex session after installing a plugin.

If the marketplace is already registered, refresh it before installing a new
release:

```sh
codex plugin marketplace upgrade aperep
codex plugin add meta@aperep
```

The SSH form is intentional for this private repository. It reuses the normal
Git SSH key and avoids embedding a GitHub token in repository configuration.

## User-wide use on this machine

### Stable Git-backed installation

Register the marketplace once and install the desired set:

```sh
codex plugin marketplace add git@github.com:aperep/my-claude-marketplace.git --ref main
codex plugin add meta@aperep
```

Codex stores marketplace and plugin state under the user's Codex
configuration, so the installed plugins are available to new CLI sessions in
all repositories. Individual plugins can be enabled or disabled from the
Codex plugin browser.

### Local-checkout development

The local checkout can be registered instead of the Git source:

```sh
codex plugin marketplace add /home/sage/my-claude-marketplace
codex plugin add meta@aperep
```

The Git and local catalogs both declare the marketplace name `aperep`; do not
register both simultaneously. Switch sources explicitly with
`codex plugin marketplace remove aperep` before adding the other source.

Codex installs a cached plugin copy rather than executing directly from the
working tree. During local development, update the Codex manifest version with
a build suffix such as `0.1.0+codex.local-YYYYMMDD-HHMMSS`, reinstall the
plugin, and start a new session. For stable releases, use an ordinary semantic
version and bump it whenever shared skill content or Codex wrapper metadata
changes.

Claude manifests deliberately remain unversioned: the existing Claude Git
marketplace treats each commit as a new version. The two version policies are
host wrappers and do not require duplicated skill content.

## Third-party dependencies

Claude Code currently uses catalog entries plus manifest `dependencies` for:

- `latex` -> `simple-english`;
- `meta` -> `skillforge`, `self-learning`;
- `obsidian` -> `defuddle`, `json-canvas`, `obsidian-bases`,
  `obsidian-markdown`.

Codex manifests have no matching plugin dependency field. The first Codex
release therefore follows these rules:

1. Do not vendor third-party skills.
2. Do not pretend companion skills were installed automatically.
3. Let `latex` and `meta` degrade gracefully when a named companion is absent.
4. Keep `obsidian` at `policy.installation: NOT_AVAILABLE` until the companion
   skills have trusted Codex wrappers or upstream dual-host packaging.
5. Pin third-party Git sources by commit when Codex wrappers are eventually
   added, matching the existing trust policy.

## Proposed shared-skill changes: not applied

The following changes should be made in a separate, behavior-tested skill
content pass. They are proposals, not current behavior.

### General changes

- Keep only portable skill frontmatter (`name` and `description`) unless both
  hosts explicitly support an extra field. Move authorship to plugin manifests.
- Replace host tool labels such as `Read`, `Edit`, `Bash`, `WebSearch`,
  `WebFetch`, `Skill`, and `Agent` with capability wording: read the file,
  edit locally, run a command, search the web, or delegate to a fresh subagent.
- Resolve bundled files from the loaded `SKILL.md` directory. Do not invoke a
  helper through `.claude/skills/...` or assume either host's cache path.
- Say "project instructions" and name `CLAUDE.md` or `AGENTS.md` only as host
  examples. Project instructions continue to take precedence over a skill.
- Avoid hard-coded model families such as Sonnet in a shared workflow. Record
  the actual model used by each evaluation without requiring that model on the
  other host.
- Treat companion skills as optional unless the active host can prove that the
  dependency is installed. State the fallback behavior.

### `biblio`

- `bibliography-check`: replace the Claude-on-the-web
  `WebSearch`/`WebFetch` mode names with capability-based network modes;
  replace every `.claude/skills/bibliography-check/scripts/check_bibitems.py`
  command with a path resolved from this skill directory.
- `bibliography-check`: describe sandbox failures as detected conditions, not
  permanent properties of Claude Code; Codex network access is governed by its
  own sandbox and approvals.
- `mathscinet`: replace "Env vars set in `.claude/settings.json`" with
  host-neutral environment prerequisites and add host-specific setup examples
  in references.
- `extracting-precise-results`: no material host-specific rewrite is currently
  known.

### `latex`

- `occam-no-slop`: request `simple-english` only when installed; define what
  to do when it is absent instead of invoking the Claude `Skill` tool by name.
- `speech-style-adaptation` and `russian-translation`: replace explicit
  `Read`/`Edit`/`Bash` calls, Claude read-window limits, and `Agent` tool
  syntax with portable actions and bounded-work guidance.
- `speech-style-adaptation` and `russian-translation`: resolve `jems4.tex`
  and `P18_ru.tex` next to the loaded skill rather than through a consumer
  `.claude/skills` path.
- All LaTeX skills: treat `CLAUDE.md` and `AGENTS.md` as examples of project
  instructions rather than hard-coding one filename.
- `proofreading-pass`: retain section-level parallel review, but describe it
  as optional delegation when the host exposes subagents.

### `typst`

- Remove the extra `author` frontmatter field if the shared frontmatter is
  normalized to the minimal Agent Skills shape.
- Replace `<skill directory>` prose with one explicit instruction to resolve
  `scripts/check_typst_migration.py` relative to the loaded `SKILL.md`.

### `meta`

- `skill-quality`: replace Sonnet and Anthropic-specific assumptions with fresh
  baseline and treatment agents chosen by the active host; keep the recorded
  model identity in `evals/TESTED.md`.
- `skill-quality`: make `skillforge` an optional extended pipeline, not an
  implicit dependency.
- `editing-this-marketplace`: retain one shared entry point, but move Claude
  cache/update commands and Codex version/reinstall commands into separate
  host references.
- `trusting-foreign-skills`: retain shared trust rules (read executable
  content, pin commits, avoid silent vendoring), but split Claude
  `strict:false`/`dependencies` guidance from Codex marketplace-source and
  wrapper guidance.
- Replace references to the global `CLAUDE.md` guard policy with a host-neutral
  pointer to the applicable global instructions. Codex should adapt the guard
  idea through its own rules or hooks rather than assuming Claude paths.

## Validation contract

Before pushing a dual-wrapper change:

1. Parse both catalogs and every plugin manifest as JSON.
2. Run the Codex plugin validator for every directory containing a
   `.codex-plugin/plugin.json`.
3. Run `claude plugin validate .` and the relevant Claude per-plugin checks.
4. Confirm the diff contains no unintended `SKILL.md` changes.
5. Test installation from the local marketplace before relying on a remote
   release; schema validation alone does not exercise Git authentication or
   plugin cache behavior.

For a deliberately unavailable wrapper, record the exact skill-validation
failure and keep it `NOT_AVAILABLE`; do not treat the wrapper as installable
until the shared skill passes.
