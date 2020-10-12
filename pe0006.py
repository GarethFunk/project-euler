#!/usr/bin/python3

def sumsquare(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s


def squaresum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    s = s*s
    return s


print(squaresum(100)-sumsquare(100))
