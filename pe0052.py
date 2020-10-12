
def getdigits(n):
    # Returns a sorted list of the digits
    return sorted(list(str(n)))


if __name__ == "__main__":
    n = 0
    found = False
    while not found:
        n += 1
        digits = getdigits(n)
        for multiplier in [2, 3, 4, 5, 6]:
            if getdigits(n*multiplier) == digits:
                found = True
            else:
                found = False
                break
    print(n)
