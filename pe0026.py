#!/usr/bin/python3

# For this we need a recurrence finding algorithm
# We would first need to determine if the decimal terminates
# We know, because all these decimals are rational that they either terminate or reccur.
# So the algorithm can just look for termination or recurrence until one is spotted
# Question is, how many times do you look for a recurrence before deciding it is there?
# Let's see how we get on first.

from decimal import *

# The larger this is, the longer execution takes.
# 4 is the magic number here. Any less and we miss out the biggest recurrence.
pattern_threshold = 4


def recurringcycle(num):
    # A recurring cycle can be preceeded by an arbitrary length of non-recurring digits
    recurrence_found = False
    digits = []
    possible_patterns = []
    decimal_places = 0
    while recurrence_found is not True:
        decimal_places += 1
        #nth_decimal_place, exact = nthdecimalplace(num, decimal_places)
        digits, exact = ndecimalplaces(num, decimal_places)
        if exact is True:
            # There is no repeating pattern
            return False
        else:
            # digits.append(nth_decimal_place)
            patterns = getpatterns(digits, pattern_threshold)
            valid_pattern = testpatterns(digits, patterns, pattern_threshold)
            if valid_pattern is False:
                # print(digits)
                # print(patterns)
                continue
            else:
                return valid_pattern
    return False


def getpatterns(digits, threshold):
    # For n digits there are n possible recurring patterns from (n) to (1, 2, ..., n-1, n)
    # But we only want the ones we can test
    patterns = []
    for i in range(1, len(digits)//threshold):
        candidate_pattern = digits[-i:]
        patterns.append(candidate_pattern)
    return patterns


def testpatterns(digits, patterns, threshold):
    # For each pattern, we want to scan through the digits seen so far
    for pattern in patterns:
        valid = False  # We will see if we can disprove this
        if digits[-1*len(pattern):] == pattern:
            # The back end matched, now let's meet the threshold
            valid = True
            for i in range(1, threshold):
                if digits[-1*(i+1)*len(pattern):-1*(i)*len(pattern)] == pattern:
                    valid = True
                else:
                    valid = False
                    break
            if valid is True:
                # This pattern has been found
                return pattern
        else:
            valid = False
    # If we got this far without returning then no valid patterns were found
    return False


def ndecimalplaces(num, n):
    # Instead of returning the nth, the returns all n
    setcontext(DefaultContext)  # Resets all flags
    # Use as many decimal places as we need (last one might be rounded)
    getcontext().prec = n+1
    dec = Decimal(1)/Decimal(num)
    sign, digits, exponent = dec.as_tuple()
    zeros = []
    num_preceeding_decimal_zeros = (exponent*-1) - len(digits)
    for i in range(num_preceeding_decimal_zeros):
        zeros.append(0)
    return (zeros + list(digits))[:n], not getcontext().flags[Inexact]


def nthdecimalplace(num, n):
    # We are going to shift through all the decimal places by multiplying the number by 10
    # each time, flooring and modulo 10
    # This doesn't work all in one go because at high powers of 10 you run into floating point
    # innaccuracies. We need to use the decimal module
    # This module again has precision limitations
    setcontext(DefaultContext)  # Resets all flags
    # Use as many decimal places as we need (last one might be rounded)
    getcontext().prec = n+1
    dec = Decimal(1)/Decimal(num)
    sign, digits, exponent = dec.as_tuple()
    num_preceeding_decimal_zeros = (exponent*-1) - len(digits)
    index_of_nth_decimal = n - num_preceeding_decimal_zeros - \
        1  # -1 is for zero index 1st decimal place at [0]
    if n <= num_preceeding_decimal_zeros:
        # The desired decimal place is a preceeding zero
        nth_decimal_place = 0
    else:
        # The desired decimal place may not be in the digits we have
        if index_of_nth_decimal < len(digits):
            nth_decimal_place = digits[index_of_nth_decimal]
        else:
            # The desired decimal place goes beyond our digits and is therefore zero
            nth_decimal_place = 0
    return nth_decimal_place, not getcontext().flags[Inexact]


if __name__ == "__main__":
    recurring_cycles = []
    for i in range(1, 1000):
        print(i)
        cycle = recurringcycle(i)
        if cycle is not False:
            recurring_cycles.append((i, cycle))
    print(max(recurring_cycles, key=lambda x: len(x[1])))
