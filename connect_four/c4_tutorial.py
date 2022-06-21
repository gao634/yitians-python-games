import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    pass

def is_valid_location(board, col):
    if board[5][col] == 0:
        return True
    return False

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
def winning_move(board, piece):

board = create_board()
#print(board)
turn = 0
game_over = False
while not game_over:
    # Ask for p1 input
    if turn == 0:
        col = int(input("Player 1 (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
    else:
        col = int(input("Player 2 (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
    turn += 1
    turn = turn % 2
    print(board)
