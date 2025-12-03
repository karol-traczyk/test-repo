# test-repo
Refresh

## Testing

### Current status
This repository only contains documentation (`README.md`). No automated test runner or package manifest is committed yet, so treat the steps below as the full test plan until code and tooling are added.

### Full verification checklist
1. Open the Markdown preview in your editor to confirm headings and spacing render correctly.
2. Run the built-in whitespace check before committing:

```bash
git diff --check
```

3. If you have Node.js/npm available, lint the Markdown with the default ruleset (no extra config required in this repo):

```bash
npx markdownlint README.md
```

### Running subsets or watch mode
Not applicable yet—there is no automated suite to slice or watch. Once you add a runner (Jest, Vitest, Pytest, etc.), document the exact `--watch` or `-k` flags here so contributors can run focused feedback loops.

### Coverage reports
Coverage tooling is not configured. When you wire up a test runner, add the command you settle on (for example `jest --coverage` or `pytest --cov`) so CI and local workflows stay in sync.

## Testing tips
- When adding actual source code, keep tests either in a top-level `tests/` directory or next to the feature under test using a `.test`/`.spec` suffix.
- Prefer fast unit tests for helpers and pure functions; layer integration tests only where a full workflow from the README needs protection.
- Share fixtures or snapshots under `tests/fixtures/` (or a similar helper folder) so data is easy to reuse without cluttering the repo root.
- Update this section as soon as you add real tooling—documenting the runner, commands, and expectations here keeps the README the single source of truth.
