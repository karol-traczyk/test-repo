# test-repo
Refresh
Testing

## Testing Tips

### What to Test
- Critical user-facing functionality
- Edge cases and boundary conditions
- Previously broken code (regression prevention)
- Complex algorithms and logic

### Writing Tests
- Follow **Arrange–Act–Assert** pattern
- One test = one concept
- Mock external services, time, and random data
- Use descriptive names: `test_what_when_expected`

### Before Merging
- [ ] New code has tests
- [ ] Tests pass locally and in CI
- [ ] Tests are deterministic
- [ ] No hardcoded secrets
