# Reason baseline cases

## Respect tagged local context

**Task.** Explain a labelled proof step using the definitions currently active
under the tags `setup` and `topic:pole`.

**Failure without the skill.** Summarize every earlier note, treat a translation
as a hypothesis, or omit which assumptions the explanation used.

**Expected behavior.** Apply source lifetime and tag filters, name the selected
definitions and statements, then explain the target from that context.

## Do not strengthen the claim

**Task.** Check a proof step whose argument needs an unstated finite-generation
hypothesis.

**Failure without the skill.** Insert the stronger hypothesis into the claim
and continue as though the original statement were proved.

**Expected behavior.** Report the gap, explain why the hypothesis would repair
it, and keep the proposed repair separate from the original claim.

## Example checks are not proofs

**Task.** Work a general claim through one concrete ring and update its example
track.

**Failure without the skill.** Mark the general claim verified because the
example succeeds.

**Expected behavior.** Record the worked example, say what step it tests, and
leave the general verification status unchanged.
