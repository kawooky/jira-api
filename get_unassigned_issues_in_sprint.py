def get_unassigned_issues_in_sprint(jira, sprint_id, project_key):
    unassigned_issues = jira.search_issues(f'sprint = {sprint_id} AND project = {project_key} AND assignee IS EMPTY')
    
    print(f'Number of unassigned issues: {len(unassigned_issues)}')
    return unassigned_issues