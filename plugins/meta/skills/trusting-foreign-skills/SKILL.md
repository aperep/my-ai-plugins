---
name: trusting-foreign-skills
description: >
  Use when installing, pinning, updating, or deciding whether to adopt a skill
  or plugin written by someone else, when choosing between the git-subdir and
  strict:false entry forms, when an install fails with "conflicting manifests",
  and when self-learning or another harvester has written a skill nobody has
  read yet. Covers pinning by sha, what a third-party plugin can execute, and
  which unread prompts get a guard.
---

# Trusting foreign skills

A skill is a prompt executed with your tool permissions, and a plugin can also
carry hooks, agents and MCP servers. Two kinds arrive without being read: what
someone else wrote, and what a harvester wrote for you. Both are handled here.

## Never vendor; pin instead

Copying a third-party skill into `plugins/` is the one thing not to do.
Vendoring decays silently — there is no error, only an older prompt. The
vendored `obsidian-bases` documented `and/or/not` filters as freely combinable
when upstream had long since required exactly one key, and it was wrong in two
vaults at once before anyone noticed.

Add it as its own marketplace entry with a pinned `sha`. If a copy must exist
for a while, carry `upstream: <owner>/<repo>` in its frontmatter; a copy whose
only diff against the pin is that line is by definition safe to delete.

## Picking the entry form

The wrong choice fails at load, not at validate.

- Upstream ships **no** `.claude-plugin/plugin.json` → `github` source with
  `strict: false` plus a `skills` array naming the subset to expose.
- Upstream ships **any** `plugin.json` → the above is a "conflicting manifests"
  error. Probed directly: the trigger is the mere *presence* of that file, not
  what it declares — neither kepano's nor Imbad0202's names a single component,
  and both conflict. Take one directory with a `git-subdir` source instead
  (`url` + `path` + `sha`).

Use the `git@github.com:` URL. Git over HTTPS to github.com is blocked in this
environment ("Connection reset by peer"), while the `github` source type works
because it does not clone.

`git-subdir` sparse-clones the named directory including its `references/`, but
only that directory. Skills that reach across the repo — `../../shared/`, each
other's `agents/` — are not self-contained and cannot be taken this way; the
choice is then the whole upstream plugin or nothing.

To pull an entry in automatically, add `"dependencies": ["that-entry"]` to a
plugin's `plugin.json`. Same-marketplace, so no
`allowCrossMarketplaceDependenciesOn`. Bare strings only — version ranges
resolve against `{plugin}--v{version}` git tags, which this marketplace does not
create.

## Read what it executes before adopting

Run `claude plugin details <name>@aperep-dev` and look at the inventory, not the
README. `academic-research-skills` brings 20 skills, 3 agents, and two hooks —
a `SessionStart` announce and a `PreToolUse` matcher on
`Write|Edit|MultiEdit|Bash`. It is a documented fail-open guard, not something
hostile, and it still means third-party code runs on every write and every Bash
call wherever the plugin is enabled.

Check the licence, and enable anything that ships hooks **per project, never at
user scope**.

## Skills nobody has read

`self-learning` tells its agent to act on the cue immediately and not ask for
permission first, and what it writes is authoritative: the next session trusts
it without re-deriving. That is the strongest case there is for a review
reminder.

Harvested skills land with **no stamp**, so they read as never reviewed until
someone looks. A global harvest lands in `~/.claude/skills/`, which is the
dotfiles repo, so it is in git and can be tracked. A session-start hook lists
skills sitting on no guard; that listing is the raw material for a proposal.

Offer a guard for one path at a time, when the skill matters. Never add one
uninvited, never widen it to a wildcard, and never stamp a skill you wrote
yourself. The guard rules are in the global `CLAUDE.md`. Whether the skill is
any good is a separate question: `skill-quality`.
