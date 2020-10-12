#!/usr/bin/python3

# Let's not reinvent the wheel here
import num2words

s = 0
for i in range(1, 1001):
    s += len(num2words.num2words(i, lang='en_GB').replace(" ", "").replace("-", ""))

print(s)
