import re

def separate_letters_and_numbers(s):
    # letter to number
    s = re.sub(r'([a-zA-Z]+)([0-9]+)', r'\1-\2', s)
    # number to letter
    s = re.sub(r'([0-9]+)([a-zA-Z]+)', r'\1-\2', s)
    return s