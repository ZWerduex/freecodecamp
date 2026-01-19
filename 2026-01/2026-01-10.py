def tic_tac_toe(board):
    flipped = [list() for _ in board]
    for row in board:
        # check rows
        if all(c == row[0] for c in row[1:]):
            return row[0] + " wins"
        # build cols
        for i, c in enumerate(row):
            flipped[i].append(c)
    for col in flipped:
        # check cols
        if all(c == col[0] for c in col[1:]):
            return col[0] + " wins"
    # build diags
    diag1, diag2 = [], []
    for i in range(len(board)):
        diag1.append(board[i][i])
        diag2.append(board[i][len(board) - i - 1])
    # check diags
    if all(c == diag1[0] for c in diag1[1:]):
        return diag1[0] + " wins"
    if all(c == diag2[0] for c in diag2[1:]):
        return diag2[0] + " wins"
    return "Draw"