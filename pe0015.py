#!/usr/bin/python3

# This problem can be rephrased quite simply thus:
# You have two numbers (i, j) and each one can increase one at a time by 1 each time
# There are six unique sequences starting at (0, 0) and ending at (2, 2)
# It is quite plain that i and j are the coordinates on the grid

# Let's go a step further, you have a set of {+1 +1 -1 -1}, each +1 for each time
# you go right and each -1 for each time you go down
# How many ways can you arrange these 4 things?
# 4C2 = 6

# For the 20x20 problem we have 20 +1 and 20 -1
# How many ways can we arrange these 40 things?
# 40C20 = 137846528820
