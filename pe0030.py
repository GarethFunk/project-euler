#!/usr/bin/python3

# The number clearnly needs to have 2 or more digits, but what's the upper bound?
# Let's keep going up to 1,000,000 and see where we get to.
# There was one six digit number which worked and two four digit numbers.
# Let's go to 10,000,000
# No more found... Call it a day?

def digitnthpower(num, n):
    s = str(num)
    digit_sum = 0
    for c in s:
        digit_sum += int(c)**n
    return digit_sum == num


if __name__ == "__main__":
    digit_powers = []
    for i in range(10, 10000000):
        if digitnthpower(i, 5):
            print(i)
            digit_powers.append(i)
    print(sum(digit_powers))
