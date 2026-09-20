---
name: dev-grill-docs
description: 'Clarify feature requirements, pressure-test scope and domain terms, and produce a feature spec before implementation. Use for fuzzy requirements, PRD/spec requests, 需求对齐, 拷问需求, or 设计文档. Read existing evidence before asking focused questions. A generic "do not edit code" instruction alone does not trigger intake. Supports --quick, --deep, and --spec-only.'
---

# Dev Grill Docs

Turn the user's feature intent into a usable contract. Preserve decisions already made and ask only about gaps that change behavior, scope, acceptance, or substantial cost. This skill does not implement code or replace analysis-only requests with document work.

Project artifacts belong in the user's project, not the installed skill directory.

## Routing and depth

- Use this entry point for requirement alignment. `--spec-only` limits output to the feature specification.
- When scope is already clear and the user wants implementation steps, plan directly from repository evidence; a particular phrase such as "写个方案" does not override the conversation's actual intent.
- Broken behavior belongs to `dev-fix`. Persistent visual direction belongs in the project's design documentation, outside this requirements workflow.
- `--quick` requests a compact contract and minimal questions; zero questions is correct when evidence is sufficient.
- Default depth covers the material uncertainties. `--deep` adds scrutiny of lifecycle, invariants, compatibility, failures, and reversibility where relevant.
- `--spec-only` disables glossary and ADR writes. It is independent of interview depth.

Explicit analysis-only, chat-only, or no-file instructions govern output. A request to discuss an idea is not permission to write project documents. When the user requests a durable spec or feature-alignment artifact, write `docs/specs/<feature>.md` unless they specify another path or the repository has an established location.

## Gather evidence before questions

Read the supplied brief and relevant existing spec, `docs/CONTEXT.md`, ADRs, models, APIs, tests, or similar features. Follow the repository's search conventions; inspect enough to ground the decisions, without scanning unrelated modules.

Distinguish confirmed requirements, codebase facts, proposed defaults, and unresolved decisions. Do not ask the user for facts the repository can establish. Do not treat an implementation's current behavior as proof of intended behavior.

If the request spans independent subsystems, decompose it before refining details and align the first coherent delivery. For a consequential architectural choice with multiple viable answers, present two or three approaches with tradeoffs and a recommendation. Do not invent alternatives when one approach clearly follows from the evidence.

## Resolve the material gaps

Check whether the intended user, desired outcome, in/out boundary, acceptance behavior, and integration surface are clear enough to write a contract. Ask the highest-impact unresolved question first, with concise context and an evidence-backed recommendation when useful. Group tightly related questions only when the answers depend on each other or the user requests a questionnaire.

Pay attention to domain identity: conflicting names, the same name for different entities, lifecycle transitions, ownership, and invariants. Use established project terms; surface real conflicts instead of silently renaming concepts. A stable vocabulary does not prove the feature is ready.

Use qualitative, evidence-backed gaps rather than invented ambiguity percentages. Do not enforce a minimum interview length, a number of entities, or a quota of acceptance criteria. Stop questioning when the contract is sufficient, the user changes scope, or a concrete external decision blocks progress. If repeated questions produce no new information, name the blocker and preserve useful work instead of cycling.

When the user asks to proceed, incorporate that authorization. Resolve low-impact details from existing conventions and record consequential assumptions. Do not silently decide unresolved high-impact product behavior; mark the affected scope blocked while completing independent parts.

## Write the feature contract

Use a stable existing slug when it identifies this feature. Otherwise choose a descriptive slug from the request; ask only when there is a real collision or ambiguous work item. Preserve existing content outside this task.

```markdown
# <feature> Spec

> Status: DRAFT | ALIGNED | IMPLEMENTED | STUCK
> Source: <request, document, or existing artifact>
> Last updated: <YYYY-MM-DD>

## Background
<User, problem, and intended outcome>

## In scope
<Behavior included in this delivery>

## Out of scope
<Relevant boundaries; say none identified when that is accurate>

## Assumptions
<Consequential defaults and their basis; omit if none>

## Solution
<Minimal behavior and integration sketch, not an implementation task list>

## Edge cases & risks
<Relevant boundaries, failures, invariants, and mitigations>

## Acceptance criteria
- AC-1 <condition or action> -> <observable expected result>

## Open questions
<Specific blocker, affected scope, needed evidence or decision owner; omit if none>
```

Add core entities, state transitions, compatibility constraints, or data contracts when they help downstream implementation. Omit interview transcripts, artificial clarity scores, and empty template sections. Preserve existing AC identifiers during revisions.

Status semantics:

- `DRAFT`: proposed requirements remain subject to alignment; specify what remains unresolved.
- `ALIGNED`: material requirements are supported by user direction or an accepted source, and no implementation-blocking question remains. Routine inferred details may be recorded as assumptions.
- `STUCK`: a concrete unanswered decision or unavailable evidence blocks the intended scope. Identify it explicitly; do not advance affected implementation on that basis.
- `IMPLEMENTED`: retain only when actual implementation evidence supports it; this intake skill does not implement the feature. Changed requirements invalidate that status for the affected scope.

Before handoff, check the contract for placeholders, internal contradictions, avoidable ambiguity, and scope too large for one coherent implementation. Fix supported defects directly; surface only decisions that still require the user.

## Durable documentation

Only in documentation-authorized work outside `--spec-only`, persist reusable knowledge when it meets these gates. Follow existing project paths and format before creating new ones.

- `docs/CONTEXT.md`: stable domain terms, boundaries, aliases, and evidence-backed meanings. Update related glossary rows only. Keep task checklists, transient copy, unresolved guesses, and implementation diaries in the task artifact.
- `docs/adr/<nnnn>-<slug>.md`: an accepted decision with real tradeoffs, reuse across features/modules, meaningful reversal cost, and a rationale future readers need. Naming choices and local implementation details do not qualify. Use the project's numbering convention; otherwise the next unused number. Record Context, Decision, Consequences, status, and date. Do not label an unconfirmed proposal Accepted.

Durable notes must not conflict with the spec. A decision local to this feature belongs in its plan when implementation planning is requested.

## Handoff

Report the artifact path and status, material decisions, remaining blockers, and the next useful action. Mention glossary/ADR changes only if made. If the user requested intake only, stop after the deliverable. If their broader request already authorizes implementation, continue within that scope when requirements are sufficient; do not require a new skill invocation as a permission ceremony.

## SDD Contract

The downstream anchors are `In scope`, `Out of scope`, `Assumptions`, `Open questions`, and stable `Acceptance criteria`. Existing glossary and ADR decisions also constrain implementation. Report and reconcile material spec drift before delivery instead of treating the artifact as proof that code complies.
