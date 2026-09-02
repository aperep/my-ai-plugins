---
name: zotero-library
description: Manage items in the user's Zotero library and synchronize them with repository bibliography records. Use for Zotero reads or writes, not for paper summaries or repository-only note edits.
---

# Zotero library

Use the available Zotero connector. If it is unavailable, report the Zotero part as blocked. Read repository instructions for its collection and local record format; do not assume AGora conventions.

Before creating or changing a citation key, read [the canonical citation-key rules](../../references/citekeys.md).

For writes:

1. Verify bibliographic metadata from an authoritative source.
2. Search by DOI, arXiv ID, citation key, or title and authors; reuse an existing item instead of creating a duplicate.
3. Update items in place. Do not delete and recreate an item, because its Zotero key may be referenced elsewhere.
4. Pin the citation key where the connector supports it, then re-fetch the item to verify the write.
5. When synchronizing a repository record, store the returned Zotero item key. Leave the repository's field empty if no item exists; never invent a key.
