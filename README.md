# Jira Automation Script

This Python project integrates with Jira's API to automate several tasks such as retrieving board information, fetching sprint details, getting backlog items older than a specified number of days, and more.

## Requirements

- Python 3.7 or higher

Install the required libraries from reuirements.txt using `pip`:

```bash
pip install -r requirements.txt
```

## Setup

1. Jira API Authentication:
   - You'll need your Jira API token, which you can generate from your Jira account settings under "API tokens."
   - Replace the following placeholders in the script with your actual Jira credentials:
   ```bash
   JIRA_SERVER = 'https://your-jira-instance.atlassian.net'
   JIRA_USERNAME = 'your-email@example.com'
   JIRA_API_TOKEN = 'your-jira-api-token'
   ```
2. Jira Board and Sprint Details:
   - Set the board_id and sprint_id according to your Jira project details. These can be retrieved using the get_jira_boards and fetch_sprints_from_board functions.
   ```bash
   board_id = 21  # Change this to your board's ID
   sprint_id = 32  # Change this to your sprint's ID
   project_key = "XSP"  # Change this to your Jira project key
   ```

## Functions

1. get_jira_boards(jira) - Fetches and displays all boards associated with the Jira account.

2. fetch_sprints_from_board(jira, board_id) - Retrieves all sprints from a specific board.

3. get_active_sprint_issues(jira, sprint_id, project_key) - Fetches all issues in an active sprint for a given project.

4. get_unassigned_issues_in_sprint(jira, sprint_id, project_key) - Retrieves all unassigned issues in a specific sprint.

5. get_backlog_items_older_than_x_days(jira, project_key, days) - Gets all backlog items in a project that have been inactive for a specified number of days.

## How to Use

1. Clone the repository or copy the code to your local environment.
2. Install the dependencies as specified above.
3. Update the script with your Jira server URL, username, API token, and project details.
4. Use the example functions provided to fetch boards, sprints, and issues from Jira.
