def is_valid_hex(s):
    chrs = set('0123456789abcdefABCDEF')
    return s.startswith('#') and len(set(s[1:]) - chrs) == 0 and (len(s) == 4 or len(s) == 7)