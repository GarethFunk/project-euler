# We could devise an algorithm to come up with all the different ways
# There are too many ways (when you keep order in mind)
# We need a way to find the ways agnostic to order of coins

coins = [200, 100, 50, 20, 10, 5, 2, 1]

# i is the place to start searching in the list
def waystomake(n, i=0):
    if n == 0:
        return [[0, 0, 0, 0, 0, 0, 0, 0]]
    ways = []
    for j in  range(i, len(coins)):
        if coins[j] <=n:
            way = [0, 0, 0, 0, 0, 0, 0, 0]
            way[j] += 1
            for way_for_n_minus_coin in waystomake(n-coins[j], j):
                ways.append(addways(way, way_for_n_minus_coin))
    return ways

def addways(w1, w2):
    way = []
    for i in range(len(w1)):
        way.append(w1[i] + w2[i])
    return way


if __name__ == "__main__":
    ways = waystomake(200)
    print(len(ways))