# Baseline failures

Recorded 2026-08-25 against the pre-refactor skill at revision `2259a73`.

| Task | Observable failure in the old skill |
|---|---|
| Adapt one standalone mathematical paragraph | Loads thesis paths, protected-directory rules, long-file mechanics, and build commands unrelated to the task. |
| Adapt TeX in an arbitrary repository | Assumes `tex/CLAUDE.md`, a fixed `tex/` layout, corpus macros, and `pdflatex` instead of discovering project conventions. |
| Revise a thesis chapter | Treats one repository's filenames, source directories, contribution sentence, address, email, and grant as defaults. |
| Adapt several files | Mandates obsolete Claude agent types and one worker per file rather than testing size, independence, shared notation, and authorization. |
| Match voice without changing structure | Generic anti-slop and list rules overlap `occam-no-slop` and can broaden a local voice edit into structural rewriting. |
| Follow the corpus faithfully | Claims new ideas almost always begin with a connective, although the corpus contains many ordinary subject-first sentences; this invites mechanical imitation. |

Recorded later that day against revision `e7d2c83`: the replacement
`project-work.md` still prescribed generic project discovery, chunking,
delegation, validation, and reporting that do not belong to a voice skill.

The revision passes when the common path is host-neutral and content-preserving,
no generic project workflow remains, factual metadata requires confirmation,
and voice rules remain distinct from de-slopping.
