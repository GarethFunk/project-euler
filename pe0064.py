#!/usr/bin/python3

from math import floor, sqrt
from pe0047 import primefactors

# a0 = floor(sqrt(n))
# -> sqrt(n) = a0 + sqrt(n) - a0
# ->   (cN*sqrt(n) - bN) / dN is the generic term
# Forumlae for the next generic coeffiecients are: (from some algebra)
# aN+1 = floor(dN(CN*sqrt(n) + bN)/(cN^2 * n - bN^2))
# cN+1 = dN*cN
# bN+1 = - dN*bN + (aN+1(cN^2 * n - bN^2))
# dN+1 = cN^2 * n - bN^2

class ContinuedFractionSquareRoot:
    def __init__(self, n):
        self.n = n
        self.rootn = sqrt(n)
        self.a = floor(self.rootn)
        self.b = self.a
        self.c = 1
        self.d = 1
        self.iteration = 0
        self.looped = False
    def __iter__(self):
        return self

    def __next__(self):
        if self.looped is True:
            raise StopIteration
        a = self.a
        next_a = self.__nextA()
        next_b = self.__nextB()
        next_c = self.__nextC()
        next_d = self.__nextD()
        self.a = next_a
        self.b = next_b
        self.c = next_c
        self.d = next_d
        self.__cancelFraction()
        self.iteration += 1
        if self.iteration == 1:
            # Save the internal variables here so we can check if we loop back to the same condiiton
            self.bd_quotient_loop_start = self.b/self.d
            self.cd_quotient_loop_start = self.c/self.d
        if self.iteration > 1:
            if self.bd_quotient_loop_start == self.b/self.d and \
                self.cd_quotient_loop_start == self.c/self.d:
                self.looped = True
        return a

    def __nextA(self):
        return floor((self.d*((self.c * self.rootn) + self.b))/self.__nextD())

    def __nextB(self):
        return (self.__nextA() * self.__nextD()) - (self.d * self.b)
    
    def __nextC(self):
        return self.d * self.c

    def __nextD(self):
        return ((self.c**2) * self.n) - self.b**2

    def __cancelFraction(self):
        # Check common factors and cancel.
        b_factors = primeFactors(self.b)
        c_factors = primeFactors(self.c)
        d_factors = primeFactors(self.d)
        common_prime_factors = set(b_factors.keys()).intersection(set(c_factors.keys())).intersection(set(d_factors.keys()))
        for common_prime_factor in common_prime_factors:
            # Find the most times the common factor is shared
            highest_common_index = min(b_factors[common_prime_factor], c_factors[common_prime_factor], d_factors[common_prime_factor])
            common_factor = common_prime_factor ** highest_common_index
            self.b = int(self.b / common_factor)
            self.c = int(self.c / common_factor)
            self.d = int(self.d / common_factor)
        return

if __name__ == "__main__":
    max_num = 10000
    periods = []
    irrational_roots = [x for x in range(max_num + 1) if int(sqrt(x)) * int(sqrt (x)) != x]
    for number in irrational_roots:
        cfsr = ContinuedFractionSquareRoot(number)
        aN = []
        for a in cfsr:
            aN.append(a)
        period = len(aN) -1 
        print(str(number) + " has period " + str(period))
        #print(aN)
        periods += [period]
    
    print(len([x for x in periods if x % 2 == 1]))
        

        