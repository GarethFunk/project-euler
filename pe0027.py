# for n^2 + an + b to give consecutive primes starting at n = 0, b must always be prime
# So we need a list of prime numbers below or up to 1,000.
# Prime numbers are all positive so we can take that into account

from pe0003 import isprime

primes = []
for i in range(2, 1001):
    if isprime(i):
        primes.append(i)

longest_sequence = (0, 0, 0)  # (a, b, n)
for a in range(-999, 999):
    for b in primes:
        n = 0
        ans = (n*n)+(a*n)+b
        while ans > 0 and isprime(ans):
            n += 1
            ans = (n*n)+(a*n)+b
        if n > longest_sequence[2]:
            longest_sequence = (a, b, n)

print(longest_sequence)
a, b, n = longest_sequence
print(a*b)
