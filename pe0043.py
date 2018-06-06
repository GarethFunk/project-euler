from itertools import permutations

digits = "0123456789"

def substringdivisible(s):
    if int(s[1:4])%2 != 0:
        return False
    if int(s[2:5])%3 != 0:
        return False
    if int(s[3:6])%5 != 0:
        return False
    if int(s[4:7])%7 != 0:
        return False
    if int(s[5:8])%11 != 0:
        return False
    if int(s[6:9])%13 != 0:
        return False
    if int(s[7:])%17 != 0:
        return False
    return True


if __name__ == "__main__":
    numbers = []
    for pandigital in permutations(digits, 10):
        num = ""
        for digit in pandigital:
            num += digit
        # Assume leading zero is not okay?
        if num[0] == "0":
            continue
        if substringdivisible(num):
            numbers.append(int(num))
            print(num)
    print(sum(numbers))
        