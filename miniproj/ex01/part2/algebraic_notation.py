pieces_can_block = ["R", "P", "Q", "B"]
pieces_lists = ["K", "R", "P", "Q", "B"]

def is_piece_check(board_matrix, piece_data, king_pos):
    piece_pos_r = piece_data["pos"]["row"]
    piece_pos_c = piece_data["pos"]["column"]
    piece_type = piece_data["type"]

    if piece_type == "P":
            # Pawn can check at up-left and up-right of it position
        if (((king_pos["column"] == piece_pos_c+1) or (king_pos["column"] == piece_pos_c-1)) and king_pos["row"] == piece_pos_r-1):
            return 1

    if piece_type == "R" or piece_type == "Q":
        # Rook (and Queen) can check in same column or row
        if king_pos["column"] == piece_pos_c or king_pos["row"] == piece_pos_r:
            # Check anything block it checking way?
            got_block = 0

            if king_pos["column"] == piece_pos_c:
                tem_r = piece_pos_r
                step_r = 1 if piece_pos_r < king_pos["row"] else -1

                while tem_r != king_pos["row"]:
                    tem_r = tem_r + step_r
                    if board_matrix[tem_r][piece_pos_c] in pieces_can_block:
                        got_block = 1
                        break
            else:
                tem_c = piece_pos_c
                step_c = 1 if piece_pos_c < king_pos["column"] else -1

                while tem_c != king_pos["column"]:
                    tem_c = tem_c + step_c
                    if board_matrix[piece_pos_r][tem_c] in pieces_can_block:
                        got_block = 1
                        break
            
            if not got_block:
                return 1

    if piece_type == "B" or piece_type == "Q":
        # Bishop (and Queen) can check at same Diagonal of it position. if diagonal two position 
        # If the positions are diagonals apart, when you subtract the two positions, columns and row will have the same value.
        if (abs(king_pos["column"] - piece_pos_c) == abs(king_pos["row"] - piece_pos_r)):
            # Check anything block it checking way?
            tem_c = piece_pos_c
            tem_r = piece_pos_r
            step_c = 1 if piece_pos_c < king_pos["column"] else -1
            step_r = 1 if piece_pos_r < king_pos["row"] else -1
            
            got_block = 0
            while tem_c != king_pos["column"]:
                tem_c = tem_c + step_c
                tem_r = tem_r + step_r
                if board_matrix[tem_r][tem_c] in pieces_can_block:
                    got_block = 1
                    break
            
            if not got_block:
                return 1

    return 0

def algebraic_notation(board_data):
    board_matrix = board_data["board"]
    board_size = board_data["board_size"]
    king_pos = board_data["king_pos"]

    if board_size > 26:
        print("The board must be equal or smaller than 26x26.")
        return
    
    for row in range(board_size):
        for column in range(board_size):
            if board_matrix[row][column] in pieces_lists:
                piece_data = {
                    "pos": {"row": row, "column": column}, "type": board_matrix[row][column]
                }

                is_check = is_piece_check(board_matrix, piece_data, king_pos)

                print(f"- {board_matrix[row][column]}{chr(ord('a')+column)}{board_size-row}{"+" if is_check else ''}")
