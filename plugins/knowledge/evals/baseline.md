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

## 2026-09-21 move-safety gap

No skill owned moves in general. `cross-boundary` required destination
verification before source removal, but moves can also occur within one storage
and during ordinary inbox processing. The earlier guidance supplied no batch
inventory, per-item reconciliation, fidelity criteria, or required user-facing
transfer report. That leaves partial inbox migrations vulnerable to
unverifiable omissions or unsafe bulk cleanup. Cases D, E, and I–K record the
requested behavior; no independent behavioral run has yet exercised the new
workflow.
