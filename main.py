from board import display_board, show_positions
from game_logic import check_winner, check_draw
from input_handler import get_position
from player import switch_player


print("Welcome to the Tic Tac Toe game")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"

show_positions()

while True:
    print("Player", player, "turn")

    position = get_position(board)

    if position is None:
        continue

    board[position] = player

    display_board(board)

    winner = check_winner(board)

    if winner is not None:
        print("Player", winner, "wins!")
        break

    if check_draw(board):
        print("It's a draw!")
        break
  
    player = switch_player(player)