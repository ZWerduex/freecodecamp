def golf_score(par, strokes):
    if strokes == 1: return "Hole in one!"
    try:
        return {
            par - 2: "Eagle",
            par - 1: "Birdie",
            par: "Par",
            par + 1: "Bogey"
        }[strokes]
    except KeyError:
        return "Double bogey"