#!/usr/bin/python3

def distinctpowers(n):
    powers = []
    for a in range(2, n+1):
        for b in range(2, n+1):
            powers.append(a**b)
    return len(set(powers))


if __name__ == "__main__":
    print(distinctpowers(5))
    print(distinctpowers(100))
