def fetch_sprints_from_board(jira, board_id):
    """
    Fetches sprints from a specified Jira board.

    Parameters:
    - jira: JIRA instance for API interaction.
    - board_id (int): The ID of the Jira board.

    Returns:
    - List of sprints with their ID, name, and state.
    """
    # Fetch sprints from the specified board
    sprints = jira.sprints(board_id)

    # Extract and print sprints details
    sprint_details = []
    for sprint in sprints:
        sprint_id = sprint.id
        sprint_name = sprint.name
        sprint_state = sprint.state
        
        # Append sprint details to the list
        sprint_details.append({
            'id': sprint_id,
            'name': sprint_name,
            'state': sprint_state
        })
        
        # Print the sprint details
        print(f"Sprint ID: {sprint_id}, Name: {sprint_name}, State: {sprint_state}")

    return sprint_details
