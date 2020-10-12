#!/usr/bin/python3

from lib import factors


def d(n):
    # Sum of proper divisors of n
    s = 0
    pairs = factors(n)
    for pair in pairs:
        if pair[0] == pair[1]:
            # count divisors only once
            s += pair[0]
        elif pair[0] == 1:
            # Don't add n
            s += pair[0]
        else:
            s += pair[0]
            s += pair[1]
    return s


if __name__ == "__main__":
    amicables = {}
    for a in range(1, 10000):
        if a not in amicables:
            b = d(a)
            if b != a and d(b) == a:
                # These numbers are amicable
                amicables.update({a: a, b: b})
    print(sum(amicables.values()))
