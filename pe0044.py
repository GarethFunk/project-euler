#!/usr/bin/python3

"""
P(k) + P(j) = P(m)
P(k) - P(j)) = P(n)

k(3k-1) + j(3j-1) = m(3m-1)
k(3k-1) - j(3j-1) = n(3n-1)
Two equations in four variables - cannot be solved uniquely

n < m
k > j

minimise P(k) - P(j)
minimise P(n) = n(3n-1)
minimise n

n < j 
n < k

Therfore, the first pair of pentagon numbers we find whose sum and difference are 
also pentagon numbers will minimise the difference 
"""

from math import sqrt


def p(n):
    return int((n*((3*n) - 1))/2)


def ispentagon(p):
    # 3n^2 - n - 2p = 0
    # (1 ± sqrt(1 + 24*p))/6 = n
    # n > 0 so take +ve square root
    # 1 + sqrt(1 + 24p) = 6n
    if (1 + sqrt(1 + (24*p))) % 6 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    pentagons = [p(1)]
    n = 2
    current = p(n)
    solved = False
    while not solved:
        for pentagon in pentagons:
            difference = current - pentagon
            psum = current + pentagon
            if ispentagon(difference) and ispentagon(psum):
                print((difference, psum, current, pentagon))
                solved = True
        pentagons.append(current)
        n += 1
        current = p(n)
