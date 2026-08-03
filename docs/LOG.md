# LOG

Completed and rejected plans, with the reasoning. Newest first.

## 2026-08-03 — "surfaces" renamed to guards; wildcards abolished

The notion is now **guards**, and the git attribute is `guard=`. Earlier entries
below were rewritten to the new vocabulary, so "surface" survives only where one
quotes a message that shipped under the old name.

**No wildcard guarding.** Every pattern is gone from both `.gitattributes` files,
including the ones added yesterday. A guard names one file the user has decided
to own or to check; a pattern claims files nobody has looked at yet — the same
over-reach as `ai-controlled` and the fail-closed skills rule, in a third
costume. Guards are added on request, one path at a time. Proposing is allowed,
adding is not.

Both repos therefore declare **zero** guards, and both report "no guards
declared" at session start. That is the correct starting state, not a regression:
the mechanism works and nothing has been claimed with it yet.

What fills the gap is the reminder, which now lists any `*/skills/*/SKILL.md`
sitting on no guard — widened from the old `claude/skills/` check, since this
repo keeps skills under `plugins/*/skills/`. That listing is the raw material for
a proposal.

Guards could cover anything eventually. Starting with a few skills is the user's
call and the right one: the machinery is two days old and has already been wrong
twice about how hard to push.

## 2026-08-03 — the skills guard is reverted to a reminder; guards are for prompts, not code

Two corrections to yesterday's entry, both from the user, both narrowing the
design.

**No `.gitattributes` means no guard.** The second guard rule — refuse to write a
skill into a repo declaring no guard for it — is removed. It failed *closed*
while the human-only rule failed *open*, which inverted the guard's contract for
one path shape, and it punished an ordinary repo for a state that is simply its
default. Most repos will never declare guards and that is not a fault in them.

The concern was real, so it moved rather than vanished. `review-due.sh` now
reports at session start, without stopping anything: skills sitting on no
guard, and a single line when a repo declares no guards at all. The absence
of guards is visible instead of silent, which was the actual goal — blocking was
just the first tool reached for.

Worth naming the pattern, since it is the second time in two days: a rule was
built at the strongest enforcement available rather than the one that matched its
stakes. `ai-controlled` had a label with no consequence; this had a consequence
out of proportion to its label. The reminder tier exists precisely for rules that
should be noticed rather than obeyed.

**Guards cover prompt-content, not code.** `claude/hooks/**` is off the guard
map. A shell script is reviewed as code, in the diff, like any script — including
the two scripts that implement guards. A prompt is different in kind: it
changes what an agent does in a session the user is not present for, and that is
the whole reason the review machinery exists. Mirror stamps are frontmatter-only
now; the comment-marker form for scripts is dropped with it.

One wording bug fixed on the way: with the unguarded-skills entry added, the
report still opened "Files on the human-revised surface have changed since the
user last reviewed them" and closed with an instruction to move a `reviewed=`
stamp — neither true for a skill that has no guard at all. Header and footer
are now correct for both cases.

## 2026-08-02 — content guards, enforced by hooks; skill-quality added to meta

Job 1 of two. Spec: `docs/specs/2026-08-02-content-guards.md`. Job 2 (harvesting
skills from sessions, work-style reports) is deferred and unstarted.

### Guards ride on git attributes

Two guards — `human-only` and `human-revised` — declared in the repo's
`.gitattributes`, one line per glob. Rejected a purpose-built sidecar file:
git already implements the glob semantics and last-match-wins, and
`git check-attr guard -- <path>` answers the per-file question with no glob
code in the hooks at all. Frontmatter was rejected outright — guards have to
cover `scripts/` and `evals/`, which have none.

`human-revised` carries `reviewed=<short-sha>` on the same line: the commit the
user last read through. A review moves that field and touches nothing else, so
it never blocks on the user rewriting anything, and the drift is exact rather
than a count of "many changes".

