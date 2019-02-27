# -*- coding: utf-8 -*-
import math

def factors(n):
    # Factors will range from 1 and n to sqrt(n) and sqrt(n) and are in pairs
    # Check range 1 to sqrt(n) to find all factor pairs
    factors = []
    for i in range(1, int(math.sqrt(n))+1):  # int() will round down, this is desired.
        # We want to include the squareroot value in the loop hence +1 in range statement
        # Check if it is a factor
        quotient = n/float(i)
        if quotient == int(quotient):
            # The quotient is an integer therefore i is a factor
            factors.append((int(i), int(quotient)))
    return factors

# This iterator is for greatly reducing the number of divisors we check
# when looking if a number is prime.
# We do this by making the following deductions on a group of potential divisors
# for a candidate prime number:
# 7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
# ^            ^     ^           ^     ^           ^     ^           ^     ^           ^     ^    
# Starting at 7 we have jumps of [4, 2] repeating which give us a sequence of numbers 
# Which never have a prime factor of 3 or 2
# To skip over factors of 5 is possible but would require more logic. 
# The extra logic in the iterator might outweigh the saving
class pseudoprimeiterator():
    def __init__(self, end):
        self.end = end
        self.current = 5
        self.step = (4, 2)
        self.tictoc = True

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step[self.tictoc]
        self.tictoc = not self.tictoc
        if self.current < self.end:
            return self.current
        else:
            raise StopIteration
    
    def next(self):
        return self.__next__()

            
def isprime(n):
    # This function returns after finding only one factor
    # Quicker than finding all factors
    # Check two first because it doesn't fit the pattern
    quotient = n/float(2)
    if quotient == int(quotient):
        if n != 2:
            return False  # This number is divisble by 2
        else:
            return True
    for i in range(3, int(math.sqrt(n))+1, 2):
        quotient = n/float(i)
        if quotient == int(quotient):
            return False  # This number has a factor therefore is not prime
    # If we got to the squareroot and found no integer factors, then it is prime
    if n == 1:
        return False
    else:
        return True

def largestprimefactor(n):
    if type(n) is not int and type(n) is not long:
        raise TypeError
    allfactors = factors(n)
    # Now we have a list of factor pairs (non-prime)
    # Let's find which of these are prime numbers
    pfactors = []
    for factorpair in allfactors:
        if isprime(factorpair[0]):
            pfactors.append(factorpair[0])
        if isprime(factorpair[1]):
            pfactors.append(factorpair[1])
    # print(pfactors)
    return max(pfactors)

if __name__ == "__main__":
    print(largestprimefactor(600851475143))
