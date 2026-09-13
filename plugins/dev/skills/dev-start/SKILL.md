---
name: dev-start
description: Start an ambiguous development request by inspecting enough evidence to choose requirements alignment, bug investigation, or implementation. Use when the user asks to begin with understanding or triage, or when deciding whether a request is an unclear feature, an unexplained defect, or a defined change is itself the task. Do not use for an already clear review, verification, or delivery request.
---

# Development Start

Choose the first useful development lane without creating a preliminary artifact
or turning the choice into a workflow ceremony. Read
[the shared development baseline](../../references/dev-baseline.md).

## Establish only what changes the route

Read the request, relevant repository instructions, nearby code and tests, and
available failure evidence. Determine:

- what observable behavior is wanted;
- whether current behavior violates an established expectation;
- whether the cause is already supported by evidence;
- whether a missing product decision prevents implementation.

Do not require a complete specification merely to classify the work. Ask a
question only when its answer changes the lane and cannot be established from
the repository or conversation.

## Choose one primary lane

- Use `dev-grill-docs` when intended behavior, scope, or acceptance remains
  materially unclear.
- Use `dev-fix` when established behavior is broken and the cause still needs
  investigation.
- Use `dev-tdd` when desired behavior is clear: a feature, refactor, or defect
  whose cause and required correction are already understood.
- Use `dev-verify`, `dev-code-review`, or `dev-finish` directly when the request
  already concerns that completed-work phase.

A request being called a “bug” does not establish its cause. Conversely, a
known regression does not need a second diagnostic workflow merely because it
is broken.

## Continue or report

This skill itself is read-only: do not edit code, write documentation, stage,
commit, or publish merely to select a lane. If the user's broader request
already authorizes downstream work, load the selected skill and continue in the
same task. If the user asked only for triage, report the selected lane, decisive
evidence, and the one unresolved fact that would change it, if any.
