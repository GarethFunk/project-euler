# We will use this structure to store multiplicand, multiplier, product
# (multiplicand, multiplier, product)

def pandigital19(tup):
    s = ""
    s += str(tup[0])
    s += str(tup[1])
    s += str(tup[2])
    if len(s) != 9:
        return False 
    for digit in "123456789":
        if digit not in s:
            return False
    return True

if __name__ == "__main__":
    # Perhaps we can brute force it...
    # We need 9 digits in total so the smallest we can start is (10, 100, 1000)
    # By (10, 1000, 10000) we have too many digits so 1000 is upper bound on multiplier
    # By (100, 100, 10000) we have too many digits so 100 is upper bound on multiplicand
    pandigitals = {}
    for multiplicand in range(10, 100):
        for multiplier in range(100, 1000):
            product = multiplier*multiplicand
            if pandigital19((multiplicand, multiplier, product)):
                pandigitals[product] = (multiplicand, multiplier)
                #print(product)
    print(sum(pandigitals.keys()))