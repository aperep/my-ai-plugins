# Trigger cases

| Request | Expected |
|---|---|
| “Extract the exact hypotheses and conclusion of Theorem 3.2 from this paper.” | Load `extracting-precise-results`. |
| “Add citable numbered results from this paper to my literature survey.” | Load `extracting-precise-results`. |
| “Which proposition proves this claim, and where is it in the paper?” | Load `extracting-precise-results`. |
| “Is this abstract relevant to my project?” | Do not load this skill. |
| “Summarize this paper for a general audience.” | Do not load this skill. |

## Behavioral cases

- Preserve every hypothesis needed by the numbered statement.
- Give a direct link and a page or section when available.
- Keep distinct numbered results separate.
- Paraphrase faithfully unless exact wording matters.
- Disclose inaccessible full text instead of inferring from the abstract.
