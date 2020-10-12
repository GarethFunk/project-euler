from pe0004 import ispallindrome


def binary(n):
    return int(bin(n)[2:])


if __name__ == "__main__":
    base10_pallindromes = []
    # Get base 10 pallindromes
    for i in range(1, 1000000):
        if ispallindrome(i) is True:
            base10_pallindromes.append(i)
    base10_base2_pallindromes = []
    print("Found " + str(len(base10_pallindromes)) + " base 10 pallindromes...")
    # Check the base 10 pallindromes to see if they're also pallindromes in base 2
    for pallindrome in base10_pallindromes:
        if ispallindrome(binary(pallindrome)):
            base10_base2_pallindromes.append(pallindrome)
    print("Found " + str(len(base10_base2_pallindromes)) +
          " base 10 & base 2 pallindromes...")
    print(sum(base10_base2_pallindromes))
