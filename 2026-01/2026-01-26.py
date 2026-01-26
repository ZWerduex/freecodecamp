def fizz_buzz_mini(n):
    ret = ''
    if n % 3 == 0:
        ret += 'Fizz'
    if n % 5 == 0:
        ret += 'Buzz'
    return ret if ret != '' else str(n)