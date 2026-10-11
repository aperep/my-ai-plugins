# Test status

On 2026-10-11, the initial `find-knowledge` revision passed:

- `quick_validate.py` for every skill in `knowledge`;
- Codex plugin validation;
- JSON parsing and the declared Agent Plugins 1.0 schema;
- `git diff --check`;
- local installation as enabled `knowledge@aperep` version `0.4.0`.

The installed manifest and complete installed skill tree matched the checkout.
The `skills-ref` executable was unavailable in this environment.

The unskilled `DEMI` / `ДЭМИ` negative control was run in the current
GPT-5-based Codex session before the skill existed, and the user confirmed its
search paths and no-result conclusion. It is not evidence that the enabled skill
improves retrieval. Automatic routing and a positive retrieval case with a known
record still need a fresh-context run; that debt is recorded in the repository
roadmap.
