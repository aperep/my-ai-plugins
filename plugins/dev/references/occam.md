---
reviewed: 04038a2
---

# Occam

Apply this only after the required behavior and known constraints are clear.
Evaluate the relevant existing and proposed structures; neither is necessary
by default. Stop at the first option that satisfies the requirement:

1. Build nothing or delete obsolete structure.
2. Reuse code already present.
3. Use the standard library.
4. Use a native platform feature.
5. Use an already-installed dependency.
6. Add the minimum new code.

Do not simplify away requested behavior, safety, trust-boundary validation,
necessary error handling, accessibility, or physical calibration. Occam
chooses solution shape; it does not replace investigation, tests, review, or
verification.
