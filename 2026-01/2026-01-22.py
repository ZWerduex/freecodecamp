# hardcoded ranges version with loop
def get_average_grade(scores):
    moy = round(sum(scores) / len(scores))
    rgs = {
        (97, 100, "A+"), (93, 96, "A"), (90, 92, "A-"),
        (87, 89, "B+"), (83, 86, "B"), (80, 82, "B-"),
        (77, 79, "C+"), (73, 76, "C"), (70, 72, "C-"),
        (67, 69, "D+"), (63, 66, "D"), (60, 62, "D-")
    }
    for lb, ub, note in rgs:
        if lb <= moy <= ub: return note
    return "F"

# no loop version
def get_average_grade_2(scores):
    moy = round(sum(scores) / len(scores))
    if moy < 60: return "F"

    ten = moy // 10
    unit = moy - ten * 10
    basenote = {8: "B", 7: "C", 6: "D"}.get(ten, "A")
    modnote = "+" if unit >= 7 else "-" if unit <= 2 else ""
    
    return basenote + modnote