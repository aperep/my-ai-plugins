---
name: doc-map
description: Map, audit, or reorganize agent-facing repository documentation rooted at AGENTS.md. Use for documentation navigation, placement, or migration; classify Markdown templates, fixtures, eval artifacts, and domain reference material as repository content instead of mapping them.
---

# Map Repository Documentation

Keep operational repository knowledge navigable from root `AGENTS.md`. The map
contains documents meant to guide future work in the repository, not every
Markdown file the repository owns.

## Classify by purpose

Ask whether an agent needs to discover the file to understand, maintain, or
plan work in the repository.

- Map policies, architecture, runbooks, plans, decisions, and navigational
  indexes.
- Treat templates, fixtures, examples, eval inputs or results, historical
  source records, domain reference material, and Markdown whose primary role
  is plugin payload as repository content.
- A `.md` suffix, `docs/` path, or `README.md` name does not decide the class.
- A component README belongs in the map only when it guides maintenance or
  navigation; a README consumed as product content does not.
- Do not add metadata, backlinks, or index files to content merely to satisfy
  the map checker.

Membership is explicit: root `AGENTS.md` starts the map; every other mapped
document declares a repository-relative `parent`. Unmarked Markdown is content
unless a semantic audit identifies it as an unmapped document. This avoids
false positives, but means the checker alone cannot discover orphan documents.

## Map invariant

- Root `AGENTS.md` has no `parent`.
- Every mapped child starts with:

  ```yaml
  ---
  parent: docs/ROADMAP.md
  ---
  ```

- The named parent contains a short, visible Markdown link to the child.
- Each child has one logical parent; useful cross-links are unrestricted.
- Put component guidance beside the component. Keep repository-wide plans,
  decisions, bugs, and maps under `docs/`.
- Reference existing material instead of repeating it.

Before expanding a section, split it only when the material has a distinct
lifecycle, audience, or topic. Leave a short summary and link in the parent.

## Work

1. Read `AGENTS.md`, its mapped children, and nearby candidate files.
2. Classify candidates by purpose before changing metadata.
3. Reuse an existing mapped document when the topic already has a home.
4. For a new mapped document, add `parent` metadata and the parent link in the
   same change.
5. Run the map check.

Resolve `../../scripts/project_docs_context.py` relative to this skill, then
run it from the consumer repository root:

```sh
python3 /path/to/meta/scripts/project_docs_context.py --check
```

For an existing repository, migrate manually: inventory plausible operational
documents, exclude content, add parents and links only to the selected files,
then run `--check`. Automatic migration is intentionally unsupported because
paths and Markdown syntax cannot establish a file's purpose.
