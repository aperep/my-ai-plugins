---
parent: plugins/knowledge/README.md
---

# Validation record

2026-09-18, GPT-6. Baseline agent: `knowledge_baseline`; independent
skill-enabled agent: `knowledge_forward`. Both used synthetic fixtures and
proposed actions; neither executed storage mutations.

## Behavioral assessment

Cases A–H from [the case list](triggers.md) were exercised with the four
knowledge skills and `meta:maintenance`. The enabled pass resolved the two
baseline gaps: no invented inbox/source path, and no processing during capture.
It retained the baseline's correct handling of duplicate capture, extraction,
restricted sharing, failed delivery, source retention, conservative audits,
audit-only maintenance, and an unrelated formatting request.

The first pass exposed ambiguity around partial captures and the meta warning.
After clarifying those two instructions, the same independent agent reran A,
B (including an existing professional excerpt but missing personal excerpts),
and G. All matched the expected outcomes; no regressions were reported.

Final reviewed skill revision: SHA-256
`b0518e6f5c78a9c49f43d689f20eede9cb69a6f6136a1cca1de0eb4cff0aa781`.
Computed from sorted knowledge `skills/*/SKILL.md` followed by meta's
`skills/maintenance/SKILL.md`, concatenating each repository-relative path,
a NUL byte, and its file bytes.

Automatic host skill selection is not proven by these explicitly loaded
scenarios. Real cloud delivery and inbox mutations were not tested.

The 2026-09-21 move-safety revision added `move`, changed `cross-boundary` and
`process-inbox`, and added or changed cases D, E, and I–K. Those cases have not
received an independent fresh-context behavioral run. The final reviewed skill
hash above therefore applies only to the earlier skill revision and the
pre-2026-09-21 versions of cases A–H. The later series-processing change and
case L are also untested. Case M records a user-observed false warning; the
reworded instruction has not received a fresh-context behavioral run.

The 2026-10-10 `agent-charter` addition and cases N–Q have not received an
independent fresh-context behavioral run. Structural and installation checks
for that revision passed: `quick_validate.py` accepted the skill, both JSON
manifests parsed, local `codex plugin add knowledge@aperep` installed and
enabled version 0.3.0, and the installed skill tree matched the checkout.

The 2026-10-11 scenario-validation revision and cases R–S have not received an
independent fresh-context behavioral run. They require named scenario
disclosure, affected-scenario testing after material changes, and separate
evidence for each model that will execute the scenario. `quick_validate.py`,
the declared Agent Plugins JSON Schema, JSON parsing, and `git diff --check`
passed. Local installation enabled `knowledge@aperep` version 0.3.1, and its
installed tree matched the checkout. The `skills-ref` executable was not
available in this environment.

The 2026-10-11 clarification-default revision and case T have not received an
independent fresh-context behavioral run. It requires a safe default alongside
a clarification, puts it first in interactive choices when supported, and
accepts either that choice or a message without expanding the agent's
authority. `quick_validate.py`, JSON parsing, `git diff --check`, and local
installation of `knowledge@aperep` version 0.5.2 passed; the installed skill
tree matched the checkout. The `skills-ref` executable was unavailable.

## Structural and installation checks

- `quick_validate.py`: all four knowledge skills, meta maintenance, and the
  then-named `managing-repository-docs` skill (now `doc-map`) passed.
- `validate_plugin.py`: knowledge and meta passed.
- Parsed all 18 marketplace catalogs and plugin manifests. Both knowledge
  catalog entries resolve to the same shared plugin.
- `codex plugin add knowledge@aperep` and `codex plugin add meta@aperep` passed
  from the local checkout with Codex CLI 0.154.0. Both are enabled. Installed
  manifests and all ten skill files match the checkout.
- The portable Agent Plugin manifest parsed successfully. Nanobot v0.3.5
  discovered and enabled all four skills from a read-only package mount;
  Hermes v2026.9.11 listed the same four as enabled local skills from a
  read-only `skills.external_dirs` mount.
- Documentation-tree checking found no issues in changed documents. Existing
  issues remain outside scope: marketplace 10, me 60, AGora 234, us 243.
- `git diff --check` passed for the changed scope.

Claude CLI was unavailable: its JSON was parsed, but Claude host validation
and installation were not run. Use a new Codex thread to test automatic
discovery of the installed skills.
