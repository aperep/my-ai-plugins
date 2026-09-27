# Trigger tests — maintenance

## Must load

- "Run this repository's maintenance session." Read `docs/MAINTENANCE.md`,
  process `docs/INBOX.md` as directed, and perform the listed routine work.
- "Which guarded prompt files changed since I reviewed them?" Report guard
  drift and stamp problems without changing review stamps.
- "This guarded skill says `metadata.reviewed: now` but has no commit ID. Check
  its review drift." Recover the baseline from the metadata line's Git history;
  do not reject `now` or rewrite the stamp.

## Must not load

- "Fix this bug." If unrelated repository work is noticed, the SessionStart
  guidance may route a proposal to `docs/INBOX.md`; do not turn the bug fix into
  a maintenance session.
