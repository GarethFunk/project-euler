from math import sqrt

# x2 – Dy2 = 1
# (x + y*sqrt(D)) * (x - y*sqrt(D)) = 1

def DiophantineQuadraticSolver(D):
    # Note that for D > 1, x > y
    if int(sqrt(D))**2 == D:
        return 0, 0
    x = 2
    while True:
        # y = sqrt((x2 - 1)/D)
        y2 = ((x * x) - 1)/D
        if int(y2) == y2:
            y = sqrt(y2)
            if int(y)**2 == y2:
                return x, int(y)
        x += 1
    return 0, 0

if __name__ == "__main__":
    biggest_x = 0
    corresponding_D = 0
    for D in range(1, 1001):
        x, y = DiophantineQuadraticSolver(D)
        print(D, x, y)
        if x > biggest_x:
            biggest_x = x
            corresponding_D = D

print(corresponding_D)


