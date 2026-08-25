# Trigger cases

| Request | Expected |
|---|---|
| "Rewrite this runbook in simple English." | Load `simple-english` in plain mode. |
| "Make this API error message clear for non-native readers." | Load `simple-english` in plain mode. |
| "Convert this maintenance procedure to ASD-STE100." | Load `simple-english`; read the strict reference. |
| "Audit this document for Simplified Technical English compliance." | Load the skill; state the compliance limit. |
| "Cut the AI slop from this proof." | Load `occam-no-slop`, not this skill. |
| "Write a vivid landing page for this product." | Do not load this skill. |
| "Proofread this mathematical paper." | Load `proofreading-pass`, not this skill. |

## Behavioral cases

- Plain mode: improve a README without imposing word-count limits.
- Strict mode: split a 30-word instruction, place its condition first, and
  preserve a command in backticks.
- Boundary: preserve a deliberate passive when the actor is unknown.
- Compliance: do not invent ASD-STE100 rule numbers or promise certification.
