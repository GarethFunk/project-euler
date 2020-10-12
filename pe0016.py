#!/usr/bin/python3

n = 2**1000
string = str(n)
s = 0

for i in range(len(string)):
    s += int(string[i])

print(s)
