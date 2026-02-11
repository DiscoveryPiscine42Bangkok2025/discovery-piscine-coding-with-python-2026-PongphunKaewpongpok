valid_character = {"K", "R", "P", "Q", "B"}

def get_board_matrix(board):
    board_matrix = [[]]
    row = 0
    for i in range(len(board)):
        if not board[i].isspace():                      # Add character to board_matrix if it available in chess
            board_matrix[row].append(board[i])
        elif len(board_matrix[row]) > 0:                # Add new row when found whitespace (row must have at least 1 element)
            row = row + 1
            board_matrix.append([])
    
    return board_matrix

def get_board_size(board_matrix):
    board_size = len(board_matrix)
    for i in range(len(board_matrix)):
        if board_size != len(board_matrix[i]):          # If Size Y Board != Size X Board (must be square size_x=size_y)
            print("A chessboard is not a square.")
            return 0
    return board_size

def get_and_check_king(board_matrix, board_size):
    king_count = 0
    row = 0
    column = 0
    king_pos = {}

    for row in range(board_size):
        for column in range(board_size):
            if board_matrix[row][column] == "K":
                king_count = king_count + 1
                king_pos["x"] = column
                king_pos["y"] = row
    if king_count == 1:
        return king_pos
    else:
        print("There can only be one king.")
        return 0

def is_check(board_matrix, board_size, king_pos):
    for row in range(board_size):
        for column in range(board_size):
            if board_matrix[row][column] not in valid_character:

    print("Success")


def checkmate(board):
    board_matrix = get_board_matrix(board)              # Get board_matrix for calculation
    if not board_matrix:
        return
    
    board_size = get_board_size(board_matrix)           # Get board_size
    if not board_size:
        return

    king_pos = get_and_check_king(board_matrix, board_size)    # Get king_pos and check king count
    if not king_pos:
        return
    
    is_check(board_matrix, board_size, king_pos)
    
    print(board_matrix)