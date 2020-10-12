#!/usr/bin/python3

# Let's just generate fibonacci numbers until we find one with more than 1000 digits
curr = 1
prev = 1
i = 2

while len(str(curr)) < 1000:
    tmp = curr
    curr = curr + prev
    prev = tmp
    i += 1

print(i)
