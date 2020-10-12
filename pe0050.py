#!/usr/bin/python3

# A simple approach might be to, starting at 2 add up all the primes,
# checking if the sum is prime at each step, until the sum exceeds 1,000,000
# Then to repeat starting at 3, starting at 5 etc. and compare results
# This will guarantee the correct answer but seems like a lot of compuation

from copy import deepcopy

from lib import isprime


def getprimes(n=None, below=None):
    primes = [2]
    num = 3
    if below is None:
        while len(primes) < n:
            if isprime(num):
                primes.append(num)
            num += 2
    elif n is None:
        while num < below:
            if isprime(num):
                primes.append(num)
            num += 2
    return primes


if __name__ == "__main__":
    # First get a list of all prime numbers below 1,000,000
    primes = getprimes(below=1000000)
    print("Got " + str(len(primes)) + " primes")
    # We will store sums like (sum, num_terms)
    best = (0, 0)
    for i, startpoint in enumerate(primes[:-1]):
        best_for_this_start = (0, 0)
        length = 1
        summation = startpoint
        for prime in primes[i+1:]:
            summation += prime
            length += 1
            if summation > 1000000:
                break
            if isprime(summation):
                best_for_this_start = (summation, length)
        if best_for_this_start[1] > best[1]:
            best = deepcopy(best_for_this_start)
    print(best)
