# Trigger cases

| Request | Expected |
|---|---|
| "Add this DOI to my Zotero library and pin my citation key." | Load `zotero-library`. |
| "This preprint is now published; update its Zotero venue without breaking links." | Load `zotero-library`. |
| "Synchronize these local bibliography notes with their Zotero items." | Load `zotero-library`. |
| "Check whether these two Zotero records are duplicates." | Load `zotero-library`. |
| "Summarize Theorem 3.2 from this paper." | Do not load this skill. |
| "Create a repository-only bibliography note and leave Zotero untouched." | Do not load this skill. |
| "Verify these LaTeX bibitems against published metadata." | Do not load this skill unless Zotero is also part of the request. |

## Behavioral cases

- Read repository instructions for collection and local schema; never assume AGora.
- Search and deduplicate before adding.
- Leave a repository-defined Zotero field empty when local-only notes are allowed; never fabricate a key or add a redundant status field.
- Update items in place and verify by re-fetching.
- Stop after a reported-success write fails persistence verification.
- Apply the canonical citation-key rules without silently renaming legacy keys.
