# test-repo
Refresh
Testing

## Testing Tips

A comprehensive guide to writing effective tests for this project.

### Think About Test Coverage Strategically

Don't chase 100% code coverage as a vanity metric. Instead, focus on:

- **Critical paths**: Test the core functionality that users depend on daily. If it breaks, users notice immediately.
- **Edge cases**: Boundary conditions, empty inputs, null values, maximum sizes, and unusual but valid inputs.
- **Regression risks**: Areas of code that have broken before or are frequently modified. Add tests to prevent history from repeating.
- **High-complexity logic**: Complex algorithms, business rules, and conditional branches are more likely to contain bugs.

Skip trivial tests (simple getters/setters, framework boilerplate) unless they contain actual logic.

### Write Small, Focused Tests

Follow the **Arrange–Act–Assert** (AAA) pattern:

1. **Arrange**: Set up the test data and preconditions
2. **Act**: Execute the specific behavior you're testing
3. **Assert**: Verify the outcome matches expectations

Each test should verify one logical concept. If you find yourself writing "and" in a test description, consider splitting it into multiple tests.

**Good example structure:**

```
test "user login with valid credentials":
    // Arrange
    user = createUser(email="test@example.com", password="secret123")
    
    // Act
    result = login(user.email, "secret123")
    
    // Assert
    assert result.success == true
    assert result.user.email == "test@example.com"
```

### Keep Tests Deterministic

Tests should produce the same results every time they run. Avoid:

- **External services**: Mock or stub APIs, databases, and third-party services
- **Current time**: Use a fixed timestamp or inject a clock interface
- **Random data**: Seed random number generators or use fixed test data
- **Global state**: Reset any shared state between tests
- **Network flakiness**: Never let tests depend on network availability

If a test fails intermittently, it's worse than no test at all – it erodes trust in the test suite.

### Name Tests Clearly

A test name should tell you:
- **What** is being tested
- **Under what conditions**
- **What the expected outcome is**

Good test names make failures self-explanatory. When a test fails in CI, you should understand the problem from the name alone.

**Good naming examples:**
- `test_calculate_discount_returns_zero_for_negative_price`
- `test_user_registration_fails_with_duplicate_email`
- `test_search_results_sorted_by_relevance_when_query_provided`

**Avoid vague names:**
- `test_user` (what about the user?)
- `test_edge_case` (which edge case?)
- `test_works` (what works?)

### Organize Tests for Maintainability

Structure your tests so it's obvious where to add new ones:

- **Mirror your source structure**: If you have `src/auth/login.py`, tests should be in `tests/auth/test_login.py` or similar
- **Group related tests**: Use test suites, classes, or describe blocks to organize tests by feature or component
- **Keep test utilities separate**: Put test fixtures, factories, and helpers in clearly named files like `fixtures.py` or `test_helpers.py`
- **Document complex setups**: If a test requires elaborate setup, add a comment explaining why

When adding a new feature, create the corresponding test file immediately – don't wait until you have "time to write tests later."

### Run Tests Locally Before Opening a PR

Make it a habit:

1. **Run the full test suite** on your machine before pushing
2. **Check for warnings** in test output – they often indicate problems
3. **Verify tests also pass in CI** after pushing
4. **Don't merge** if CI is red, even if it "works on my machine"

If tests are slow, run only the tests related to your changes first, then the full suite before finalizing the PR.

### Pre-Merge Testing Checklist

Before merging any change, verify:

- [ ] All new code has corresponding tests
- [ ] Tests pass locally and in CI
- [ ] No tests were deleted or disabled without good reason
- [ ] Test names clearly describe what's being tested
- [ ] Tests are deterministic (run them multiple times to confirm)
- [ ] No hardcoded credentials, tokens, or sensitive data in tests
- [ ] Test data is realistic but not copied from production
