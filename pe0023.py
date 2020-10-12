#!/usr/bin/python3

from pe0021 import d

# All numbers between 1 and 28,123 (inclusive) may or may not be expressed as the sum of two abundant numbers
# Some can, some cannot. So we need a way to determine if a number can be expressed as a sum of two abundant numbers

# A naive approach would be to find all abundant numbers less than or equal to 28,123 and add them all to each other

deficients = []
perfects = []
abundants = []

for i in range(1, 28124):
    di = d(i)
    if di < i:
        deficients.append(i)
    elif di > i:
        abundants.append(i)
    else:
        perfects.append(i)

print(len(deficients))
print(len(abundants))
print(len(perfects))

# There are 21,153 deficents, 6,965 abundants and 5 perfects in this range
# So to add each of the 6,965 abundants to each other one (including itself) we would have a total of
# ((6965^2 - 6965)/2) + 6965 additions to do = 24,259095
# That shouldn't take too long so let's just do it
# Some of these will addidtions will give the same result

sums = []
for i, ab1 in enumerate(abundants, 1):
    for ab2 in abundants[:i]:
        sums.append(ab1+ab2)

print(len(sums))  # To check it's as many as we'd expect
# Now let's put these in a set to remove duplicates
sumset = set(sums)
# 53,871 unique numbers in here. The largest is 56,244 and the smallest is 24
print(len(sumset))

# Now we have a way of knowing if a number can be made by adding two abundant numbers
sumnonabundant = 0
for i in range(1, 28124):
    if i not in sumset:
        sumnonabundant += i

print(sumnonabundant)
