from pe0003 import isprime

def truncateleft(n):
    s = str(n)
    return int(s[1:])

def truncateright(n):
    s = str(n)
    return int(s[:-1])

if __name__ == "__main__":
    truncatable_primes = []
    n = 11  # Single digit primes don't count
    while len(truncatable_primes) < 11:
        if isprime(n):
            left = n
            right = n
            for i in range(len(str(n)) - 1):
                left = truncateleft(left)
                right = truncateright(right)
                if isprime(left) and isprime(right):
                    if len(str(left)) == 1:
                        # That's the last time we will be truncating
                        truncatable_primes.append(n)
                        print(n)
                else:
                    break
        n += 2
    print(sum(truncatable_primes))