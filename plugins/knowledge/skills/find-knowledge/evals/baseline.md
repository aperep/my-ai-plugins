# Baseline status

Recorded 2026-10-11 against repository revision `dd2ab45` in the current Codex
session, before `find-knowledge` existed.

The user asked to find information about a `DEMI` / `ДЭМИ` school desk starting
from the `me` and `us` knowledge stores and then the Telegram chats mapped from
them. The unskilled run:

1. Read both storage contracts and the source map reached from `me`.
2. Tried exact Cyrillic and Latin terms, relevant inflections, and broader desk
   terms in both local stores.
3. Used hybrid and semantic search where the current client exposed it, but did
   not report unsupported near-hits.
4. Identified the mapped household Telegram sources and reported that this
   client had no authorized Telegram tool instead of claiming to search them.
5. Reported no match in the searched stores rather than claiming that the
   knowledge did not exist.

The user confirmed that the search paths were appropriate and that the knowledge
was absent. This is a successful negative control, not a demonstrated baseline
failure. The user nevertheless requested a reusable skill for this workflow.

A positive baseline remains necessary: place a known record in a mapped
secondary source, give a request that does not reveal its wording or location,
and compare unskilled and enabled fresh-context runs. Do not claim measured
improvement until that case exposes and then clears an observable failure.
