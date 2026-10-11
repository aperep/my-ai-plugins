---
parent: AGENTS.md
---

# Repository roadmap

This is the only active roadmap. Move completed or rejected work to the
[change log](LOG.md) with the decision and reason.

## Shared plugin rules

For every skill change:

1. Record baseline, trigger, and must-not-trigger cases under the skill's
   `evals/` directory.
2. Make the smallest change that clears the baseline failure.
3. Test in fresh context, validate the portable and Codex manifests, and bump
   both synchronized plugin versions.
4. Keep shared skills client-neutral and provide fallbacks for optional
   dependencies.

## Knowledge and Obsidian

The `knowledge` plugin subsumes general knowledge management: canonical homes,
capture, inbox processing, boundary crossing, and audits.

### Proposed `find-knowledge`

Priority: high. Validate the need before creating the skill.

Goal: recover previously recorded information without requiring the user to
remember its wording or location. Start from the current storage's contract and
source map, follow only documented and authorized routes, and distinguish “not
found” from “not searched”. This is read-only retrieval, not web research,
capture, maintenance, or permission expansion.

Baseline example, 2026-10-11: search for a `DEMI` / `ДЭМИ` school desk starting
from `me` and `us`, then the Telegram chats mapped there. Exact local search
found only unrelated uses of “деми”; hybrid and semantic `me` search returned
irrelevant results. The storage map identified plausible family/home Telegram
sources, but host Codex exposes neither `us` semantic search nor Telegram tools;
filesystem search covered `us`, while Telegram remained explicitly unsearched.
A skill cannot repair that capability boundary and must report it.

Before implementation:

- Repeat this case in a fresh context whose client is authorized for both vaults
  and the mapped Telegram chats. Record whether the unskilled agent misses a
  relevant result, loses provenance, stops before a mapped source, or overstates
  coverage. If it succeeds, reject the new skill.
- Add must-load cases for recovering a vaguely remembered fact or artifact across
  mapped stores, and must-not-load cases for code search, web research, filing a
  note, and auditing a storage.
- Test exact spelling, Cyrillic/Latin aliases, inflection, and a cautious category
  paraphrase. Reject semantic matches that lack supporting text.

If the gate passes, add only `skills/find-knowledge/SKILL.md` and its `evals/`.
The workflow should inventory candidate sources from local maps, search each
source with observable query variants, follow documented cross-storage links,
respect audience and tool authorization, and return cited findings plus a
coverage ledger of searched, unavailable, truncated, and still-pending sources.
For Telegram, search one allowlisted numeric chat at a time and account for
pagination, 2,000-character truncation, and unavailable media; do not hardcode
personal paths, chat IDs, or client names in the shared skill.

Done when the enabled fresh-context run finds the relevant record when it is in
an accessible mapped source, or accurately reports the covered sources and gaps
when it is not; it must not present an inaccessible source or a semantic near-hit
as evidence. Then validate and locally install `knowledge` and bump both
manifests together.

Whether a separate `obsidian` technical plugin is needed is not yet known.
Reason from concrete Obsidian-only workflows, the ownership and update cost of
any third-party skills, and portable client support. If no repeated gap
justifies it, remove the reserved empty wrapper rather than duplicating
`knowledge`.

## `research`

### Architecture

The sentence-level research workflow has three stable skill names:

- `interlinear` owns line-tagged LaTeX sources, typed TeX sidecars, and PDF
  views. The distributable `interlinear.sty` contains only stable mechanics;
  `<jobname>.interlinear.tex` contains document data. The usual view uses
  compact badges throughout and expands comments inline only in the requested
  theorem block or subsection.
- `reason` supplies informal or semiformal explanations, local-context notes,
  examples, and gap analysis to `interlinear`.
- `formalize` owns Lean and formal prover work. It runs only when explicitly
  requested and records evidence without silently rewriting the source claim.

`reason` may identify a formalization target, but it does not invoke Lean or
claim formal verification. `formalize` may use Aristotle when that service is
available; the skill must still work with a local Lean toolchain alone.

### Active work

#### `interlinear`

Priority: medium. The stable package, typed sidecar contract, six semantic
comment types, and section-3 fixture exist without Python, CSV, or generated
data.

- Compile every documented mode in a TeX-enabled environment.
- Check focus/badge layout on a longer mixed theorem-and-proof block.

Done when the fixture and a longer proof compile under the supported TeX
engines and fresh routing selects the skill for typed annotation work.

#### `reason`

Priority: medium. Routing and the section-3 context behavior pass. Test a full
proof with a real gap, a valid repair, and a concrete example track.

Done when a full-proof case reports the real gap without strengthening the
claim and completes its example track.

#### `formalize`

Priority: high. Routing and generated-versus-checked behavior pass. Test a
small local Lean declaration and an Aristotle round trip when those tools are
available.

Done when a local Lean fixture compiles, an Aristotle result is checked, and
ordinary proof discussion still routes elsewhere.

## `math-writing`

### `proofreading-pass`

Priority: high. Revise before relying on it.

- Replace the applied symbol-replacement example with a flagged, unapplied
  issue; the current example contradicts the scope rule.
- Make section splitting adaptive. Use subagents only for long independent
  ranges.
- Provide or generate a standalone `-changes.tex` skeleton and test both it and
  the latexdiff output.
- Add evals separating language fixes, notation suspicions, style rewrites, and
  mathematical review.

Done when every applied edit is unambiguous, every judgment call is only
flagged, and all three promised artifacts compile.

### `project-scaffold`

Priority: low. Keep the skill.

- Add trigger evals for new or refreshed mathematical article scaffolds and a
  must-not-trigger copyediting case.
- Test English and Russian minimal projects with `latexmk`, compiling into an
  ignored `output/` directory.
- Test that refresh mode compares existing preamble, notation, and contact
  files instead of overwriting them.
- Keep affiliation and contact reuse behind explicit confirmation.

Done when both minimal variants compile and an existing project is preserved.

## Validation debt

### `biblio`

- `zotero-library`: run fresh-context routing, live add/update/dedup checks, and
  a local Codex install; structural validation only was available when the
  skill was introduced.

### `research`

- `extracting-precise-results`: run behavioral extraction cases against real
  papers, including multiple results and inaccessible full text.

### `math-writing`

- `russian-translation`: run and record an independent fresh-context evaluation
  of the reviewed revision.
- `speech-style-adaptation`: repeat fresh-context routing and behavior checks
  after the later Occam pass and shortening.
