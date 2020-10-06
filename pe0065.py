#!/usr/bin/python3

# First need to generate continued fraction coefficients for e
# Then need to evaluate the fraction into numerator and denominator
# as a cancelled fraction

from copy import copy
from math import floor
from pe0047 import primefactors

class ContinuedFractionApproximation:
    def __init__(self, x, terms=10):
        self.value = x
        self.terms = terms
    def __iter__(self):
        self.coefficients = []
        self.convergents = []
        return self

    def __next__(self):
        if len(self.coefficients) == 0:
            self.coefficients.append(floor(self.value))
            self.convergents.append((self.coefficients[0], 1))
        elif len(self.coefficients) >= self.terms:
            raise StopIteration
        else:
            self.coefficients.append(1)  # Start with 1
            even = (len(self.coefficients) % 2) != 0  # zero index
            numerator, denominator = self.evaluate(self.coefficients)
            old_error = 1  # error can never be larger than 1
            error = abs(self.value - (numerator/denominator))
            while error < old_error:
                old_error = error
                self.coefficients[-1] += 1
                numerator, denominator = self.evaluate(self.coefficients)
                approximation = (numerator/denominator)
                if even is True and approximation > self.value:
                    continue
                elif even is False and approximation < self.value:
                    continue
                else:
                    error = abs(self.value - approximation)
            # Error just got bigger so back off one
            self.coefficients[-1] -= 1
        return self.coefficients[-1]

    def evaluate(self, coefficients):
        coefficients = copy(coefficients)
        # generic action here is to transform a + (b/c) into (ca * b)/c
        b = 1
        c = coefficients.pop()
        a = coefficients.pop()
        while(len(coefficients) > 0):
            new_a = coefficients.pop()
            new_b = c
            new_c = (c * a) + b
            a = new_a
            b, c = new_b, new_c
        numerator = (c * a) + b
        denominator = c
        return numerator, denominator

    def cancelFraction(self, numerator, denominator):
        # Check common factors and cancel.
        numerator_factors = primefactors(numerator)
        denominator_factors = primefactors(denominator)
        common_prime_factors = set(numerator_factors.keys()).intersection(set(denominator_factors.keys()))
        for common_prime_factor in common_prime_factors:
            # Find the most times the common factor is shared
            highest_common_index = min(numerator_factors[common_prime_factor], denominator_factors[common_prime_factor])
            common_factor = common_prime_factor ** highest_common_index
            numerator = int(numerator / common_factor)
            denominator = int(denominator / common_factor)
        print("done")
        return numerator, denominator


if __name__ == "__main__":
    from math import e, sqrt
    cf = ContinuedFractionApproximation(e, 100)
    for term in cf:
        print(term)
    numerator, denominator = cf.evaluate(cf.coefficients)
    print(numerator, denominator)
    print(sum([int(x) for x in str(numerator)]))