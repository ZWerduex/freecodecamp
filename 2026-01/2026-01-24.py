def get_bingo_letter(n):
    ranges = [
        (1, 15, "B"), (16, 30, "I"), (31, 45, "N"),
        (46, 60, "G"), (61, 75, "O")
    ]
    for lb, ub, letter in ranges:
        if lb <= n <= ub: return letter
    raise ValueError("Parameter n is not in any range")