# LOG

Completed and rejected plans, with the reasoning. Newest first.

## 2026-07-26 — Migration of academic-workshop skills into plugins

Source: `~/texlab/academic-workshop/.claude/skills/` (19 skill dirs). Provenance
came from an `upstream:` field in most skills' frontmatter, so the split was not
guesswork.

### Sorting rule

Three buckets: **mine** (migrate), **third-party** (reference upstream, never
vendor), **not a skill** (stays in the source repo).

### Migrated — 6 skills + 1 new

| plugin | skills |
|---|---|
| `biblio` | `bibliography-check`, `mathscinet`, `extracting-precise-results` |
| `latex` | `speech-style-adaptation`, `russian-translation`, `proofreading-pass` (new) |
| `typst` | `typst` |

Edits made in the move:

- `bibliography-check` — description hard-coded `tex/bibliography*.tex`. Softened
  to "typically", with a note to glob for `\bibitem` instead of assuming a
  layout. A plugin skill is used from repos with other conventions.
- `typst` — the check script was invoked as
  `.claude/skills/typst/scripts/check_typst_migration.py`. That path dies the
  moment the skill ships as a plugin (plugins run from a cache directory), so it
  now says "next to `SKILL.md`".
- `typst-talk` was a stub: `references/slides.typ`, no `SKILL.md`. Folded the
  file into the `typst` skill's `references/` and pointed the workflow at it.
- `proofreading-pass` is new, generalised from the one worked example in
  `academic-workshop/proofreading/zaidenberg-solvable-lie-algebras/`
  (subagent-per-section, three output files, categorised change log, flagged-not-
  changed section). The example itself stays in the workshop repo.

### Not migrated

- **superpowers** (7: `brainstorming`, `executing-plans`, `using-git-worktrees`,
  `using-superpowers`, `verification-before-completion`, `writing-plans`,
  `writing-skills`). Already installed as `superpowers@claude-plugins-official`
  at a newer version. Git history showed only two bulk commits touching them and
  no individual edits, so the 0–89 line diffs against the installed copies are
  upstream version skew, not local customisation — nothing to preserve.
- **`Imbad0202/academic-research-skills`** (4: `academic-paper`,
  `academic-paper-reviewer`, `academic-pipeline`, `deep-research`). Kept at the
  user's decision, as a pinned entry rather than a copy — see below. My objection
  stands on the record: 2.1 MB of generic paper-mill orchestration whose trigger
  lists fire on bare words like "research" and "review paper". Enabled per
  project, never at user scope.
- **`templates/`, `interlinear/`, `setup/`, `proofreading/`** — project content,
  not skills. Stay in the workshop repo.

### defuddle: bundled by dependency, not copied

`defuddle` (from `kepano/obsidian-skills`) is used *by* other skills, so the
`obsidian` plugin must be able to rely on it. Resolution, in the order tried:

1. **`strict: false` + `skills: ["./skills/defuddle"]` over a `github` source** —
   rejected: fails at load with "conflicting manifests". Their repo carries its
   own `.claude-plugin/plugin.json` that specifies components, and `strict:false`
   with a component spec on both sides is an error. Works only for upstream repos
   that ship bare `SKILL.md` files with no manifest — which the README's
   third-party section assumes and should say.
2. **`git-subdir` over HTTPS** — rejected: git-over-HTTPS to github.com is
   blocked in this environment ("Connection reset by peer"), though the `github`
   source type works, so it presumably fetches over the API rather than by clone.
3. **`git-subdir` over SSH** — adopted. Sparse-clones `skills/defuddle` alone,
   pinned by `sha`; the cache directory holds exactly one `SKILL.md`. Consistent
   with the README's existing "use an SSH remote" requirement.

`plugins/obsidian` declares `"dependencies": ["defuddle"]`. Because the entry
lives in this marketplace, it is a same-marketplace dependency and needs no
`allowCrossMarketplaceDependenciesOn`. Installing `obsidian` reports
`(+ 1 dependency: defuddle)`; disabling `defuddle` while `obsidian` is enabled is
refused; `claude plugin prune` removes it once nothing needs it.

Bare-string dependencies only: semver ranges resolve against git tags named
`{plugin}--v{version}`, and this marketplace deliberately declares no `version`.

Not resolved: `defuddle` wraps a CLI that is not installed here (no `defuddle`,
no `node`). The skill is inert until `npm install -g defuddle`.

### academic-research-skills: partial load is impossible, all-or-nothing adopted

Asked for a partial load (the 4 skills, nothing else). Not achievable:

- `strict: false` + a `skills` array fails the same way as kepano —
  "conflicting manifests". Probed directly: the trigger is the mere *presence* of
  an upstream `.claude-plugin/plugin.json`, not what it declares. Neither
  kepano's nor Imbad0202's manifest names a single component, and both conflict.
  So the README's `strict: false` form only ever applies to upstreams with no
  manifest at all.
- per-skill `git-subdir` (as used for `defuddle`) breaks these skills: they
  reference `../../shared/`, `../../docs/`, and each other's `agents/` and
  `references/` across directories. A one-directory sparse clone is not
  self-contained.
- their own `marketplace.json` publishes all four as a *single* plugin, so adding
  their marketplace directly is equally all-or-nothing.

Adopted: one entry, `github` source, pinned to sha `15740c8e`. What that drags
in, verified by `claude plugin details`: **20 skills** (the 4 plus 16 `/ars-*`
commands), **3 agents**, and **2 hooks** — a `SessionStart` announce and a
`PreToolUse` matcher on `Write|Edit|MultiEdit|Bash` that shells out to
`run_guard.sh`. Read before adopting: it is a documented, fail-open write-scope
guard that emits a pass-through and exits 0 on any error, not something hostile.
It still means third-party code runs on every write and every Bash call in any
repo where the plugin is enabled. Licence is CC-BY-NC-4.0.

Consequence: enable it per project only. It is deliberately absent from this
machine's user scope.

### Consumers

`academic-workshop/.claude/settings.json` declares `aperep` and
`claude-plugins-official`, and enables `meta`, `latex`, `biblio`, `typst`,
`defuddle`, `academic-research-skills`, `superpowers`. All 19 skill directories
were deleted from `academic-workshop/.claude/skills/`; every one of them is
covered by an enabled plugin, so nothing was dropped on the floor.
