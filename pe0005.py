def isevenlydivisible(n, maxdivisor):
    for i in range(1, maxdivisor+1):    # +1 to include final value
        if n%i != 0:
            return False
    # Getting to this point means it worked
    return True

# We know we can start at at least 2520
n = 2520
# We know it must have all the prime factors of primes between 10 and 20
n = n*11*13*17*19 #116396280 
# This isn't evenly divisble by 20
# numbers we missed out were 12, 14, 15, 16, 18 & 20
# prime factors of these are 2, 2, 2, 2, 3, 3, 5, 7 and all these need to be prime factors of this new number
# Only need one extra 2 here because all the other prime factors are
# also prime factors of 2520 (cos evenly divisble by 1-10)
n = n*2
print(n)
print(isevenlydivisible(n, 20))
