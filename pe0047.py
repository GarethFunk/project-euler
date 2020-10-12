from lib import factors, isprime

def primeFactors(n, conv=False):
    prime_factors = {}
    for pair in factors(n):
        for num in pair:
            if isprime(num):
                prime_factors[num] = 1
    prod = 1
    for prime_factor in prime_factors:
        prod = prod * prime_factor
    while prod != n:
        quotient = n/prod  # i.e. what we still need to represent with the prime factors
        for prime_factor in prime_factors:
            if quotient%prime_factor == 0:
                prod = prod * prime_factor
                prime_factors[prime_factor] += 1
    if conv is False:
        return prime_factors
    else:
        return primefactorconverter(prime_factors)


# This converts e.g. 2^2, 5, 7 into 4, 5, 7
# This makes it easier to compare prime factors
def primefactorconverter(pfs):
    converted = []
    for pf in pfs:
        converted.append(pf**pfs[pf])
    return set(converted)
    

if __name__ == "__main__":
    nums = []
    pfs = []
    n = 2
    found = False
    consecutive = False
    while found is False:
        pf = primeFactors(n, True)
        if len(pf) != 4:
            consecutive = False
        else:
            if consecutive is False:
                nums = [n]
                pfs = [pf]
                consecutive = True
            else:
                nums.append(n)
                pfs.append(pf)
            if len(nums) == 4:
                # We have found four consecutive numbers with four prime factors
                # Now check if they're distinct
                intersection = pfs[0] & pfs[1] & pfs[2] & pfs[3]
                if len(intersection) == 0:
                    # There were no common factors
                    print(nums)
                    print(pfs)
                    found = True
                else:
                    # There were some common factors - remove first element
                    del pfs[0]
        n += 1