# Interlinear research roadmap

Implemented and retained as the supported core:

1. Sentence labels and CSV-backed translation/comment views.
2. Heuristic active-context spans and JSON context export.
3. Candidate lookup against a supplied local Stacks-style index.
4. Parallel proof-on-example tracks and deterministic gap reporting.

Possible extensions, not current capabilities:

- a full Stacks/Kerodon/Mathlib index with semantic retrieval;
- formal Lean status and independently compiled proof artifacts;
- generation of board content and speaker notes from selected labels;
- a project state file connecting open questions to proved or verified lemmas.

Add an extension only as a tested vertical slice. Preserve the CSV label bus so
renderers and verification tools can evolve independently.
