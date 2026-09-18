---
name: managing-repository-docs
description: Use when creating, splitting, moving, auditing, or migrating agent-facing Markdown documentation in a repository, or when documentation is orphaned, duplicated, oversized, or poorly placed.
---

# Manage Repository Documentation

Keep repository knowledge navigable from the root `AGENTS.md` as a parent
tree. This applies to repository-owned agent-facing Markdown, not installed or
vendored skill documentation.

The parent must make its child observable. Parent metadata alone is not
navigation; the direct Markdown link from parent to child is the core
invariant.

## Structure

- Root `AGENTS.md` is the tree root and has no `parent`.
- Every other document starts with repository-relative `parent` metadata:

  ```yaml
  ---
  parent: docs/ROADMAP.md
  ---
  ```

- The named parent contains a short, visible Markdown link to the child. Other useful
  cross-links are fine, but each document has exactly one logical parent.
- Put component-specific knowledge in that component's directory. Keep
  repository-wide plans, decisions, bugs, and maps under `docs/`.
- Reference existing material instead of repeating it.
- Content folders explain their purpose and lifecycle in a README. Put
  agent-specific refinements in `AGENTS.md`, linking to that contract rather
  than repeating it. Storage-specific knowledge rules belong to `knowledge`.

Before adding a substantial section, ask whether it has its own lifecycle,
audience, or topic. If so, create a child document and leave a short summary
and link in the parent. Do not split a short cohesive section merely to satisfy
a size rule.

## Create or Edit

1. Read the intended parent and nearby documents.
2. Reuse or extend an existing document when the topic already has a home.
3. Otherwise create the file in the relevant component directory or `docs/`,
   add its `parent`, and add a short parent link in the same change.
4. Run the tree check.

Resolve `../../scripts/project_docs_context.py` relative to this skill, then
run it from the consumer repository root:

```sh
python3 /path/to/meta/scripts/project_docs_context.py --check
```

## Existing Repositories

Run `--check` for a read-only report. Run `--migrate` only when edits are
authorized. Migration adds missing metadata and links using the nearest
directory `AGENTS.md` or README. Top-level docs and component indexes may fall
back to root `AGENTS.md`; ambiguous nested documents are reported instead of
guessed. Review placement and parent semantics, then rerun `--check`.

The checker includes tracked and untracked non-ignored Markdown and excludes
paths inside `skills/`. It reports missing roots or parents, absent parent
links, and cycles.
