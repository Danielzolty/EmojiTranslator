import move_piece
import numpy as np
from termcolor import colored

RED_INT = 1
BLUE_INT = 2
ROW_COUNT = 6
COLUMN_COUNT = 7
RED_CHAR = colored('X', 'red')  # RED_CHAR = 'X'
BLUE_CHAR = colored('O', 'blue')  # BLUE_CHAR = 'O'

def create_board():
    """creat empty board for new game"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    return board

'''
Prints what the board looks like.
'''
def print_board(board):
    """print current board with all chips put in so far"""
    # print(np.flip(board, 0))
    print(" 0 1 2 3 4 5 6 \n" "|" + np.array2string(np.flip(np.flip(board, 1)))
          .replace("[", "").replace("]", "").replace(" ", "|").replace("0", "_")
          .replace("1", RED_CHAR).replace("2", BLUE_CHAR).replace("\n", "|\n") + "|")


def play_game():
    turn = 0

    board = create_board()
    game_over = False

    while not game_over:
        print_board(board)
        if turn % 2 == 0:
            col = int(input("RED please choose a column(0-6): "))
            while col > 6 or col < 0:
                col = int(input("Invalid column, pick a valid one: "))
            while not move_piece.is_valid_location(board, col - 1):
                col = int(input("Column is full. pick another one..."))
            # col -= 1
            # col = move_piece.best_move(board)

            row = move_piece.get_next_open_row(board, col)
            move_piece.drop_chip(board, row, col, RED_INT)

        if turn % 2 == 1 and not game_over:
            col = move_piece.best_move(board)

            row = move_piece.get_next_open_row(board, col)
            move_piece.drop_chip(board, row, col, BLUE_INT)
            # move_piece.MoveRandom(board,BLUE_INT)

        # print_board(board)
        
        if move_piece.game_is_won(board, RED_INT):
            game_over = True
            # print(colored("Red wins!", 'red'))
            return 1
        if move_piece.game_is_won(board, BLUE_INT):
            game_over = True
            # print(colored("Blue wins!", 'blue'))
            return 2
        if len(move_piece.get_valid_locations(board)) == 0:
            game_over = True
            # print(colored("Draw!", 'blue'))
            return 0
        turn += 1

play_game()
# wins = 0
# for i in range(100):
#     if play_game() == 1:
#         wins += 1
# print(f"Percentage of times player wins: {wins/100}")