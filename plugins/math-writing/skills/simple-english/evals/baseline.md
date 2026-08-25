# Baseline failures

Recorded 2026-08-25 from the repository and the upstream skill at commit
`8e8a008a13e4b478f9ccc20ca16e79aef66c0739`.

1. Codex does not install the companion named by `occam-no-slop`.
2. The upstream description treats “de-slop” and “make this readable” as STE
   triggers. These collide with structural editing and ordinary prose work.
3. The upstream default applies rigid 20/25-word limits and controlled-language
   mechanics to normal documentation, although users did not request STE.
4. Its full rule catalog loads for every task. Most plain-language edits need a
   small core, not 53 rules and several lookup tables.
5. Mathematical narrative and technical procedures need different treatment;
   one universal clarity pass can damage the former.

The local refactor passes when it is available on both hosts, routes narrowly,
keeps ordinary technical English flexible, and loads strict rules only for an
explicit STE request.
