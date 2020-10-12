#!/usr/bin/python3

from math import sqrt
from pe0064 import ContinuedFractionSquareRoot

# x2 – Dy2 = 1
# X = x2; Y = y2


class ContinuedFractionSquareRootEndless():
    def __init__(self, n):
        cfsr = ContinuedFractionSquareRoot(n)
        self.aN = []
        for a in cfsr:
            self.aN.append(a)

        self.repeating_length = len(self.aN) - 1

    def __iter__(self):
        self.call_count = 0
        return self

    def __next__(self):
        index = self.call_count % self.repeating_length
        a = None
        if index == 0:
            if self.call_count == 0:
                a = self.aN[0]
            else:
                a = self.aN[-1]
        else:
            a = self.aN[index]
        self.call_count += 1
        return a


class ContinuedFractionSquareRootConvergents():
    def __init__(self, n):
        self.a = ContinuedFractionSquareRootEndless(n)

    def __iter__(self):
        self.h = [0, 1]
        self.k = [1, 0]
        self.n = 2  # actually 0 but we need -1 and -2 for the startup
        self.a.__iter__()
        return self

    def __next__(self):
        an = self.a.__next__()
        hn = (an * self.h[self.n-1]) + self.h[self.n-2]
        kn = (an * self.k[self.n-1]) + self.k[self.n-2]
        self.h.append(hn)
        self.k.append(kn)
        self.n += 1
        return hn, kn


def DiophantineQuadraticSolver(D):
    if int(sqrt(D))**2 == D:
        return 0, 0
    # https://mathworld.wolfram.com/PellEquation.html
    cfsr = ContinuedFractionSquareRootConvergents(D)
    for pN, qN in cfsr:
        if (pN ** 2) - (D * (qN ** 2)) == 1:
            return pN, qN


if __name__ == "__main__":
    biggest_x = 0
    corresponding_D = 0
    for D in range(1, 1001):
        x, y = DiophantineQuadraticSolver(D)
        #print(D, x, y)
        if x > biggest_x:
            biggest_x = x
            corresponding_D = D

print(corresponding_D)
