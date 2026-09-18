---
name: maintenance
description: Run a repository's documented maintenance session and delegate its domain checks. Use when asked to run repository maintenance or a maintenance checklist, not for an ordinary feature edit, capture, or unspecified cleanup.
---

# Repository maintenance

Read the maintenance document linked from the repository's instructions;
otherwise look for `MAINTENANCE.md` or `Maintenance.md` locally. Follow its
scope, lifecycle links, thresholds, and requested mode. If missing, report
that gap and propose a small local checklist based on repository evidence.

Use `knowledge:audit-knowledge` for knowledge checks when available.
Invoke `knowledge:process-inbox` only when processing is part of the requested
session; an audit alone does not authorize it. Use other domain skills only
for checks the local checklist calls for. If one is unavailable, report the
limit and perform only supported checks.

Default to findings and proposed diffs, not automatic cleanup. Report what
was checked and what remains unresolved. Recurring execution needs a separate
scheduled invocation; this skill does not create one.
