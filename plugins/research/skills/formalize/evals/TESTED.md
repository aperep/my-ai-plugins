# Formalize test status

## Pipeline scaffold: 2026-09-17, research 0.5.0

Implemented and checked in the Codex GPT-6 session on `comal-lean`:

- Official `aristotlelib==2.1.0` inspected and invoked. The public version
  endpoint returned Lean 4.28.0 and mathlib
  `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
- Nine offline tests passed against the SDK import boundary: explicit file
  snapshot, changed archive, unsafe input paths, unsafe result archive,
  no overwrites, immediate ID persistence, uncertain submission recovery,
  bounded polling/result-only retrieval, and missing credentials. These mock
  remote operations; they do not establish live service success.
- `comal-lean`'s finite eigencomponent theorem compiled locally. Its original
  target type and axiom report were checked. An unfinished request and a
  deliberate extra axiom both failed acceptance. The paper's vector-field
  specialization is still open.
- Skill validation passed; Claude plugin/catalog validation passed with the
  existing unversioned-manifest warnings. Codex installed 0.5.0 from the local
  marketplace. Its changed runtime files are checked directly below the cache.

Run the offline tests with:

```sh
uv run --with aristotlelib==2.1.0 python -m unittest discover \
  -s plugins/research/skills/formalize/scripts -p 'test_*.py'
```

Limits: no API key was available, so no live submission or returned proof was
checked. Fresh-context model routing was not rerun; the prior routing evidence
below predates this workflow change. The marketplace-wide documentation check
reports a pre-existing missing root `AGENTS.md`; the consumer's doc tree passes.

## Earlier routing checks

On 2026-08-26, revision `ac7d6c0` was installed locally as
`research@aperep` version `0.4.1` and tested in fresh context with
`gpt-5.6-sol` under Codex 0.149.1.

- A natural-language request to formalize and compile a selected Lean lemma
  selected `research:formalize`; no `$formalize` spelling was required.
- Given plausible Aristotle output with no checker run, the behavior case used
  `generated`, not `checked`, and required a stable declaration, exact Lean
  toolchain, and successful checker output.
- An ordinary proof-explanation case selected `research:reason`, not
  `formalize`.

No local Lean executable or Aristotle connection was available, so an actual
formal proof run remains untested.
