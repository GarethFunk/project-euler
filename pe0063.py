#!/usr/bin/python3

from itertools import count


def digitCount(n):
    return len(str(n))


if __name__ == "__main__":
    number_of_n_digit_nth_powers = 0
    for base in count(start=1):
        # If we base**2 and has more digits than 2 digits, we are done, all larger bases will have this property
        if digitCount(base**2) > 2:
            break
        for exponent in count(start=1):
            num_digits = digitCount(base**exponent)
            if num_digits == exponent:
                number_of_n_digit_nth_powers += 1
            elif exponent > num_digits:
                # As soon as the exponent is larger than the number of digits, it will stay that way
                break
    print(number_of_n_digit_nth_powers)
