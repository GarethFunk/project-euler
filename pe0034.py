#!/usr/bin/python3

# The digit factorial sum of a number does not scale with the size of the number
# 10^362879 has the same digit factorial sum as 9
# For an n digit number, the smallest digit factorial sum is n 1's
# Whose DFS = n. 10^(n-1) > (n*1) for all integer n > 1
# and the largest digit factorial sum is n 9's
# 9.(9)x10^(n-1) < n*362,880 for all integer n < N
# finding N finds an upper bound on the numbers we need to examine

from pe0020 import factorial

factorials = {0: 1,
              1: factorial(1),  # 1
              2: factorial(2),  # 2
              3: factorial(3),  # 6
              4: factorial(4),  # 24
              5: factorial(5),  # 120
              6: factorial(6),  # 720
              7: factorial(7),  # 5,040
              8: factorial(8),  # 40,320
              9: factorial(9)}  # 362,880


def nines(n):
    s = ""
    for i in range(n):
        s += "9"
    return int(s)


def findN():
    num_digits = 1
    while nines(num_digits) < factorials[9]*num_digits:
        num_digits += 1
    return num_digits


def digitfactorialsum(n):
    s = str(n)
    digits = []
    for char in s:
        digits.append(int(char))
    # Sort the digits in reverse order so we fail fast
    digits.sort(reverse=True)
    dfs = 0
    for digit in digits:
        dfs += factorials[digit]
        if dfs > n:
            return False
    if dfs == n:
        return True
    else:
        return False


if __name__ == "__main__":
    N = findN()
    print(N)
    sumdfs = 0
    for i in range(3, 10**N):
        if digitfactorialsum(i):
            sumdfs += i
    print(sumdfs)
