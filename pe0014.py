#!/usr/bin/python3

# I expect we will retrace our steps a lot here because when a number comes up, if we've
# come accross it before, we have alraedy calculated the whole sequence.
# All that needs to be stored is the length of the sequence from that number to 1
# Let's use a dict for this with key = number and value = length of rest of sequence

# We can initialise this edge case so we always terminate
known_collatz = {1: 1}
longest_chain = (1, 1)


def collatz(n):
    global longest_chain
    if n in known_collatz:
        #print("It is known.")
        return known_collatz[n]
    m = 0  # Next term in the sequence
    if n % 2 == 0:  # If even
        m = int(n/2)
    else:
        m = int((3*n) + 1)
    # print(m)
    length = collatz(m) + 1
    known_collatz.update({n: length})
    if length > longest_chain[1]:
        longest_chain = (n, length)
    return length


# Now work out the lengths of sequences starting between 1 and 1,000,000
for n in range(1, 1000000):
    collatz(n)

# Sanity check: known_collatz should have AT LEAST 999,999 entries (probably more because the sequence
# will often go to larger numbers before going to 1
print(len(known_collatz))
print(longest_chain)
