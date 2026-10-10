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

## 2026-09-21 series-processing gap

`process-inbox` lacked classify-first series handling with per-item sources,
risking inconsistent routing or bulk retirement. Case L covers this untested
behavior.

## 2026-09-21 meta-availability wording gap

A user observed that `knowledge-rule` warned that its `meta` dependency was not
loaded even though `meta:*` skills were available. The instruction tested the
ambiguous state "loaded" instead of the observable state "available". Case M
covers the corrected distinction.

## 2026-10-10 agent-charter gap

Repository agent blueprints existed as infrastructure-adjacent role,
capability, and preference files without a reusable vault-local structure.
There was no shared rule for inheritance, manual materialization into runtime
Markdown, or exact disclosure after an agent edits its own durable files. The
user explicitly requested one reusable knowledge skill and the standard
`docs/charter/` layout. Cases N–Q record the requested behavior; no independent
behavioral run has exercised them yet.
