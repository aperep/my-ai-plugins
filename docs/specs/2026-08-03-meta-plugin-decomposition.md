---
date: 2026-08-03
status: approved
---

# Meta plugin: three skills, enabled per repo

Two independent jobs. Job 1 re-cuts the plugin into three skills and rewrites
their bodies. Job 2 stops loading them in repos that cannot use them. Either can
ship first.

## Job 1: three skills

Both current `SKILL.md` bodies were generated in one pass and never tested, so
they carry no weight. Their *facts* do: `docs/LOG.md` records them as real
probes. Rewrite each body from the log. Do not edit the drafts paragraph by
paragraph.

Keep only what a fresh Claude cannot derive — this repo's traps and the user's
quality bar. Anthropic's authoring guidance says Claude writes correct
`SKILL.md` structure natively, so generic format prose goes.

| Skill | Job | Loads for |
|---|---|---|
| `skill-quality` | prove a skill earns its place, then author it | "is this any good", "why does it never fire", "worth writing at all" |
| `editing-this-marketplace` | place the files and ship them | "where does this go", "it doesn't show up", "how do I push" |
| `trusting-foreign-skills` | prompts written by someone else | "is this safe to install", "pin this skill", "self-learning wrote a skill" |

Moves:

- description doctrine → `skill-quality`. A description decides when a skill
  loads, so it is a quality property, not a layout one.
- third-party vendoring and harvested-skill review → `trusting-foreign-skills`.
  Both answer one question: a prompt nobody here wrote will run with our tool
  permissions, so what do we do.
- guard rules under "Harvested skills" → deleted, replaced by a pointer. They
  are already in the global `CLAUDE.md`, which loads every session.

Two descriptions must change. `skill-quality` says "This is the proof step, not
the authoring step", which becomes false once description doctrine moves in.
`editing-this-marketplace` must drop its vendoring clause.

## Job 2: enable per repo

A description is preloaded exactly when its plugin is enabled. There is no
"installed but unlisted" state, so enabling scope is the only lever.

Every one of the 20 `enabledPlugins` entries is `true` at user scope, and
neither repo has a `.claude/settings.json`. Three of the four meta-layer skills
have no reason to be global: `editing-this-marketplace` names one repository,
`skill-quality` fires only where skills ship, and `skillforge` never
self-triggers — it is reached by typing `/skillforge` or by `skill-quality`
naming it, and neither path reads its description.

```
dotfiles/claude/settings.json      meta@aperep-dev       true → false
                                   skillforge@aperep-dev true → false

my-claude-marketplace/.claude/settings.json   new: both enabled
dotfiles/.claude/settings.json                new: both enabled
```

Saves ~338 tokens per session elsewhere, ~430 once the third skill lands.
Measured descriptions: `self-learning` ~249, `skill-quality` ~139, `skillforge`
~105, `editing-this-marketplace` ~94.

Do not touch: `extraKnownMarketplaces`, which is a registry, not a switch —
unregistering `aperep-dev` strands `self-learning` and seven other user-wise
entries. `self-learning` stays enabled at user scope; it harvests from any repo,
which is the point of it. Guards are hooks in `dotfiles/claude/settings.json`,
not a plugin, and are untouched by both jobs.

Both editing repos enable from `@aperep-dev`. That is correct for them: they are
where prompt content is edited, so they should run the working tree.

## Drift

`.claude-plugin/marketplace.json:188` describes `self-learning` output as
landing on `surface=human-revised`. Commit `5d7afb9` renamed surfaces to guards
and made guards opt-in per path. Wrong in vocabulary and in claim. Sweep the
catalog for the same rot.

## Evals

`evals/triggers.md` per skill: phrasings that must load it, near-misses that
must not. Draw near-misses from the installed roster — `skillforge` competes for
skill-related triggers by its own admission in the catalog entry.

No RED/GREEN, no `baseline.md`, no `TESTED.md`. A cost decision, not a judgement
that the drafts are sound. The gate `skill-quality` demands of every other skill
stays unpaid by the plugin that demands it.

## Verification

```sh
claude plugin validate .
claude plugin validate ./plugins/meta
claude plugin install meta@aperep-dev          # only check that resolves sources
python3 scripts/skillforge_doctor.py           # from the skillforge plugin dir
```

Job 2 cannot be scripted. Open a session in a third repo and confirm the meta
skills are absent, then one in `my-claude-marketplace` and confirm they are
present. Verify both directions: reversed, this silently disables the gate
everywhere.

Ship using the procedure in `editing-this-marketplace`. If the skill cannot
guide its own release, the refactor is wrong.

## Rejected

- **Two skills**, closing the harvested gap with a one-line description edit.
  Cheaper, and it closes the only real gap — `editing-this-marketplace` already
  claims vendoring. Rejected for boundary clarity once job 2 confined the cost
  to two repos.
- **Four skills**, splitting the dev loop from repo layout. Two triggers for 443
  words, closing no gap.
- **One skill.** Authoring work would load push and rename detail it never needs.
- **Cutting for length.** The bodies are 112 and 99 lines against a 500-line
  budget. What gets cut is generic content, which is a different operation.
- **Auditing all 20 `enabledPlugins` entries.** Probably the largest saving
  available. Deferred to keep this pass bounded.
- **Moving consumer plugins to `@aperep`.** Smaller than it first looked, after
  two corrections. Only 5 entries take content from the working tree — `meta`,
  `latex`, `biblio`, `obsidian`, `typst`, the ones with relative `source` paths;
  the other 9 are pinned to github shas and are identical under either registry.
  And the cache is keyed by commit sha, so working-tree edits land on an explicit
  `marketplace update`, not instantly. Consumer repos already declare `aperep` in
  their own `.claude/settings.json` (`docs/LOG.md`); only this machine's user
  scope is all-dev. After job 2 that leaves `latex` alone — its skills shape
  paper repos from an uncommitted tree, which is the one case with real stakes.
  Deferred, and it needs care: `latex@aperep` and `latex@aperep-dev` are distinct
  IDs, so enabling both anywhere doubles every skill.
