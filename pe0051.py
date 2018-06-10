from copy import deepcopy
from itertools import combinations, combinations_with_replacement

from pe0003 import isprime

def digitreplace(n, checkprime=False):
    # This function will return all possible digit replacements
    # excluding replacing all digits
    # Note that a preceeding zero would cause the number to be omitted
    number = list(str(n))
    length = len(number)
    indices = list(range(length))
    replacement_digits = "0123456789"
    new_numbers = []
    for num_digits_to_replace in range(1, length):  # 1 to length-1 digits
        for replacement_indices in combinations(indices, num_digits_to_replace):
            this_pattern = []
            for digit in replacement_digits:
                new_number = deepcopy(number)
                for replacement_index in replacement_indices:
                    new_number[replacement_index] = digit
                # Now we have a new number
                # We want to omit numbers which start with a zero
                if new_number[0] != "0":
                    # Convert to an int
                    new_number = int("".join(new_number))
                else:
                    continue
                if checkprime is False or isprime(new_number):
                    this_pattern.append(new_number)
            if len(this_pattern) > 0:
                new_numbers.append(this_pattern)
    return new_numbers

if __name__ == "__main__":
    # Iterating one at a time will lead to a LOT of re-doing the same calculations
    # possible digit replacements of 10 are 1* and *0
    # possible digit replacements of 11 are 1* and *1
    # This is too intensive. We need to generate sequences we know will not re-do 
    # the same calculations.
    # For 2 digit numbers this means passing in [1-9]* and *[0-9]
    # For 3 digit numbers this means passing in [1-9]*[0-9], [1-9][0-9]*, *[0-9][0-9], **[0-9], *[0-9]* and[1-9]** 
    num_digits = 2
    found = False
    digits = list("0123456789")
    while not found:
        print(num_digits)
        num = list(range(num_digits))
        indices = list(range(num_digits))
        for digits_to_replace in range(1, num_digits):
            for pattern in combinations(indices, digits_to_replace):
                template = list(range(num_digits))
                nonindices = list(range(num_digits))
                for index in pattern:
                    # Generate the *'s in the sequences
                    template[index] = "9"  # Arbitrary number.
                    nonindices.remove(index)
                for remaining_digits in combinations_with_replacement(digits, len(nonindices)):
                    trial_pattern = deepcopy(template)
                    for i, index in enumerate(nonindices):
                        trial_pattern[index] = remaining_digits[i]
                    # At this point we have a unique pattern where we can run digitreplace
                    number = int("".join(trial_pattern))
                    new_prime_numbers = digitreplace(number, checkprime=True)
                    try:
                        longest_length = len(max(new_prime_numbers, key=lambda x: len(x)))
                    except ValueError:
                        # If max() is passed []
                        longest_length = 0
                    if longest_length == 8:
                        found = True
                        print(max(new_prime_numbers, key=lambda x: len(x)))
        num_digits += 1

