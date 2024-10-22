from jira import JIRA
from x_days_old import get_backlog_items_older_than_x_days  # Change to absolute import
from board_info import get_jira_boards
from get_active_sprit_issues import get_active_sprint_issues
from get_unassigned_issues_in_sprint import get_unassigned_issues_in_sprint
from sprints_info import fetch_sprints_from_board
from x_days_old import save_backlog_items_to_excel
import pandas as pd

# Constants
JIRA_SERVER = 'https://corecomtechacademy.atlassian.net'
JIRA_USERNAME = 'youssef@corecomtechacademy.co.uk'
JIRA_API_TOKEN = "YOUR API TOKEN"

# Authenticate with your Jira instance
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

board_id = 21
sprint_id = 32
project_key = "XSP"



# Example usage
get_jira_boards(jira)

#Example usage
# fetch_sprints_from_board(jira, board_id)

# Example usage
# get_active_sprint_issues(jira, sprint_id, project_key)


# Example usage
# get_unassigned_issues_in_sprint(jira, sprint_id, project_key)


# # Call the function with jira instance
backlog_items = get_backlog_items_older_than_x_days(jira, "TT", days=21)
save_backlog_items_to_excel(backlog_items)