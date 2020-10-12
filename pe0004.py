
def ispallindrome(n):
    s = str(n)
    # We want to round this down cos middle character doesn't affect symmetry
    for i in range(int(len(s)/2)):
        if s[i] != s[-1*(i+1)]:
            return False
    # If we reach here without returning, it is a pallindrome
    return True


if __name__ == "__main__":
    # Naive approach: multiply all 3 digit numbers by all other 3 digit numbers (~ 1 million multiplications)
    pallindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if ispallindrome(i*j):
                pallindromes.append(i*j)
    print(max(pallindromes))
