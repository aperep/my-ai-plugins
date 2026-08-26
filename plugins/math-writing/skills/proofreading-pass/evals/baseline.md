# Baseline failures

Recorded 2026-08-26 against revision `6627a3e`, after the Christophersen paper
proofreading pass.

1. Valid voice choices such as “So” to “Thus”, “we will get” to “we obtain”,
   and sentence tightening were applied to the corrected source.
2. `[Flagged — not changed]` mixes status with category, so categories cannot
   consistently distinguish applied changes from suggestions.
3. The change log starts with applied edits rather than identifying the major
   issues and their original-source lines.
4. The skill's notation example applies a suspected symbol replacement even
   though its scope rule says to leave such changes to the author.

The revision passes when voice choices and notation suspicions are suggestions
only, every entry has an independent status and category, and the log opens
with the count and line numbers of major issues.
