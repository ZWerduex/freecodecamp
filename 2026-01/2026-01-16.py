import math

def is_integer_hypotenuse(a, b):
    hyp = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return hyp.is_integer()