from datetime import datetime, timedelta
import pandas as pd

# Function to get backlog items older than X days
def get_backlog_items_older_than_x_days(jira, board_id, days):
    # Calculate the date threshold
    threshold_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    # JQL Query
    jql = f'project = {board_id} AND status = "Backlog" AND created <= "{threshold_date}"'
    print(f"JQL: {jql}")  # Print the JQL for troubleshooting

    # Query for backlog items older than X days
    backlog_items = jira.search_issues(jql)
    
    if not backlog_items:
        print("No backlog items found")
        return []

    # Process the results
    backlog_data = []
    
    for issue in backlog_items:
        created_date = datetime.strptime(issue.fields.created.split('T')[0], '%Y-%m-%d')  # Extract the created date
        days_ago = (datetime.now() - created_date).days  # Calculate days ago
        
        backlog_data.append({
            'Issue Key': issue.key,
            'Summary': issue.fields.summary,
            'Created Date': created_date.strftime('%Y-%m-%d'),
            'Days Ago': days_ago
        })
    
    return backlog_data

# Function to save backlog items to Excel
def save_backlog_items_to_excel(backlog_data, excel_file='backlog_items.xlsx'):
    if not backlog_data:
        print("No data to save")
        return

    # Convert the backlog data to a pandas DataFrame
    df = pd.DataFrame(backlog_data)
    print(f"Data to be saved: \n{df}")  # Print the DataFrame for verification
    
    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)
    print(f"Backlog items have been saved to {excel_file}")
