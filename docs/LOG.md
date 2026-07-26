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
  `academic-paper-reviewer`, `academic-pipeline`, `deep-research`). Rejected.
  2.1 MB of generic paper-mill orchestration whose trigger lists fire on bare
  words like "research" and "review paper" — they would hijack ordinary requests
  in a repo where real mathematics is being done. If ever wanted: third-party
  entry, pinned sha, enabled per project, never at user scope.
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

### Consumers

`academic-workshop/.claude/settings.json` now declares the `aperep` marketplace
and enables `meta`, `latex`, `biblio`, `typst`. It resolves once this repo is
pushed. The repo's own `.claude/skills/` copies are still in place and will
collide by name — deleting them is a separate, reviewed step.
