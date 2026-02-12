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
                king_pos["column"] = column
                king_pos["row"] = row
    if king_count == 1:
        return king_pos
    elif king_count > 1:
        print("There can only be one king.")
        return 0
    elif king_count == 0:
        print("There must be at least one king.")
        return 0


pieces_can_block = ["R", "P", "Q", "B"]

def is_check(board_matrix, board_size, king_pos):
    for row in range(board_size):
        for column in range(board_size):
            if board_matrix[row][column] == "P":
                 # Pawn can check at up-left and up-right of it position
                if (((king_pos["column"] == column+1) or (king_pos["column"] == column-1)) and king_pos["row"] == row-1):
                    return

            if board_matrix[row][column] == "R" or board_matrix[row][column] == "Q":
                # Rook (and Queen) can check in same column or row
                if king_pos["column"] == column or king_pos["row"] == row:
                    # Check anything block it checking way?
                    got_block = 0

                    if king_pos["column"] == column:
                        tem_r = row
                        step_r = 1 if row < king_pos["row"] else -1

                        while tem_r != king_pos["row"]:
                            tem_r = tem_r + step_r
                            if board_matrix[tem_r][column] in pieces_can_block:
                                got_block = 1
                                break
                    else:
                        tem_c = column
                        step_c = 1 if column < king_pos["column"] else -1

                        while tem_c != king_pos["column"]:
                            tem_c = tem_c + step_c
                            if board_matrix[row][tem_c] in pieces_can_block:
                                got_block = 1
                                break
                    
                    if not got_block:
                        return

            if board_matrix[row][column] == "B" or board_matrix[row][column] == "Q":
                # Bishop (and Queen) can check at same Diagonal of it position. if diagonal two position 
                # If the positions are diagonals apart, when you subtract the two positions, columns and row will have the same value.
                if (abs(king_pos["column"] - column) == abs(king_pos["row"] - row)):
                    # Check anything block it checking way?
                    tem_c = column
                    tem_r = row
                    step_c = 1 if column < king_pos["column"] else -1
                    step_r = 1 if row < king_pos["row"] else -1
                    
                    got_block = 0
                    while tem_c != king_pos["column"]:
                        tem_c = tem_c + step_c
                        tem_r = tem_r + step_r
                        if board_matrix[tem_r][tem_c] in pieces_can_block:
                            got_block = 1
                            break
                    
                    if not got_block:
                        return


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
    return {
        "board": board_matrix,
        "board_size": board_size,
        "king_pos": king_pos
    }
    #print(board_matrix)