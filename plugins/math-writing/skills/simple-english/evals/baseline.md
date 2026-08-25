# Baseline failures

Recorded 2026-08-25 against revision `11ab79b`.

1. The skill splits into plain and ASD-STE100 modes although it needs one job:
   simple English.
2. Manual rules dominate the skill: procedures versus descriptions, commands,
   conditions, warnings, notes, and sentence quotas.
3. The description narrows simple English to technical documents instead of
   general prose.
4. Attribution and compliance text consume instructions without helping the
   rewrite.

The revision passes when it has one general-prose task, no modes, and no
manual-specific machinery.
