from lib import isprime

# Let's just run through all the odd natural numbers starting at 3
primes = [2]
testnum = 3
while len(primes) != 10001:
    if isprime(testnum):
        primes.append(testnum)
    testnum += 2

print(primes[-1])
