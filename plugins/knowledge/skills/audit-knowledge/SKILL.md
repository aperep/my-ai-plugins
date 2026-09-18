---
name: audit-knowledge
description: Audit a knowledge storage for orphan notes, duplicates, broken links, stale facts, and inbox or attachment problems; propose changes by default. Use for knowledge maintenance, not automatic cleanup or a repository documentation-tree check alone.
---

# Audit knowledge

Read [knowledge-rule](../knowledge-rule/SKILL.md) and local maintenance
instructions. Stay within their scope; use their inbox age threshold and
lifecycle rather than inventing global defaults.

Look for:

- Orphan notes and near-duplicates.
- Broken links and the same entity under different names.
- Stale operational facts and tasks without context.
- Inbox items older than the local threshold and attachments without notes.
- Handwritten indexes that could become computed views.

Report evidence and propose a diff or equivalent change preview. Do not apply
cleanup unless requested. Orphans are not automatically useless, similar names
are not proof of identity, and inaccessible links are unverified, not broken.
Preserve authored explanations when replacing an index with a view.

Repository maintenance may call this skill; processing is a separate operation
handled by [process-inbox](../process-inbox/SKILL.md).
