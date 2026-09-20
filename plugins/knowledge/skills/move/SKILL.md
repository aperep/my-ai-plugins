---
name: move
description: Safely relocate one or many knowledge objects, including inbox items, within or across repositories, vaults, clouds, and other stores. Use when the destination should become canonical and source removal matters, not for copying, sharing, or editing in place.
---

# Move knowledge safely

Read [knowledge-rule](../knowledge-rule/SKILL.md) and the source and destination
rules. Resolve the exact objects, destinations, attachments, and references in
scope. Confirm that the requested operation and local policy permit source
removal. If the move crosses a storage or audience boundary, also read
[cross-boundary](../cross-boundary/SKILL.md).

Use a native atomic, no-clobber move only when the storage system guarantees it
for the resolved source and destination; a command named `move` may still copy
and delete across filesystems. Verify the resulting destination. Otherwise,
stage or copy the object, verify it, and only then remove its source. At the
destination, prefer staging followed by an atomic publish when supported.

Match verification to the object: compare bytes or hashes for files, and
re-read structured records to confirm content, provenance, metadata, links,
and attachments that must survive. A success response or matching item count
alone is insufficient. Remove only the exact source whose destination passed
verification. Prefer recoverable deletion when available. Update known
references and leave a useful redirect where local conventions support one.

For a batch, first make a stable inventory of source identifiers and intended
destinations. Track each item through transfer, verification, and source
removal, then reconcile the inventory. A failed or ambiguous item stays at the
source. Make retries resume from recorded state and inspect the destination
before transferring again. Never bulk-delete sources from a batch-level
success signal alone.

Report what moved from where to where, what remains at the source, and every
failed or pending item. For batches, include reconciled counts and the location
of any durable manifest or log. If the destination is unavailable or
verification fails, keep the source and report the pending work.
