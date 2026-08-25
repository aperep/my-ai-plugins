# Long documents

Use a section map rather than arbitrary fixed-size windows.

1. Inspect the preamble, document structure, project instructions, and any
   existing glossary.
2. Map sections, theorem blocks, inputs, and parallel source/target files.
3. Work in coherent units small enough to compare against the source. Keep one
   unit of surrounding context on each side when continuity matters.
4. Maintain one glossary and a short list of unresolved choices across units.
5. After each substantial unit, review the diff and run the cheapest useful
   structural or build check.
6. Finish with a whole-document pass for terminology, references, duplicated or
   missing paragraphs, and transitions across unit boundaries.

For several files, choose dependency order when terminology or notation flows
between them; otherwise a small representative file is a useful first pass.

Delegation is optional. Use it only when the user permits it and units are truly
independent. One translator must reconcile terminology and voice across all
outputs.
