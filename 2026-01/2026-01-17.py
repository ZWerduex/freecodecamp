def knight_moves(position):
    def on_board(col, row):
        return 0 <= col <= 7 and 0 <= row <= 7

    col = ord(position[0]) - 65
    row = int(position[1]) - 1
    moves = 0
    for i in [-2, 2]:
        for j in [-1, 1]:
            if on_board(col + i, row + j):
                moves += 1
            if on_board(col + j, row + i):
                moves += 1
    return moves