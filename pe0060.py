from pe0003 import isprime
from pe0050 import getprimes

from copy import deepcopy
from itertools import permutations, combinations, product


def concatenate(x):
    return int(str(x[0]) + str(x[1]))


def findValidSets(input_set, member_length):
    # Takes in an iterable of iterables (preferably set of frozensets)
    # Gives back only those which have the prime pair set property
    num_permutations = len(
        list(permutations([0]*member_length, 2)))  # A bit gross
    print("Searching through " + str(len(input_set)) + " possible combinations...")
    valid_sets = set()
    for primes in input_set:
        num_prime_pairs = 0
        # This will give us the pairs both ways round
        for x in permutations(primes, 2):
            if isprime(concatenate(x)):
                num_prime_pairs += 1
            else:
                break
            if num_prime_pairs == num_permutations:
                # All the pairs we checked were prime
                valid_sets.add(frozenset(primes))
    return valid_sets


def combineSets(input_sets, pairs):
    output_set = set()
    for input_set in input_sets:
        input_set = list(input_set)
        pairs_with_matching_items = []
        number_of_matching_pairs = []
        for i in range(len(input_set)):
            matching_item_pairs = [x for x in pairs if input_set[i] in x]
            if len(input_set) == 2:
                matching_item_pairs.remove(frozenset(input_set))
            pairs_with_matching_items.append(matching_item_pairs)
            number_of_matching_pairs.append(len(matching_item_pairs))
        # Now, we must find an element (not from the input_set) in each list that appears in all lists
        # Might as well just check the shortest list seeing as it must be in that one anyway
        element_index_with_smallest_list = number_of_matching_pairs.index(
            min(number_of_matching_pairs))
        shortest_list_of_pairs = pairs_with_matching_items[element_index_with_smallest_list]
        for candidate_pair in shortest_list_of_pairs:
            element_to_ignore = input_set[element_index_with_smallest_list]
            candidate_number = deepcopy(candidate_pair)
            candidate_number = list(candidate_number)
            candidate_number.remove(element_to_ignore)
            candidate_number = candidate_number[0]
            if candidate_number in input_set:
                continue  # Not a new number
            number_of_times_to_find_candidate_number = len(input_set) - 1
            number_of_times_found_candidate_number = 0
            for i in range(len(input_set)):
                # Run through all the other lists
                if i == element_index_with_smallest_list:
                    continue
                found_num = False
                for test_pair in pairs_with_matching_items[i]:
                    if candidate_number in test_pair:
                        number_of_times_found_candidate_number += 1
                        found_num = True
                        break
                # If we haven't found it in a given list, we can stop checking that candidate number.
                if found_num is False:
                    break
            if number_of_times_found_candidate_number == number_of_times_to_find_candidate_number:
                # Candidate number was found in all the other lists, it and the input set form a new valid set with length +1
                output_set.add(frozenset(input_set + [candidate_number]))
    return output_set


if __name__ == "__main__":
    # Basic approach (after many failed attempts):
    # Get a list of pairs of primes which have the desired property.
    # From this list, find triples with the property by combining pairs based on elements in common
    # Then find quadruples with the property by combining triples with pairs based on elements in common
    # Then find quintuples with the property by combining quadruples with pairs based on elements in common
    all_primes = getprimes(n=1100)  # first n primes
    # remove the ones where, if they occured at the end, would always mean non-prime
    all_primes.remove(2)
    all_primes.remove(5)
    print("Starting with " + str(len(all_primes)) + " prime numbers.")
    # First do it will all combinations of length 2 to narrow the list down
    prime_pairs = set(list(combinations(all_primes, 2)))
    valid_pairs = findValidSets(prime_pairs, 2)
    print("Found " + str(len(valid_pairs)) + " pairs.")
    reference_pairs = deepcopy(valid_pairs)
    valid_triples = combineSets(valid_pairs, reference_pairs)
    print("Found " + str(len(valid_triples)) + " triples.")
    valid_fours = combineSets(valid_triples, reference_pairs)
    print("Found " + str(len(valid_fours)) + " fours.")
    valid_fives = combineSets(valid_fours, reference_pairs)
    print(valid_fives)