A third guard, `ai-controlled`, was specified, built, and cut the same day at
the user's call. Its rule was "the user never reads this" — which is not a rule,
because it is what the default already does. Same edits allowed, same hooks
silent, same tracking absent. It survived the design review only because a
three-row table looks more complete than a two-row one. Worth remembering as the
failure mode: a taxonomy grows a category that names a feeling rather than a
behavior, and nothing catches it until someone asks what changes when the label
is applied.

Two constraints fell out of the choice, both now documented in the file itself:
patterns must be path-anchored, because a bare `*.md` matches at any depth for
`check-attr` but only at the root for the `:(glob)` pathspec the drift check
uses; and `.gitattributes` must stay unlisted, or the guard blocks the one edit
a review needs.

### Prompt rules were rejected for enforcement

"Never edit this" and "remind me when things pile up" are the two rule shapes
that fail silently when the model is busy elsewhere. Both are hooks now, in
`dotfiles/claude/hooks/`, linked to `~/.claude/hooks/`:

- `guard.sh` — `PreToolUse` on `Write|Edit|MultiEdit|NotebookEdit`,
  denies with exit 2 on `human-only`. Fails **open** everywhere else: no repo, no
  `.gitattributes`, malformed stdin, missing path all exit 0. A guard that failed
  closed would block edits in every repo that never heard of guards.
- `review-due.sh` — `SessionStart`, prints a diffstat per drifted
  `human-revised` pattern, silent otherwise.

Two things the tests forced. `git diff <stamp>..HEAD` was wrong twice over: it
misses uncommitted edits (drift the user has not seen either), so the range
became `git diff <stamp>` against the working tree; and it cannot see a file that
was never added, so untracked matches are collected separately with
`ls-files --others`. Without that second fix a brand-new unreviewed skill — the
exact case the reminder exists for — was invisible. A stampless pattern that
matches nothing is now silent instead of reporting "never reviewed" forever.

### `dotfiles/CLAUDE.md` was wrong about its own links

It claimed `claude/` and `codex/` are linked as whole directories. They are
linked file by file, and must be: `~/.claude/` also holds Claude Code's own
sessions, plugins and caches, so it cannot be a symlink. Corrected, with the
consequence stated — a new file under `claude/` is dead until it gets its own
`install.conf.yaml` entry. `claude/hooks` is a directory link, like
`claude/agents`.

Also removed a dead line from the global `CLAUDE.md`: it told every session to
"use meta-prompting and sdd skills". Neither has ever existed on this machine.

### skill-quality, and why SkillForge is not pinned

New `plugins/meta/skills/skill-quality/`. A gate, not an authoring guide:
`superpowers:writing-skills` covers how to write one, this covers proving it
changes behavior. RED (a fresh sonnet subagent fails without the skill, or there
is no skill to write) → write against those recorded failures only → GREEN (a
fresh subagent clears them) → trigger tests including the must-not-fire list →
an adversarial subagent whose job is to refute the result. Evidence lands in
`evals/{baseline,triggers,TESTED}.md`; `TESTED.md` is one row per model, because
a skill tested on one model is tested on one model.

Cut a third of it in an Occam pass before shipping. The "is a skill needed?"
section restated the RED gate. Three of five architecture bullets were already in
`editing-this-marketplace` or `docs/SKILL-template.md`, and the file-layout tree
would have been its fourth copy in this repo — a gate skill has no business
re-teaching authoring. Two bullets survive because nothing else states them: one
skill one job, and say what to do rather than what to avoid.

`tripleyak/SkillForge` (MIT, 842★) supplied the RED/GREEN idea and nothing else.
Not adopted as an entry: its description claims "create a skill", "improve the X
skill" and "which skill should I use", which fires over both
`superpowers:writing-skills` and `editing-this-marketplace`. It is an
orchestrator that wants the whole trigger space, and it ships Python tooling for
what is four subagent calls. Its own doctrine — a skill that steals triggers is
worse than one that never fires — is the argument against installing it here.

### Job 2 folded in: self-learning and skillforge pinned

