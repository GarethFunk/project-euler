from lib import isprime


def rotate(s):
    rotated = ""
    for i in range(len(s)):
        rotated += s[i-1]
    return rotated


def iscircularprime(n):
    s = str(n)
    for i in range(len(s)):
        if isprime(int(s)) is False:
            return False
        s = rotate(s)
    return True


if __name__ == "__main__":
    primes = [2]
    for i in range(3, 1000000, 2):
        if isprime(i) is True:
            primes.append(i)
    print("found " + str(len(primes)) + " primes")
    circular_primes = []
    for prime in primes:
        if iscircularprime(prime) is True:
            circular_primes.append(prime)

    # print(circular_primes)
    print(len(circular_primes))
