# We can search though it intelligently or by brute force
# Intelligent thoughts:
# We know we will be adding 15 numbers together and we know the largest number that occurs is 99
# Therefore, as we explore pathways, if after n steps, a path is more than (14-n)*99 behind the best path
# then it can be culled because there is no way it could catch up.
# According to the footnote in the problem, this one can be brute forced quickly but problem 67 is the
# same with a 100 row triangle and therefore cannot.

# For each element on row n, there are two possible ways to get to that element (except edge ones)
# Only allow the highest values preceeding chain on row n-1 (highest of the two option) to go thorough a given point
# If there is a tie, pick aritrarily because the sum doesn't care which you pick
# Above pruning method is still valid but only comes into effect as the end is reached.
# Pruning makes the implementation a bit harder - no need with previous efficiency saving.
# Results of pruning printed to console for interest


triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

# Let's use the following data structure for keeping track of these things:
# (ROW, COL, SUM)


def maxtrianglesum(t):
    paths = [(0, 0, t[0][0],)]
    num_rows = len(t)
    for i in range(1, num_rows):
        # Get the new possibilites (cleverly)
        new_paths = []
        for j in range(len(t[i])):
            new_paths += parentchooser(t, i, j, paths)
        # Now trim these down by the rule above
        max_sum = max(new_paths, key=lambda x: x[2])[2]
        num_removed = 0
        max_possible_further_path = (num_rows-1-i)*99
        for path in new_paths:
            if path[2] + max_possible_further_path < max_sum:
                # This path cannot possibly beat the best path so remove it
                # new_paths.remove(path)
                num_removed += 1
        print("On row " + str(i) + ", " + str(num_removed) + " paths could be removed.\t" +
              str(len(new_paths)) + " being considered next round.")
        # Keeping track of all the old paths causes RAM issues on problem 67
        # By round 26, even forgetting old paths causes RAM shortages
        del(paths)
        paths = new_paths
    best_path = max(paths, key=lambda x: x[2])
    return best_path


def nexttwo(t, tup):
    i, j, s = tup
    # Indices of lower adjacent numbers are [i+1][j] and [i+1][j+1]
    i += 1
    left = (i, j, s+t[i][j])
    right = (i, j+1, s+t[i][j+1])
    return [left, right]


def parentchooser(t, i, j, paths):
    # Possible parents of i, j are located at [i-1][j] and [i-1][j-1]
    try:
        if paths[j][2] < paths[j-1][2]:
            # paths[j-1] is better
            best_sum = paths[j-1][2]
        else:
            # paths[j] is better (or the same)
            best_sum = paths[j][2]
    except IndexError:
        if j == 0:
            # path[j-1] doesn't exist
            best_sum = paths[j][2]
        else:
            best_sum = paths[j-1][2]
    return [(i, j, best_sum + t[i][j])]


print(maxtrianglesum(triangle))
