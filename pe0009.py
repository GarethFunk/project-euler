#!/usr/bin/python3

# How to find Pythagorean triplet s.t. a + b + c = 1000 ?
# Largest number for a, b, or c naievely is 998 (with the other two being 1)
# Let's say c <= 998. We can find pythagorean triplets for c = 1 to 998 (if they exist)
# Then check a + b + c

def findtriplet(c):
    c2 = c*c
    # Sum of squares is always less than square of sum
    # Therefore c^2 < (a+b)^2
    # So c < (a+b)
    # Because b > a, the largest b could be is c-1 with a = 1
    for b in range(2, c):
        b2 = (b*b)
        for a in range(1, b):
            if (a*a) + b2 == c2:
                # We have a triple
                return (a, b)
            if a + b + c > 1000:
                break
    # If we get this far, we didn't find it
    return (0, 0)


if __name__ == "__main__":
    for c in range(1, 999):  # 999 because of range < not <=
        a, b = findtriplet(c)
        if a + b + c == 1000:
            print("Found a + b + c = 1000\na*b*c = ")
            print(a*b*c)
            print((a, b, c))
            break
