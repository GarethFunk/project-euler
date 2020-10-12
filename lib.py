#!/usr/bin/python3
from math import sqrt

def evenly_divides(dividend, divisor):
    return dividend % divisor == 0

def factors(n):
    # Factors will range from 1 and n to sqrt(n) and sqrt(n) and are in pairs
    # Check range 1 to sqrt(n) to find all factor pairs
    factors = []
    for i in range(1, int(sqrt(n))+1):  # int() will round down, this is desired.
        # We want to include the squareroot value in the loop hence +1 in range statement
        # Check if it is a factor
        if evenly_divides(n, i):
            factors.append((int(i), int(n / i)))
    return factors

def isprime(n):
    # This function returns after finding only one factor
    # Quicker than finding all factors
    # Check two first because it doesn't fit the pattern
    if evenly_divides(n, 2):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        # Skipping even numbers
        if evenly_divides(n, i):
            return False
    # Handle corner cases
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        return True

if __name__ == "__main__":
    print(evenly_divides(8, 2))  # True
    print(evenly_divides(8, 3))  # False
    print(factors(60))
    for i in range(20):
        print(i, isprime(i))

