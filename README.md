# test-repo
Refresh

## Prompt tips

Writing clear and effective prompts helps coding agents deliver better results. Here are some practical tips:

- **Be specific about the goal**: State exactly what you want to achieve. Instead of "fix the bug", say "fix the null pointer exception in the login handler when username is empty."
- **Provide context**: Mention relevant files, functions, or frameworks. For example: "In `auth.py`, refactor the `validate_user()` function to use bcrypt instead of plain text."
- **Break down complex tasks**: Split large requests into smaller, actionable steps. Request "Add user authentication" as separate prompts: schema design, API endpoints, then frontend integration.
- **Specify constraints and preferences**: Mention coding style, libraries to use/avoid, performance requirements, or compatibility needs (e.g., "Use TypeScript with strict mode" or "Ensure Python 3.8+ compatibility").
- **Use examples when helpful**: Show input/output samples or reference similar existing code. "Make the error messages look like the ones in `utils/errors.js`."
- **Ask for explanations when learning**: Include phrases like "explain your changes" or "add comments" to understand the agent's reasoning and learn best practices.
- **Review and iterate**: Treat the first response as a draft. Provide feedback like "move that validation earlier in the function" or "add error handling for network failures."
- **Mention testing needs**: Specify if you need unit tests, integration tests, or edge case handling. "Add tests for empty input, special characters, and SQL injection attempts."

---

*Authored (in part) by the Cursor agent.*
