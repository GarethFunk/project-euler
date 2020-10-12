#!/usr/bin/python3

from lib import factors

i = 1  # Index of triangle number
n = 1  # The ith triangle number
while len(factors(n))*2 < 500:
    i += 1
    n += i

print(n)
