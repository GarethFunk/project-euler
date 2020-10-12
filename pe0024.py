# There are 10! = 3,628,800 permutations of characters 0 1 2 3 4 5 6 7 8 9
# We can generate these permutations in lexicographic order
# There are 9!  = 362,880 permutations for each starting digit
# Therefore the millionth will start with a 2.
# We can follow this pattern to find the millionth
# BUT, once we use a multiplier, we can't use it again
# That was very badly explained. It works though!

from pe0020 import factorial


def nthlexicographicpermutation(n, m):
    # m is the number of consecutive digits starting at 0
    if n > factorial(m):
        return -1
    var = 0
    facts = []
    multipliers = []
    for i in range(0, m):
        reduced_n = n
        for j, fact in enumerate(facts):
            reduced_n -= fact*multipliers[j]
        facts.append(factorial(m-i-1))
        multipliers.append(reduced_n//facts[i])
    print(facts)
    print(multipliers)
    s = 0
    for i in range(m):
        s += facts[i]*multipliers[i]
    print(s)  # Sanity check
    # Now we need to determine the exact permutation
    digits = list(range(m))
    permutation = ""
    for mult in multipliers:
        permutation += str(digits.pop(mult))
    return permutation


if __name__ == "__main__":
    # Gotta use 999,999 for the 1,000,000th one because the function is zero indexed
    print(nthlexicographicpermutation(999999, 10))
