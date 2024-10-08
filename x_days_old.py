from datetime import datetime, timedelta

def get_backlog_items_older_than_x_days(jira, board_id, days):
    # Calculate the date threshold
    threshold_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    # Query for backlog items older than X days
    backlog_items = jira.search_issues(f'project = {board_id} AND status = "Backlog" AND created <= {threshold_date}')
    
    # Print the title and number of days ago each issue was created
    for issue in backlog_items:
        created_date = datetime.strptime(issue.fields.created.split('T')[0], '%Y-%m-%d')  # Extract the created date
        days_ago = (datetime.now() - created_date).days  # Calculate days ago
        print(f'{issue.key}: {issue.fields.summary} (Created {days_ago} days ago)')
