def factorial(n):
    retval = 1
    for i in range(2, n+1):  # don't need to multiply by 1
        retval = retval*i
    return retval


def sumfactorialdigits(n):
    num = factorial(n)
    s = str(num)
    sumfact = 0
    for i in range(len(s)):
        sumfact += int(s[i])
    return sumfact


if __name__ == "__main__":
    print(sumfactorialdigits(100))
