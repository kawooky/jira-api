def get_active_sprint_issues(jira, sprint_id, project_key):
    try:
        issues_in_sprint = jira.search_issues(f'sprint = {sprint_id} AND project = {project_key} AND status != "Closed"')
        
        if issues_in_sprint:
            print(f"Issues in Sprint ID {sprint_id} for Project '{project_key}':")
            for issue in issues_in_sprint:
                print(f'  - {issue.key}: {issue.fields.summary}')
    except Exception as e:
        print(f"An error occurred while fetching issues: {str(e)}")