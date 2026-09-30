print("Welcome to the Tic Tac Toe game")
board=[" "," "," "," "," "," "," "," "," "]
player="X"
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")
while True:
    print("Player", player, "turn")
    try:
      position = int(input("Enter a position (1-9): "))
    except ValueError:
      print("Please enter a number!")
      continue
    if position < 1 or position > 9:
        print("Please enter a position between 1 and 9!")
        continue
    if board[position - 1] == " ":
       board[position - 1] = player
    else:
       print("Position already taken!")
       continue
    
    if board[0] == board[1] == board[2] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break
    if board[3] == board[4] == board[5] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break

    if board[6] == board[7] == board[8] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break

    if board[0] == board[3] == board[6] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break

    if board[1] == board[4] == board[7] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break

    if board[2] == board[5] == board[8] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break
    if board[0] == board[4] == board[8] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break

    if board[2] == board[4] == board[6] != " ":
       print(board[0], "|", board[1], "|", board[2])
       print("--+---+--")
       print(board[3], "|", board[4], "|", board[5])
       print("--+---+--")
       print(board[6], "|", board[7], "|", board[8])
       print("Player", player, "wins!")
       break
    if " " not in board:
       print("It's a draw!")
       break

    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    if player == "X":
        player = "O"
    else:
        player = "X"