#!/usr/bin/python3

from math import sqrt

from lib import isprime


def isint(n):
    if int(n) == n:
        return True
    else:
        return False


def goldbach(n, primes):
    # Primes is every prime number below n
    for prime in primes:
        if isint(sqrt((n - prime)/2)):
            return True
    return False


if __name__ == "__main__":
    primes = [2]
    disproven = False
    n = 3
    while disproven is False:
        if isprime(n):
            primes.append(n)
            n += 2  #  odd numbers only
            continue
        if goldbach(n, primes) is False:
            disproven = True
            print(n)
        n += 2
