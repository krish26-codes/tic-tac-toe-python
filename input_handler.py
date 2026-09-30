def get_position(board):
    try:
        position = int(input("Enter a position (1-9): "))
    except ValueError:
        print("Please enter a number!")
        return None

    if position < 1 or position > 9:
        print("Please enter a position between 1 and 9!")
        return None

    if board[position - 1] != " ":
        print("Position already taken!")
        return None

    return position - 1