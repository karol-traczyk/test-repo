# test-repo

Refresh

## Clean Code Tips

- **Use meaningful names**: Choose descriptive names for variables, functions, classes, and files so future readers can infer intent without hunting through implementation details.
- **Keep functions focused**: Limit each function to a single responsibility; when it starts branching into multiple concerns, split it into smaller helpers.
- **Return early to reduce nesting**: Guard invalid states or edge cases up front so the main logic stays at the top level instead of buried inside deep `if` / `else` blocks.
- **Prefer clarity over cleverness**: A straightforward solution that everyone can read beats a tricky construct that only its author understands.
- **Comment with purpose**: Let the code explain itself; add comments only when they communicate context or rationale that can’t be expressed cleanly in code.
- **Stay consistent with formatting**: Follow the project’s indentation, brace style, and whitespace conventions so diffs stay clean and reviewers can focus on behavior.
- **Document behavior changes**: Whenever you alter how a feature behaves, update the relevant README examples so contributors have up-to-date guidance.
