# test-repo
Refresh

## ClickUp Tasks CLI Tool

A simple Python CLI tool to fetch and display your most recently updated tasks from ClickUp.

### Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Set your ClickUp API token:
```bash
export CLICKUP_TOKEN='your_clickup_api_token_here'
```

You can get your API token from: https://app.clickup.com/settings/apps

### Usage

Basic usage (fetches last 5 tasks for user ID 307142 in workspace "Karol"):
```bash
python scripts/clickup_tasks.py
```

#### CLI Options

- `--workspace NAME` - Workspace (team) name (default: "Karol")
- `--assignee ID|NAME|EMAIL` - User ID, name, or email (default: "307142")
- `--limit N` - Number of tasks to fetch (default: 5)
- `--order FIELD` - Order by: updated, created, or due_date (default: updated)
- `--markdown-only` - Output only Markdown format

#### Examples

Fetch last 10 tasks:
```bash
python scripts/clickup_tasks.py --limit 10
```

Fetch tasks for a different user:
```bash
python scripts/clickup_tasks.py --assignee "john@example.com" --limit 3
```

Fetch tasks from a different workspace:
```bash
python scripts/clickup_tasks.py --workspace "My Team" --assignee "Karol"
```

Get only Markdown output (suitable for pasting into ClickUp):
```bash
python scripts/clickup_tasks.py --markdown-only
```

### Output

The tool provides two formats:
1. **Pretty console output** - Easy to read in the terminal with task details
2. **Markdown output** - Formatted for pasting into ClickUp comments/descriptions

Each task includes:
- Task title (with clickable link)
- Current status
- Location (Space / Folder / List)
- Last updated timestamp (in Europe/Warsaw timezone)

### Example Output

```
================================================================================
LAST 5 CLICKUP TASKS
================================================================================

1. Implement user authentication
   Status: In Progress
   Location: Development / Backend / API Tasks
   URL: https://app.clickup.com/t/abc123
   Last Updated: 2025-10-22 14:30 CEST

2. Fix navigation bug
   Status: To Do
   Location: Development / Frontend / Bug Fixes
   URL: https://app.clickup.com/t/def456
   Last Updated: 2025-10-21 16:45 CEST

...
================================================================================

--- MARKDOWN OUTPUT (for ClickUp) ---

# Last 5 Tasks

## 1. [Implement user authentication](https://app.clickup.com/t/abc123)
- **Status**: In Progress
- **Location**: Development / Backend / API Tasks
- **Last Updated**: 2025-10-22 14:30 CEST

## 2. [Fix navigation bug](https://app.clickup.com/t/def456)
- **Status**: To Do
- **Location**: Development / Frontend / Bug Fixes
- **Last Updated**: 2025-10-21 16:45 CEST

...
```
