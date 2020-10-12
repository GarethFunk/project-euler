# Getting all primes with < 10 digits takes way too much time
# Get all pandigital numbers < 10 digits then check for primeness
# Certainly quicker to generate pandigital numbers than to iterate and find them

from itertools import permutations

from pe0003 import isprime

digits = "123456789"
if __name__ == "__main__":
    primepandigitals = []
    for n in range(2, 10):
        for pandigital in permutations(digits[:n], n):
            num = ""
            for digit in pandigital:
                num += digit
            if isprime(int(num)):
                primepandigitals.append(int(num))
    print("Found " + str(len(primepandigitals)) + " pandigital prime numbers")
    print(max(primepandigitals))
