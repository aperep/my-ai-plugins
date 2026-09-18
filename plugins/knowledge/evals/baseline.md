---
parent: plugins/knowledge/README.md
---

# Baseline

2026-09-18, GPT-6, independent agent `knowledge_baseline`, before the knowledge
skills existed. Eight synthetic requests are recorded in [cases](triggers.md).
The agent proposed actions; it did not execute storage mutations.

Capture A invented `Personal/sources/chat-42.md` and immediately filed derived
facts and a task into people notes. The supplied fixture had no such source
route. Its final caveat acknowledged that new paths needed local validation.
The accepted workflow instead resolves the inbox first and leaves processing
for a separate session. These are the narrow gaps the capture rules address.

The other proposals already handled duplicate capture, extracting an independent
paragraph, restricted sharing, an unavailable destination, preservation of the
only source copy, conservative audits, audit-only maintenance, and formatting
without knowledge work. No improvement over those baseline behaviors is claimed.

The user explicitly requested these conventions as a reusable plugin. Passing
baseline cases remain regression cases, not evidence that every rule fixes a
newly observed defect.
