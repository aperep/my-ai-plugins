# LOG

Completed and rejected plans, with the reasoning. Newest first.

## 2026-08-01 — occam-no-slop added to latex; simple-english pinned by dependency

New skill `plugins/latex/skills/occam-no-slop/SKILL.md`: an original,
language-agnostic slop check (narrative smoothness vs. cheap effects) plus an
Occam's-razor base rule (generalize, merge cases, cut what isn't needed). Runs
upstream of `speech-style-adaptation`/`russian-translation` — voice
calibration on a slop-riddled structure just produces well-voiced slop.

Requested as "based on AminBlg/SimpleEnglish". That repo (MIT, bare
`skills/simple-english/SKILL.md`, no manifest) ships ASD-STE100 Simplified
Technical English — sentence-level mechanics (20/25-word limits, active
voice, one instruction per sentence), a different layer from the structural
checks above. Per the third-party rule, did not vendor its text; added it as
its own marketplace entry (`simple-english`, `github` source pinned to
`379728b`, `strict:false` + `skills: ["./skills/simple-english"]` — safe here
since upstream has no manifest to conflict with, unlike kepano/Imbad0202
above). `plugins/latex/plugin.json` now declares
`"dependencies": ["simple-english"]`; `occam-no-slop` delegates to it by name
for English text only — no Russian equivalent exists, so Russian prose falls
back to `russian-translation`'s own anti-pattern list. Verified via
`claude plugin install latex@aperep-dev` → `(+ 1 dependency: simple-english)`.

## 2026-07-27 — me_obsidian migrated; no marketplace change needed

Third consumer, and the first that required nothing new here. `~/me_obsidian`
(the personal vault, `aperep/me_obsidian`) held eight skills in
`.claude/skills/`, **all** of them copied third-party, **none** of its own —
unlike AGora, which kept `arxiv-digest` and `zotero-mcp`.

| copies | upstream | already served by |
|---|---|---|
| `defuddle`, `json-canvas`, `obsidian-bases`, `obsidian-markdown` | kepano/obsidian-skills | `obsidian@aperep` + its 4 pinned deps |
| `brainstorming`, `executing-plans`, `using-git-worktrees`, `using-superpowers` | obra/superpowers | `superpowers@claude-plugins-official` 6.1.1 |

So the whole migration was a delete plus a `.claude/settings.json`. Enabled
`obsidian` and `superpowers` only — no `biblio`/`typst` (a personal vault is not
a paper repo), and `academic-research-skills` stays absent for the reason
recorded below: its `PreToolUse` hook would run on every write in the vault.

### The copies were not merely redundant, they were wrong

Diffed all eight against their pins before deleting. Local edits: the
`upstream:` frontmatter line, nothing else, in all eight. Everything else was
upstream being *ahead*, and in ways that mislead a session:

- `obsidian-bases` — still documented `and/or/not` as freely combinable
  (upstream: exactly one key). The identical staleness AGora's copy had, which
  is what a frozen copy of a shared upstream does twice over.
- `obsidian-markdown/references/EMBEDS.md` — no "Embed Bases" section.
- `brainstorming` — offered the visual companion upfront; 6.1.1 offers it
  just-in-time and starts the server with `--open`. `frame-template.html`
  rewritten wholesale.
- `using-superpowers` — predates the "The Rule" restructure and the
  `references/*-tools.md` platform adaptation.
- `using-git-worktrees` — still carried the legacy
  `~/.config/superpowers/worktrees/` global path upstream has dropped.

Worth stating plainly, since it is the argument for the whole marketplace:
vendoring decays silently. There is no error, just an older prompt, and the
`obsidian-bases` filter syntax was wrong in two separate vaults simultaneously.

### The `upstream:` field is the thing that makes this cheap

Three consumers sorted with no guesswork because most vendored skills carried
`upstream:` in frontmatter. Keep the convention on anything vendored in future.
Its corollary, now confirmed three times: a copy whose *only* diff against the
pin is that line is by definition safe to delete.

Cross-reference grep (the failure mode flagged in the AGora entry) found one hit
— `skills/brainstorming/visual-companion.md`, internal to the vendored skill
itself. No vault note referenced a skill path.

## 2026-07-26 — AGora migrated; kepano's three Obsidian skills un-vendored

Second consumer, same treatment as `academic-workshop`. AGora (the Obsidian
vault) held its skills two ways: nine symlinks into a `tools/academic-workshop`
git submodule, and three *copied* third-party skills.

### The three copies

`json-canvas`, `obsidian-bases`, `obsidian-markdown` — all
`upstream: kepano/obsidian-skills`, the same repo `defuddle` comes from. Added
as three more `git-subdir` entries pinned to the same sha `a1dc48e6`, and
`plugins/obsidian` now declares all four as `dependencies`. Installing
`obsidian@aperep` reports `(+ 4 dependencies)`; the plugin still ships no skill
of its own and exists purely as the aggregator.

The sparse clone carries each skill's `references/` subdirectory, not just
`SKILL.md` — worth knowing, since these three are useless without it, unlike
`defuddle`.

Diffed the copies against the pin before deleting them: the only local edit was
the `upstream:` frontmatter line, and upstream is *ahead* — the vendored
`obsidian-bases` still documented `and/or/not` filters as freely combinable
(upstream: exactly one key), and its `EMBEDS.md` lacked the "Embed Bases"
section. Vendoring had silently frozen a wrong version. Nothing to preserve.

Not adopted: kepano's repo as one `github` entry. All-or-nothing — it would also
pull `obsidian-cli`, and the 2026-07-26 entry below records why `strict: false`
subsetting fails against that repo.

### AGora's side

`.claude/settings.json` declares `aperep` + `claude-plugins-official` and enables
`obsidian`, `biblio`, `typst`, `superpowers`. Removed: the submodule, the nine
symlinks, `.claude/skills.manifest`, `tools/setup-skills.sh`, the `.gitignore`
block listing the symlinks. `.claude/skills/` keeps exactly the two skills that
are about *this* vault — `arxiv-digest` and `zotero-mcp`.

`academic-research-skills` was symlinked in and is deliberately **not** enabled:
a notes vault does not write papers, and enabling it would run a third-party
`PreToolUse` hook on every write in the vault. It stays available per project
where papers actually get written.

Cross-references needed repair by hand — `arxiv-digest` and `zotero-mcp` name
their sub-skills in prose (`tools/academic-workshop:mathscinet` →
`biblio:mathscinet`), and nothing type-checks that. A stale skill reference is
the failure mode this migration form introduces; grep for the old path after
every consumer move.

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
