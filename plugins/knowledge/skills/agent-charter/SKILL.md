---
name: agent-charter
description: Create, edit, inherit, compare, or reconcile a repository's docs/charter blueprint for its attached agent. Also use when that agent changes its own durable instruction or personality Markdown and must report the exact self-change. Do not use for ordinary AGENTS.md edits unrelated to an attached agent.
---

# Maintain an agent charter

A repository charter is the human-authored blueprint for its attached agent.
It lives under `docs/charter/`; the agent does not load it as runtime
instructions. Runtime-specific procedures materialize it into the agent's
internal Markdown files.

Use these standard files:

- `README.md`: attached agent, repository, inheritance, and file index;
- `ROLE.md`: purpose, responsibility, exclusions, and success criteria;
- `CAPABILITIES.md`: intended access, authority, and enforced limits;
- `PERSONALITY.md`: character, communication style, and stable preferences;
- `CONTEXT.md`: durable local context and canonical sources;
- `SCENARIOS.md`: recurring triggers, actions, outcomes, and escalation cases.

Keep live tasks, schedules, transient memory, tool schemas, and deployment
configuration in their existing canonical systems. Link them from the charter
only when the blueprint needs the context. `AGENTS.md` remains the repository
contract for agents editing the repository; encountering a charter does not
assign its identity to the editor.

## Inheritance

Name the parent charter in the local `README.md`. Read the complete parent and
then the local charter. Local text adds repository-specific behavior and
overrides the parent only when it says so explicitly. Report unresolved
conflicts instead of inventing merge semantics.

## Reconciliation and self-change

Treat the charter as canonical human intent. The attached agent must not edit
it. Follow the runtime repository's documented reconciliation procedure to
compare the charter with internal files, apply reviewed changes, and verify
what the runtime actually loads. Manual reconciliation is primary; an agent
may occasionally compare its internal files with the charter and report drift.

The attached agent may update its own durable instruction, personality, or
context Markdown under its normal runtime rules. After every such self-change,
it must report the exact changed paths and the exact edits, using a diff or an
equally precise before-and-after account. A summary such as “updated memory” is
not sufficient. It must not propagate the change into the charter.
