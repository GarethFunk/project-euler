#!/usr/bin/python3

# Find all right angled triangles with p <= 1000

from pe0009 import findtriplet

if __name__ == "__main__":
    triangles = {}
    for c in range(1, 999):
        a, b = findtriplet(c)
        p = a + b + c
        if p in triangles:
            triangles[p].append((a, b, c))
        else:
            triangles[p] = [(a, b, c)]
    print(max(triangles, key=lambda x: len(triangles[x])))
