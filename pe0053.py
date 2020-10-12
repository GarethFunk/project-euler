from math import factorial


def nCr(n, r):
    return factorial(n)//(factorial(r) * factorial(n-r))


if __name__ == "__main__":
    num_greater_1mil = 0
    for n in range(1, 101):
        for r in range(1, n):
            if nCr(n, r) > 1000000:
                num_greater_1mil += 1
    print(num_greater_1mil)
