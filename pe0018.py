# We can search though it intelligently or by brute force
# Intelligent thoughts:
# We know we will be adding 15 numbers together and we know the largest number that occurs is 99
# Therefore, as we explore pathways, if after n steps, a path is more than (14-n)*99 behind the best path
# then it can be culled because there is no way it could catch up.
# According to the footnote in the problem, this one can be brute forced quickly but problem 67 is the
# same with a 100 row triangle and therefore cannot. 


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
# (ROW, COL, SUM, [LIST, OF, ALL, NUMS, IN, SUM])

def maxtrianglesum(t):
    paths = [[(0, 0, t[0][0], [t[0][0]])]]
    for i in range(1, len(t)):
        # Get all the new possibilites
        new_paths = []
        for path in paths[i-1]:
            new_paths += nexttwo(t, path)
        # Now trim these down by the rule above
        max_sum = max(new_paths, key=lambda x:x[2])[2]
        num_removed = 0
        for path in new_paths:
            if path[2] + ((14-i)*99) < max_sum:
                # This path cannot possibly beat the best path so remove it
                new_paths.remove(path)
                num_removed += 1
        print("On row " + str(i) + ", " + str(num_removed) + " paths were removed")
        paths.append(new_paths)
    best_path = max(paths[-1], key=lambda x:x[2])
    return best_path
                
def nexttwo(t, tup):
    i, j, s, nums = tup
    # Indices of lower adjacent numbers are [i+1][j] and [i+1][j+1]
    left_num = t[i+1][j]
    left = (i+1, j, s+left_num, nums + [left_num])
    right_num = t[i+1][j+1]
    right = (i+1, j+1, s+right_num, nums + [right_num])
    return [left, right]

print(maxtrianglesum(triangle))

    
