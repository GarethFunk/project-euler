#!/usr/bin/python3

def digitsum(n):
    s = str(n)
    digsum = 0
    for digit in s:
        digsum += int(digit)
    return digsum


if __name__ == "__main__":
    maxdigsum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            digsum = digitsum(a**b)
            if digsum > maxdigsum:
                maxdigsum = digsum
    print(maxdigsum)
