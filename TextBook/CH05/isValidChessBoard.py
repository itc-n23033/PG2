def is_valid_chess_board(board):
    valid_positions = {f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"}
    
    valid_pieces = {'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking',
                    'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking'}
    
    max_counts = {
        'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1,
        'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1
    }
    
    piece_counts = {piece: 0 for piece in valid_pieces}
    
    for position, piece in board.items():
        if position not in valid_positions:
            return False
        if piece not in valid_pieces:
            return False
        piece_counts[piece] += 1
    
    for piece, count in piece_counts.items():
        if count > max_counts[piece]:
            return False
    
    return True

chess_board = {'1n': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(is_valid_chess_board(chess_board))  # False
