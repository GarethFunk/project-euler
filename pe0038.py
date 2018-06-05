
def pandigital(s):
    if len(s) != 9:
        return False 
    for digit in "123456789":
        if digit not in s:
            return False
    return True

def concatencatedproduct(x, n):
    retval = ""
    for i in range(1, n+1):
        retval += str(x * i)
    return retval

if __name__ == "__main__":
    maxval = 0
    # We have to concatenate at least two numbers and get a 9 digit number
    # Stopping searching at 100000 will cover all cases
    for i in range(1, 100000):
        n = 2
        s = concatencatedproduct(i, n)
        while len(s) < 10:
            if pandigital(s):
                if int(s) > maxval:
                    maxval = int(s)
                    print(s)
            n += 1
            s = concatencatedproduct(i, n)