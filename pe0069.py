#!/usr/bin/python3

if __name__ == "__main__":
    factors = {}
    N = 10000
    for i in range(1, N + 1):
        factors[i] = set([1, i])
    for i in range(2, N + 1):
        j = 2
        product = i * j
        while product <= N:
            factors[product].add(i)
            factors[product].add(j)
            j += 1
            product = i * j
    # Now we have a list of all the factors of all the numbers
    # To tell if two numbers are coprime, the intersection of their sets of
    # factors should be just {1}
    max_n_over_totient_n = 0
    max_n = 0
    for n in range(2, N + 1):
        # Calculate totient of n
        totient = 0
        for i in range(1, n):
            if factors[i].intersection(factors[n]) == {1}:
                totient += 1
        if n / totient > max_n_over_totient_n:
            max_n_over_totient_n = n / totient
            max_n = n
    print(max_n, max_n_over_totient_n)
