import re

def to_consonant_case(s):
    vw = {'a', 'e', 'i', 'o', 'u'}
    acc = ''
    for c in s:
        # if vowel
        if c.lower() in vw:
            acc += c.lower()
        # if letter, which actually tests for consonants
        # as vowels has been tested for before
        elif re.match(r'[a-zA-Z]', c):
            acc += c.upper()
        elif c == '-':
            acc += '_'
        else:
            acc += c
    return acc