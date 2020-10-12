#!/usr/bin/python3

# We need to find three four digit numbers that are prime,
# permutations of each other and are equispaced.
# We could run through all 4-digit numbers starting at 1000
# finding all permutations of digits (24 of them) the rule out
# those which are not prime. Then look for three which are equispaced

from itertools import permutations

from lib import isprime


def findequispaced(nums):
    # Start assuming the first number is in the equispaced sequence
    # We need to find at least three numbers to make it a sequence
    # If no seqeunce is found, then assume the second number is the
    # start of an equispaced sequence
    if len(nums) < 3:
        return []
    nums.sort()
    for i, start in enumerate(nums[:-2]):
        gaps = []
        for potential_sequence_member in nums[i+1:]:
            gaps.append(potential_sequence_member - start)
        for gap in gaps:
            if gap*2 in gaps:
                # We have found a sequence with gap
                return [start, start + gap, start + (2*gap)]
    return []


if __name__ == "__main__":
    for i in range(1000, 10000):
        primeperms = []
        for perm in permutations(str(i)):
            if perm[0] == "0":
                continue  # We need 4 digit numbers
            n = int(perm[0] + perm[1] + perm[2] + perm[3])
            if n not in primeperms and isprime(n):
                primeperms.append(n)
        seqeunce = findequispaced(primeperms)
        if len(seqeunce) > 0:
            print(seqeunce)
