---
name: zotero-library
description: Search, add, deduplicate, and safely update items in the user's Zotero library, including pinned citation keys and synchronization with repository bibliography records. Use when a request acts on Zotero itself or links a local bibliography record to Zotero; do not use merely to summarize a paper or edit a repository-only note.
---

# Zotero library

Use the available Zotero connector for library mutations. If no Zotero connector is available, report that part as blocked; continue with a repository-local record only when the repository permits it. Never invent a Zotero item key.

## Repository contract

Read the target repository's instructions before acting. The repository owns its collection name, note path and schema, tags, link field, and content-fill policy. Do not assume AGora or any other collection by default.

This skill owns the user's citation-key convention and safe Zotero operations. Read [the canonical citation-key rules](../../references/citekeys.md) before creating or changing a key.

A local bibliography record may exist before its Zotero item. Preserve the repository's empty value for an unsynchronized item rather than adding a redundant status field. When synchronization succeeds, write the returned Zotero key into the local record in the same task.

## Workflow

1. Verify title, authors, date, and persistent identifiers on an authoritative abstract, DOI, publisher, or indexing page. Search snippets are leads, not metadata sources.
2. Search before adding. Check citation key, DOI, arXiv ID, then normalized title plus authors. Scope to a collection only when the repository or user names one.
3. Add through an idempotent URL or DOI operation when available. Reuse and file an existing item instead of creating a duplicate.
4. Compute the citation key from the canonical rules and check collisions in both Zotero and the repository. Where supported, pin it in both the native citation-key field and an `Extra` line of the form `Citation Key: <key>` so local and web lookups agree.
5. Correct metadata in place. Never delete and recreate an item to change its type, venue, or citation key: that changes the item key and breaks local links.
6. Re-fetch every material write and compare the persisted fields. A success response without matching re-fetched data is a failure; stop instead of retrying blindly.
7. Update the repository record with the verified item key and report any fields that remain unresolved.

For an arXiv match, require a compatible title and author list; otherwise leave the arXiv field empty. For publication metadata and MR numbers, use an authoritative index such as MathSciNet when available. An online journal article may be updated to a journal item before pagination exists, but its citation-key year changes only under the canonical year rule.

## Batches and duplicates

Respect the connector's current rate limit. Independent papers may be processed concurrently only when the shared Zotero account limit remains safe; otherwise use small waves or sequential calls.

Use a connector's duplicate finder and dry-run merge preview when available. Do not choose an item for deletion by guesswork. Preserve attachments and child items during a merge.

## Report

Return the item key, citation key, collection used if any, authoritative source, and synchronized local path. Call out absent identifiers, inconclusive matches, failed persistence checks, and local-only records.
