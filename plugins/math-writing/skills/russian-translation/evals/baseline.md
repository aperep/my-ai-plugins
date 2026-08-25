# Baseline failures — russian-translation

Recorded 2026-08-25 against the pre-rewrite `SKILL.md` at commit `09b8a9b`.

| Task | Observable failure in the old skill |
|---|---|
| Translate one standalone mathematical abstract | Assumes a thesis tree, local macros, and a fixed TeX build command. |
| Revise existing Russian theorem prose | Loads a 400-line mixed manual instead of a focused voice guide. |
| Adapt voice without changing content | Several rules encourage added transitions and project notation, risking content drift. |
| Translate a dissertation acknowledgment | Contains live grant, address, email, and acknowledgment text that can be copied without confirmation. |
| Translate a long chapter | Prescribes host tool names, arbitrary windows, and automatic commit/push actions. |
| Change one technical term consistently | Treats grep counts and one-edit-per-occurrence as the workflow instead of checking inflection and meaning. |

The rewrite must preserve formulas and meaning, discover project conventions,
route optional detail, and perform no unrequested version-control or network
action.
