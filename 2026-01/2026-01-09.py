def is_prime(n):
    if n <= 1:
        return False
    # iterate over all integers from n to n/2
    # every divisor < n/2 gives another divisor > n/2
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    rotations = set()
    nstr = str(n)
    # compute set of rotations
    for shift in range(len(nstr)):
        rotations.add(int(nstr[shift:] + nstr[:shift]))
    return all(is_prime(r) for r in rotations)