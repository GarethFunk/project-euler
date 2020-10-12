#!/usr/bin/python3

# a 16 digit string is formed by putting the only 2 digit number, 10,
# in one of the outer rings, otherwise it would be double counted forming
# a 17 digit string

# There are 10! (=~3.6million) ways to put the digits (not all will be valid)
# Knowing that the 10 must be in one of five places, it's 5 * 9! =~1.8million

# A valid solution is actually one of 5 in a family of rotations
# So the number of solutions is 5 * 9! / 5 = 362,880 (not all valid)

# Doesn't seem crazy to just compute them all, check which ones are valid,
# and find the longest string

def FiveGonRing(a, b, c, d, e, f, g, h, i, j):
    # a, b, c, d, e = the outer five points
    # f, g, h, i, j = the inner five points (corresponding)
    # Thus the five triplets are:
    # a, f, g
    # b, g, h
    # c, h, i
    # d, i, j
    # e, j, f
    # These five triplets form a Solution Set
    # A Solution Set is valid iff all members sum to the same value
    return frozenset([(a, f, g),
                      (b, g, h),
                      (c, h, i),
                      (d, i, j),
                      (e, j, f)])


def Valid(fivegonring):
    # Check sums are equal
    linesum = None
    for line in fivegonring:
        if linesum is None:
            linesum = sum(line)
            continue
        else:
            if sum(line) != linesum:
                return False
    return True


def StringFiveGonRing(fivegonring):
    # Need to figure out the order again
    lines = list(fivegonring)
    lines.sort(key=lambda tup: tup[0])
    ordered_fivegonring = [lines[0]]
    lines.remove(lines[0])
    while len(lines) > 0:
        for line in lines:
            if ordered_fivegonring[-1][-1] == line[-2]:
                ordered_fivegonring.append(line)
                lines.remove(line)
                break
    string = "".join(["".join([str(s) for s in list(x)])
                      for x in ordered_fivegonring])
    return string


if __name__ == "__main__":
    from itertools import permutations
    fgr = FiveGonRing(10, 9, 8, 7, 6, 3, 1, 4, 2, 5)
    print(Valid(fgr))
    print(StringFiveGonRing(fgr))
    solutions = set()
    for a, b, c, d, e, f, g, h, i, j in permutations(range(1, 11)):
        solutions.add(FiveGonRing(a, b, c, d, e, f, g, h, i, j))
    valid_solutions = {x for x in solutions if Valid(x)}
    strings = {StringFiveGonRing(x) for x in valid_solutions}
    strings_16 = {x for x in strings if len(x) == 16}
    print(max({int(x) for x in strings_16}))
