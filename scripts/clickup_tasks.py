#!/usr/bin/env python3
"""
ClickUp Tasks Fetcher
Fetches the most recently updated tasks for a user from ClickUp API.
"""

import os
import sys
import json
import argparse
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import pytz


def fetch_clickup_api(endpoint, token, params=None):
    """Make a request to the ClickUp API."""
    base_url = "https://api.clickup.com/api/v2"
    url = f"{base_url}/{endpoint}"
    
    if params:
        param_str = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{url}?{param_str}"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    request = Request(url, headers=headers)
    
    try:
        with urlopen(request) as response:
            return json.loads(response.read().decode())
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}", file=sys.stderr)
        print(f"Response: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def get_workspace_id(token, workspace_name):
    """Get workspace (team) ID by name."""
    data = fetch_clickup_api("team", token)
    teams = data.get("teams", [])
    
    for team in teams:
        if team.get("name", "").lower() == workspace_name.lower():
            return team["id"]
    
    print(f"Workspace '{workspace_name}' not found.", file=sys.stderr)
    print(f"Available workspaces: {', '.join([t['name'] for t in teams])}", file=sys.stderr)
    sys.exit(1)


def get_user_id(token, team_id, user_identifier):
    """Get user ID by name or return if already an ID."""
    # If it's already a numeric ID, return it
    if user_identifier.isdigit():
        return user_identifier
    
    # Otherwise, search by name/email
    data = fetch_clickup_api(f"team/{team_id}", token)
    members = data.get("team", {}).get("members", [])
    
    for member in members:
        user = member.get("user", {})
        username = user.get("username", "").lower()
        email = user.get("email", "").lower()
        
        if (user_identifier.lower() in username or 
            user_identifier.lower() in email):
            return str(user["id"])
    
    print(f"User '{user_identifier}' not found in workspace.", file=sys.stderr)
    sys.exit(1)


def fetch_tasks(token, team_id, assignee_ids, limit=5, order_by="updated"):
    """Fetch tasks for a user from all spaces in the workspace."""
    all_tasks = []
    
    # Get all spaces in the workspace
    spaces_data = fetch_clickup_api(f"team/{team_id}/space", token, {"archived": "false"})
    spaces = spaces_data.get("spaces", [])
    
    for space in spaces:
        space_id = space["id"]
        
        # Get all folders in the space
        folders_data = fetch_clickup_api(f"space/{space_id}/folder", token, {"archived": "false"})
        folders = folders_data.get("folders", [])
        
        # Get folderless lists
        lists_data = fetch_clickup_api(f"space/{space_id}/list", token, {"archived": "false"})
        lists = lists_data.get("lists", [])
        
        # Fetch tasks from folderless lists
        for lst in lists:
            list_id = lst["id"]
            params = {
                "archived": "false",
                "assignees[]": ",".join(assignee_ids),
                "order_by": order_by,
                "reverse": "true",
                "include_closed": "true"
            }
            
            try:
                tasks_data = fetch_clickup_api(f"list/{list_id}/task", token, params)
                tasks = tasks_data.get("tasks", [])
                
                for task in tasks:
                    task["_space"] = space.get("name", "Unknown")
                    task["_folder"] = None
                    task["_list"] = lst.get("name", "Unknown")
                    all_tasks.append(task)
            except:
                # Skip lists that fail
                pass
        
        # Fetch tasks from folders and their lists
        for folder in folders:
            folder_lists = folder.get("lists", [])
            
            for lst in folder_lists:
                list_id = lst["id"]
                params = {
                    "archived": "false",
                    "assignees[]": ",".join(assignee_ids),
                    "order_by": order_by,
                    "reverse": "true",
                    "include_closed": "true"
                }
                
                try:
                    tasks_data = fetch_clickup_api(f"list/{list_id}/task", token, params)
                    tasks = tasks_data.get("tasks", [])
                    
                    for task in tasks:
                        task["_space"] = space.get("name", "Unknown")
                        task["_folder"] = folder.get("name", "Unknown")
                        task["_list"] = lst.get("name", "Unknown")
                        all_tasks.append(task)
                except:
                    # Skip lists that fail
                    pass
    
    # Sort all tasks by date_updated (most recent first)
    all_tasks.sort(key=lambda t: int(t.get("date_updated", 0)), reverse=True)
    
    return all_tasks[:limit]


def format_timestamp(timestamp_ms, timezone_str="Europe/Warsaw"):
    """Format timestamp to human-readable date in specified timezone."""
    if not timestamp_ms:
        return "N/A"
    
    tz = pytz.timezone(timezone_str)
    dt = datetime.fromtimestamp(int(timestamp_ms) / 1000, tz=pytz.UTC)
    dt_local = dt.astimezone(tz)
    return dt_local.strftime("%Y-%m-%d %H:%M %Z")


def generate_markdown(tasks):
    """Generate Markdown output for ClickUp."""
    lines = ["# Last 5 Tasks\n"]
    
    if not tasks:
        lines.append("No tasks found.\n")
        return "\n".join(lines)
    
    for i, task in enumerate(tasks, 1):
        title = task.get("name", "Untitled")
        status = task.get("status", {}).get("status", "Unknown")
        task_url = task.get("url", "#")
        list_name = task.get("_list", "Unknown")
        folder_name = task.get("_folder")
        space_name = task.get("_space", "Unknown")
        date_updated = format_timestamp(task.get("date_updated"))
        
        location = f"{space_name}"
        if folder_name:
            location += f" / {folder_name}"
        location += f" / {list_name}"
        
        lines.append(f"## {i}. [{title}]({task_url})")
        lines.append(f"- **Status**: {status}")
        lines.append(f"- **Location**: {location}")
        lines.append(f"- **Last Updated**: {date_updated}\n")
    
    return "\n".join(lines)


def print_console_output(tasks):
    """Print pretty console output."""
    print("\n" + "="*80)
    print("LAST 5 CLICKUP TASKS")
    print("="*80 + "\n")
    
    if not tasks:
        print("No tasks found.\n")
        return
    
    for i, task in enumerate(tasks, 1):
        title = task.get("name", "Untitled")
        status = task.get("status", {}).get("status", "Unknown")
        task_url = task.get("url", "#")
        list_name = task.get("_list", "Unknown")
        folder_name = task.get("_folder")
        space_name = task.get("_space", "Unknown")
        date_updated = format_timestamp(task.get("date_updated"))
        
        location = f"{space_name}"
        if folder_name:
            location += f" / {folder_name}"
        location += f" / {list_name}"
        
        print(f"{i}. {title}")
        print(f"   Status: {status}")
        print(f"   Location: {location}")
        print(f"   URL: {task_url}")
        print(f"   Last Updated: {date_updated}")
        print()
    
    print("="*80 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch the last N tasks for a user from ClickUp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --limit 10
  %(prog)s --assignee "john@example.com" --limit 3
  %(prog)s --workspace "My Team" --assignee "307142"

Environment Variables:
  CLICKUP_TOKEN    Your ClickUp API token (required)
        """
    )
    
    parser.add_argument(
        "--workspace",
        default="Karol",
        help="Workspace (team) name (default: Karol)"
    )
    
    parser.add_argument(
        "--assignee",
        default="307142",
        help="Assignee user ID, name, or email (default: 307142)"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of tasks to fetch (default: 5)"
    )
    
    parser.add_argument(
        "--order",
        default="updated",
        choices=["updated", "created", "due_date"],
        help="Order by field (default: updated)"
    )
    
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Output only Markdown (no console formatting)"
    )
    
    args = parser.parse_args()
    
    # Get API token from environment
    token = os.getenv("CLICKUP_TOKEN")
    if not token:
        print("Error: CLICKUP_TOKEN environment variable not set.", file=sys.stderr)
        print("Please set it with: export CLICKUP_TOKEN='your_token_here'", file=sys.stderr)
        sys.exit(1)
    
    # Get workspace ID
    team_id = get_workspace_id(token, args.workspace)
    
    # Get user ID
    user_id = get_user_id(token, team_id, args.assignee)
    
    # Fetch tasks
    tasks = fetch_tasks(token, team_id, [user_id], args.limit, args.order)
    
    # Output results
    if args.markdown_only:
        print(generate_markdown(tasks))
    else:
        print_console_output(tasks)
        print("\n--- MARKDOWN OUTPUT (for ClickUp) ---\n")
        print(generate_markdown(tasks))


if __name__ == "__main__":
    main()
