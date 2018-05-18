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

            
def isprime(n):
    # This function returns after finding only one factor
    # Quicker than finding all factors
    for i in range(2, int(math.sqrt(n))+1):  # Start at 2 because we are ignoring the 1 & n pair
        quotient = n/float(i)
        if quotient == int(quotient):
            return False  # This number has a factor therefore is not prime
    # If we got to the squareroot and found no integer factors, then it is prime
    return True

def largestprimefactor(n):
    if type(n) is not int:
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
