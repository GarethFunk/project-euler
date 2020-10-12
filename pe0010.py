from lib import isprime

# let's see if we can just check all odd numbers below 2,000,000
s = 2  # Sum starts at 2 because we're missing 2 out of the range
for n in range(3, 2000000, 2):
    if isprime(n):
        s += n

print(s)

# Takes about 30sec or so. Fit for purpose.
