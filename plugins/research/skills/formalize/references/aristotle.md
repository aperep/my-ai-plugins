---
parent: plugins/research/skills/formalize/SKILL.md
---

# Aristotle round trip

Use the bundled `scripts/aristotle.py` with `uv run`. It pins the official
`aristotlelib==2.1.0` SDK; no MCP server is required. Inspect `--help` before
adapting examples. The old `Project.prove_from_file` API is not present in
this SDK. Its `aristotle show` CLI may wait for completion; the helper's
`status` makes a single poll.

## Prepare

Check the project's toolchain and mathlib revision against Aristotle's live
`https://aristotle.harmonic.fun/api/v3/version` response. Preserve existing
project pins unless migration is part of the task; report mismatches.

Prepare one explicit target with stable names and all required local imports.
Prefer a self-contained Lean file importing mathlib for the first attempt.
Include the toolchain, Lake configuration, and manifest. An explicit file list
is the upload boundary; the helper does not resolve imports. Include additional
local modules when needed. Keep credentials and unrelated files outside it.

Write a prompt file stating the target, hypotheses, proof sketch, and that
definitions, statement, and version pins must be preserved. Then run:

```sh
uv run /path/to/formalize/scripts/aristotle.py prepare \
  --project /path/to/lean-project --run /path/to/attempt \
  --prompt-file /path/to/prompt.txt \
  --file Target.lean --file lean-toolchain \
  --file lakefile.toml --file lake-manifest.json
```

The new attempt directory contains `input.tar.gz` and `request.json` with the
exact prompt and file/archive hashes. Review those before submitting.
Supply `ARISTOTLE_API_KEY` through the environment, never as a command argument.

## Submit and resume

```sh
uv run /path/to/formalize/scripts/aristotle.py submit /path/to/attempt
uv run /path/to/formalize/scripts/aristotle.py status /path/to/attempt
uv run /path/to/formalize/scripts/aristotle.py fetch /path/to/attempt
```

Submission persists the returned project ID immediately. Poll only while useful
and keep the user informed during long jobs. Run one command at a time per
attempt directory. Do not start another job just
because the current one is slow. If submission times out, inspect remote
history (`uvx --from aristotlelib==2.1.0 aristotle list`) and recover the project
ID into the receipt; do not blindly retry an uncertain submission. The SDK
itself can retry HTTP requests, so also check for duplicate jobs after errors.

`fetch` requires an idle project with result files, preserves the archive, and
extracts regular files/directories into a new `result/`. Failed or partial tasks
may have useful files. Their existence or a remote `COMPLETE` status does not
mean a checked proof. The helper never promotes a result to `checked`.

## Local acceptance

1. Review the result diff, imports, definitions, and theorem type. Inspect any
   executable Lean metaprogramming before compiling. Keep the trusted project's
   Lake files and toolchain; do not run an arbitrary returned build setup.
2. Check the candidate in the pinned local project. A contract file should
   re-state the intended type and prove it by the returned declaration, then
   run `#print axioms Namespace.theoremName`.
3. Run `lake build` and `lake env lean -DwarningAsError=true Contract.lean`.
   Require the target and its dependencies to be free of `sorryAx` and new
   axioms. Mathlib's usual `propext`, `Classical.choice`, and `Quot.sound` are
   acceptable. Disclose any other trust dependency; never mark an axiom-backed
   result as an unconditional proof of the paper.
4. Preserve a checker log and receipt with declaration name, source location,
   exact versions, accepted-file hashes, axiom output, and any statement
   mismatch. Only then record `checked` in the consumer's evidence or sidecar.

This check establishes the Lean statement. A separate mathematical review
must establish that its definitions and hypotheses represent the paper.
