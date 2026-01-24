# test-repo
Refresh
Testing

## Testing Tips

### Focus Your Test Coverage

Prioritize testing:
- **Critical paths** – core functionality users depend on
- **Edge cases** – boundary conditions, null/empty inputs, max sizes
- **Regression risks** – code that's broken before or changes frequently
- **Complex logic** – algorithms and conditional branches

Skip trivial tests (simple getters/setters) unless they contain actual logic.

### Write Clean Tests

Use **Arrange–Act–Assert**:
1. Set up test data
2. Execute the behavior
3. Verify the outcome

Each test should verify one concept. If your test name includes "and", split it.

### Keep Tests Deterministic

Avoid flaky tests by eliminating:
- External services (mock APIs and databases)
- Time dependencies (use fixed timestamps)
- Random data (seed generators or use fixed values)
- Global state (reset between tests)

### Name Tests Clearly

Format: `test_what_when_expectedOutcome`

Good: `test_user_registration_fails_with_duplicate_email`  
Bad: `test_user` or `test_edge_case`

### Organize Tests

- Mirror source structure (`src/auth/login.py` → `tests/auth/test_login.py`)
- Group related tests in suites or classes
- Keep fixtures and helpers in separate files

### Pre-Merge Checklist

- [ ] New code has tests
- [ ] Tests pass locally and in CI
- [ ] Test names are descriptive
- [ ] Tests are deterministic
- [ ] No hardcoded credentials or production data
