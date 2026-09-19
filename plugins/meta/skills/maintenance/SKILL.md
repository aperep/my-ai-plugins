---
name: maintenance
description: Run a repository's documented maintenance session, including its inbox, routine checks, and content-guard review drift. Use when asked to run repository maintenance or a maintenance checklist, not for an ordinary feature edit, capture, or unspecified cleanup.
---

# Repository maintenance

Read the maintenance document linked from the repository's instructions;
otherwise look for `docs/MAINTENANCE.md`, then a legacy root `MAINTENANCE.md`.
Follow its scope, routine checklist, and requested mode. If missing, report the
gap and propose a small checklist based on repository evidence.

Process `docs/INBOX.md` when the maintenance document calls for it. Apply small,
unambiguous items within the requested scope, move deferred work to the
repository-wide `docs/ROADMAP.md`, and remove rejected items. Use domain skills
only for checks the local checklist calls for.

If `.gitattributes` declares `guard=human-revised`, report paths changed since
their `reviewed=<sha>` commit, missing or invalid stamps, and disagreement with
any in-file `reviewed:` mirror. Do not change review stamps.

Report what was done, what remains unresolved, and any unavailable checks.
Recurring execution needs a separate scheduled invocation; this skill does
not create one.
