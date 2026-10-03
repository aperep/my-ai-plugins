# Reason baseline cases

## Respect tagged local context

**Task.** Explain the step at `dJ2z` using its explicit `context` comment and
the earlier tagged source line it names.

**Failure without the skill.** Summarize every earlier note, treat a translation
as a hypothesis, or omit which assumptions the explanation used.

**Expected behavior.** Name only the definitions and statements actually
invoked by the context comment, then explain the target from them.

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
