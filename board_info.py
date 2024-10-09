def get_jira_boards(jira):
    
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
