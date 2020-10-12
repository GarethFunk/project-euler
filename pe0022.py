#!/usr/bin/python3

f = open("pe0022_names.txt")
raw = f.read()
f.close()

# get rid of quote marks
raw = raw.replace('"', "")
names = raw.split(",")
names.sort()

scores = []
for i, name in enumerate(names, 1):
    s = 0
    name = name.upper()
    for letter in name:
        # This adds up the letter as specified in the problem using ascii values
        s += ord(letter) - 64
    scores.append(s*i)

print(sum(scores))
