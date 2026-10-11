# Trigger cases

| Request | Expected |
|---|---|
| “Find what I previously wrote about replacing the children's desk; I do not remember where.” | Load `find`. |
| “Search my mapped vaults and chats for our decision about the repair.” | Load `find`. |
| “Where did I save or discuss this idea? Start from this knowledge repository and follow its source map.” | Load `find`. |
| “Recover the document I remember only as a red budget table.” | Load `find`. |
| “Find every caller of `parse_record` in this repository.” | Do not load this skill. |
| “Search the web for current adjustable-desk prices.” | Do not load this skill. |
| “Audit this vault for orphan notes and duplicates.” | Load `audit-knowledge`, not this skill. |
| “Save this message in the right inbox.” | Load `knowledge-rule`, not this skill. |

## Behavioral cases

- Start from named or current stores and follow their documented source map;
  never hardcode a personal path, account, chat, or client.
- Try a bounded set of exact terms and aliases before semantic retrieval.
- Reject semantic near-hits without supporting source text.
- Preserve a stable locator and distinguish quoted facts from inference.
- Respect audience and authorization boundaries; unavailable is not empty.
- Track pagination, truncation, exclusions, and inaccessible attachments in the
  reported coverage when they can change the answer.
- For the `DEMI` / `ДЭМИ` negative control, report no local match and any
  unsearched mapped source; do not invent a desk record or confuse “деми” clothing
  with the brand.
- Make no knowledge-store changes during a retrieval-only request.
