

def get_jira_boards(jira):
    """
    Retrieves and prints the details of boards including project name and key from a Jira instance.

    Args:
    - server (str): Jira server URL.
    - username (str): Jira account email or username.
    - api_token (str): Jira API token.

    """


    # Get all board
    boards = jira.boards()

    # Extract and print the board details including projectName
    for board in boards:
        board_id = board.id
        project_name = board.location.projectName
        project_key = board.location.projectKey
        board_name = board.name
        board_type = board.type
        print(f"Board ID: {board_id}, Project Name: {project_name}, Project Key: {project_key}, Name: {board_name}, Type: {board_type}")
