---
date: 2026-08-02
status: approved
job: 1 of 2
---

# Content surfaces and skill quality gates

Job 1 of two. This one is the rules: who owns which file, how a review is
recorded, and how a skill proves it works. Job 2 is the automation that rides on
top (harvesting skills from successful sessions, work-style reports) and is not
specified here.

## Surfaces

Two surfaces, plus the default. They say who owns a file, not what is in it.

| surface | the user | the agent |
|---|---|---|
| `human-only` | owns it | never edits it |
| `human-revised` | reads sometimes, edits | edits freely; must report unreviewed drift with a diff |
| (unlisted) | normal file | edits freely, no review tracking |

A review does one thing: it moves the stamp. It never requires an edit.

An `ai-controlled` surface was specified and then dropped. Its rule was "the user
never reads this", which produces no behavior the default does not already
produce: the agent edits freely, no hook fires, nothing is tracked. A surface
that changes nothing is not a surface, and carrying it cost a row in every table
and a branch in the reader's head.

## Where a surface is declared

In `.gitattributes`, at the root of the repo that holds the file:

```
plugins/*/skills/*/SKILL.md    surface=human-revised reviewed=a1b2c3d
docs/LOG.md                    surface=human-only
```

Git supplies the glob matching and the last-match-wins rule. `git check-attr
surface -- <path>` answers the question for one file with no glob code in the
hooks.

`reviewed=` holds the short SHA of the commit that the user last reviewed
through. Drift is then exact:

```sh
git diff <stamp>..HEAD -- ':(glob)<pattern>'
```

Two constraints follow from using git attributes:

- Patterns must be path-anchored. A bare `*.md` matches at any depth for
  `check-attr` but only at the root for the `:(glob)` pathspec, so the guard and
  the reminder would disagree.
- `.gitattributes` itself stays unlisted. Marking it `human-only` would block the
  agent from writing the stamp, which is the one edit a review needs.

## Enforcement

Two hooks in `~/.claude/hooks/`, linked from `dotfiles/claude/hooks/`. Both are
no-ops outside a git repo and in any repo whose `.gitattributes` declares no
surfaces, so the cost in an unrelated project is one process spawn.

**`surface-guard.sh`** — `PreToolUse` on `Write|Edit|MultiEdit|NotebookEdit`.
Denies with exit 2 when `surface=human-only`, and does nothing else. The stderr
text returns to the agent, which then proposes the change in its reply instead of
writing it.

It fails **open** on everything: no repo, no `.gitattributes`, malformed input,
undeclared path. **No `.gitattributes` means no guard**, and that is the correct
reading rather than a gap — an undeclared repo is a normal repo, not a repo with
a problem. Blocking is reserved for the one case where the user has explicitly
claimed a path.

An earlier version added a second, fail-**closed** rule: refuse to write a skill
into a repo declaring no surface for it. Removed. It inverted the guard's
contract for one path shape, and it punished an ordinary repo for a state that is
its default. That concern belongs in the reminder, which now names unsurfaced
skills without stopping anything.

Path resolution runs through `pwd -P` before asking git. `~/.claude/skills` is a
symlink into the dotfiles repo, so the path the agent writes to never starts with
the repo root, and a prefix strip alone leaves the "relative" path absolute —
which makes `check-attr` return nothing and the guard pass a file it should have
refused.

**`review-due.sh`** — `SessionStart`. Carries everything non-blocking:

- a per-pattern diffstat since each `reviewed=` stamp, and never-reviewed for a
  pattern that has no stamp;
- in-file `reviewed:` mirrors that disagree with the authoritative stamp;
- skills on no surface, which can therefore never be reported as unread;
- one line when the repo declares no surfaces at all, so the absence of guards is
  visible rather than silent.

Silent when nothing has drifted and surfaces are declared.

A prompt rule was rejected for the prohibition, because a prohibition is the rule
shape that fails silently when the model is busy elsewhere. Everything else is a
reminder by choice: the reminder is allowed to be missed occasionally, the
prohibition is not.

## What surfaces cover

Prompt-content: skills, docs, prose that steers a later session without being
read. **Not code.** A shell script is reviewed as code, in the diff, the way any
script is — so `dotfiles/claude/hooks/*.sh` sits on no surface despite
implementing this system. The asymmetry is the point: a script does what it says
when you read it, while a prompt changes what an agent does in a session you are
not present for.

## Skill quality

New skill `meta:skill-quality`. It is a gate, not a rival to
`superpowers:writing-skills` — that one is about authoring, this one is about
proving the result changes behavior. The core is the RED/GREEN pair, taken as an
idea from tripleyak/SkillForge without adopting the plugin.

1. **RED.** A fresh subagent attempts the task with the skill absent. It records
   what went wrong. Nothing went wrong means no skill is needed, and the honest
   move is to stop.
2. **GREEN.** A fresh subagent attempts the same task with the skill loaded. It
   must clear every recorded failure.
3. **Triggers.** Phrasings that must load the skill, and phrasings that must not.
   The second list is the collision check against the installed roster.
4. **Adversarial pass.** A second subagent tries to refute the findings rather
   than confirm them.

Each skill carries its evidence next to itself:

```
skills/<name>/evals/
  baseline.md    what a fresh agent got wrong without the skill
  triggers.md    phrasings that must fire, phrasings that must not
  TESTED.md      one row per model run
```

`TESTED.md` is the model record:

| model | date | skill commit | RED reproduced | GREEN cleared | notes |

`evals/` is unlisted. It is evidence for the agent, not reading for the user, and
nothing about that needs a surface to say it.

## Not adopted

**tripleyak/SkillForge as a plugin.** Its description claims "create a skill",
"improve the X skill", and "which skill should I use". Those fire over
`superpowers:writing-skills` and over `meta:editing-this-marketplace`. It is an
orchestrator that wants to own the whole trigger space, and it needs Python
tooling for a job that is four subagent calls. The RED/GREEN idea is the load
bearing part and it costs a paragraph.

## In-file mirror stamps

`.gitattributes` stays authoritative. A text file on a tracked surface also
carries `reviewed: <sha>` — in frontmatter, or behind a comment marker where
there is none — purely so the state is visible on opening the file. Non-text
files get no mirror. A territory with no file yet gets a stub that carries the
marker, which is what `dotfiles/claude/skills/README.md` is.

Two copies of one fact will drift, so `review-due.sh` compares them and reports a
mismatch instead of trusting either. That turns the redundancy from a liability
into a check.

Rejected: making the in-file stamp authoritative. It cannot mark JSON or binary
files, and it cannot protect a path before the file exists — the guard suite
denies `docs/new/deep.md` on a repo where that file has never been created.
Territory is a glob; a review record is per-file. The mirror gives the per-file
visibility without moving the authority.

## Deferred to job 2

- `Kulaxyz/self-learning-skills`, pinned. **Corrected 2026-08-03:** an earlier
  draft of this spec sent harvested output to an unlisted path, reasoning that
  the user should not be charged with reviewing something they never asked for.
  That is backwards. The skill's own instruction is "act on the cue immediately —
  don't ask for permission first", and what it writes is authoritative: the next
  session trusts it without re-deriving. An unread prompt that steers future
  sessions is the single strongest case for a review reminder, not an exemption
  from one. Harvested skills land on `human-revised` **with no stamp**, so they
  report as never reviewed until the user reads them.
- `smixs/mentor`, pinned as-is. No trigger collision; it writes an HTML report.
