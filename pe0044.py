"""
P(k) + P(j) = P(m)
P(k) - P(j)) = P(n)

k(3k-1) + j(3j-1) = m(3m-1)
k(3k-1) - j(3j-1) = n(3n-1)
Two equations in four variables - cannot be solved uniquely

n < m
k > j

minimise P(k) - P(j)
minimise P(n) = n(3n-1)
minimise n

n < j 
n < k

Therfore, the first pair of pentagon numbers we find whose sum and difference are 
also pentagon numbers will minimise the difference 
"""

def p(n):
    return int((n*((3*n) - 1))/2)

if __name__ == "__main__":
    pentagons = [p(1)]
    sums_to_check = []
    n = 2
    current = p(n)
    solved = False
    while not solved:
        print(n)
        # The difference between the current pentagonal and the second most recent is a 
        # a lower bound on the difference between any subsequent pentagonals and those previous
        # As such we can trim our list of pentagonals
        cutoff = current - pentagons[-1]
        for i, pentagon in enumerate(pentagons, 1):
            if pentagon < cutoff:
                pentagons.remove(pentagon)
                continue
            difference = current - pentagon
            # If the difference is a pentagon, we will have already seen it
            if difference in pentagons:
                psum = current + pentagon
                sums_to_check.append((psum, difference, current, pentagon))
                #print("Difference found: P(" + str(n) + ") - P(" + str(i) + ")")
        for sums in sums_to_check:
            if sums[0] in pentagons:
                solved = True
                print(sums)
            # We can remove this one from our search if the latest pentagon number is 
            # larger than it cos pentagons are monotonic increasing. 
            elif sums[0] < pentagons[-1]:
                sums_to_check.remove(sums)
        pentagons.append(current)
        n += 1
        current = p(n)