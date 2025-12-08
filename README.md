# test-repo

## Using Tools in Agents

These guidelines help engineers build agents that balance internal reasoning with deliberate tool usage.

### When to Call Tools

- Rely on internal reasoning for lightweight deductions the model can handle without outside context.
- Call a tool when you need external data, must take an action (e.g., write a file, post a comment), or require heavyweight computation that is inefficient to do mentally.
- Before invoking a tool, confirm it will add new information or complete a necessary step; otherwise stay within the reasoning loop.

### Planning vs. Execution Tools

- **Planning tools** (such as `todo_write`) should be used at the start of any workflow that has at least three concrete steps or touches multiple areas. Capture the plan before modifying the codebase and keep it updated as understanding evolves.
- **Execution tools** (such as code search, commenting, or launching jobs) should run only when needed and with precise arguments. Double-check parameters so repeated calls are unnecessary.
- Avoid redundant or exploratory tool calls; batch related actions when practical and reuse context you already have loaded.

### Handling Tool Errors and Retries

- Compare each tool’s response with your expectations. If results look wrong or incomplete, diagnose before moving on.
- Decide whether to retry, adjust the plan, or stop by weighing the cost of another attempt against the likelihood of success.
- Surface failures clearly in logs or responses so humans can understand what happened and why a step was skipped or deferred.

### Multi-step Workflows with `todo_write`

- Break complex efforts into at least three actionable todos that describe observable outcomes, not vague intentions.
- Keep exactly one todo marked `in_progress` at any time; update statuses immediately when switching focus.
- Mark todos as `completed` the moment their work is truly finished, and add new todos if additional tasks emerge mid-execution.

### Performance and Efficiency

- Batch independent operations (e.g., read multiple files in one request) when the cost of fetching them together is lower than separate calls.
- Reuse prior context instead of reloading the same data repeatedly; store short summaries when needed.
- Prefer targeted commands over broad scans to keep tool latency low and to avoid unnecessary resource consumption.