Both `strict: false` + a `skills` array over a `github` source.
`Kulaxyz/self-learning-skills` ships `.claude-plugin/marketplace.json` and
installs clean anyway — confirming for a second time that the "conflicting
manifests" trigger is an upstream **`plugin.json`**, not any file under
`.claude-plugin/`. `plugins/meta` declares both as dependencies.

`tripleyak/SkillForge` is pinned after all, against the objection recorded above,
because `skill-quality` now hands it a large rewrite the way `occam-no-slop`
hands English prose to `simple-english`. The objection is not solved, only
accepted and written down: once enabled, its description competes for
skill-related triggers, and nothing short of vendoring could change that.

### The harvest landing rule was backwards, and self-learning is why guards exist

The spec originally sent harvested skills to an *unlisted* path, so as not to
charge the user with reviewing something they never asked for. Wrong, and wrong
in the direction that defeats the whole design. `self-learning` instructs the
agent to "act on the cue immediately — don't ask for permission first", and what
it writes is authoritative: the next session trusts it without re-deriving. An
unread prompt that steers future sessions is the strongest case there is *for* a
review reminder. Harvested skills now land on `human-revised` with **no stamp**,
so they read as never reviewed until someone looks.

Two gaps that closing this exposed:

- `~/.claude/skills/` — where a *global* harvest lands — was not a git repo, so a
  globally harvested skill would have had no guard, no stamp and no reminder,
  permanently. Now `dotfiles/claude/skills/`, linked into place, with
  `claude/skills/** guard=human-revised` and no stamp. `README.md` there is the
  stub that keeps the empty directory in git and makes the guard visible.
- A repo with no `.gitattributes` gets no protection at all, and `self-learning`
  is enabled at user scope, so it will harvest anywhere. This started as a prompt
  rule in the global `CLAUDE.md` — and a prompt rule is the exact shape the hooks
  exist to replace, so it became `guard.sh`'s second rule: deny any write
  under `*claude/skills/*` in a repo that declares no guard for it, or in no
  repo at all. Unlike the `human-only` rule it fails **closed**, because it fires
  only on skills paths, where an absent guard is the bug and not a normal
  state. The refusal names the line to add.

Writing rule 2 surfaced a latent bug in rule 1. The guard stripped the repo root
off the target path by prefix, which breaks the moment the path arrives through a
symlink — and `~/.claude/skills` is now exactly that, a link into the dotfiles
repo. `check-attr` was being handed an absolute path outside the repo, returned
nothing, and the guard failed open precisely where it must not. Resolution now
goes through `pwd -P` first. Proven by denying a `human-only` file reached
through a symlink: the refusal names the repo-relative path, so it resolved
rather than fell through.

### In-file stamps as a visible mirror

`.gitattributes` stays authoritative; text files also carry `reviewed: <sha>` so
the state is visible on opening the file. Rejected making the in-file stamp
authoritative: it cannot mark JSON or binaries, and it cannot protect a path
before the file exists — the guard suite denies `docs/new/deep.md` in a repo
where that file has never been created. Territory is a glob, a review record is
per-file, and the mirror buys the per-file visibility without moving authority.

Two copies of one fact drift, so `review-due.sh` compares them and reports a
mismatch. Writing that check cost one real bug: `git grep` had no `-o` before
2.44, and passing it made git read `--untracked` as a revision, so the check
failed silently and reported nothing. Match with git, extract with grep.

Verified: `claude plugin validate` clean (only the deliberate no-`version`
warnings). Guard tested on 8 cases, reminder on 9 — re-run after the rename and
again after the mirror check. Both repos report correctly, `~/.claude/skills` is
linked. Nothing is committed yet.

Always-on cost of the meta layer is now ~800 tokens in every session in every
repo: `self-learning` ~310, `skillforge` ~190, `skill-quality` ~180,
`editing-this-marketplace` ~120. Worth revisiting if it starts crowding real
work; per-project enabling is the lever.

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
