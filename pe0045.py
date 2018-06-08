from math import sqrt

from pe0044 import p, ispentagon
from pe0042 import istriangle

def ishexagon(h):
    # h = n(2n - 1)
    # 2n^2 - n - h = 0
    # 1 ± sqrt(1 + 8*h) = 4n
    # n > 0 so take +ve sqrt
    if (1 + sqrt(1 + (8*h)))%4 == 0:
        return True
    else:
        return False

def h(n):
    return int(n*((2*n) - 1))

if __name__ == "__main__":
    # Hexagonal numbers are bigger than triangular and pentagonal 
    # We will have to check fewer if we scan hexgonal
    n = 144
    found = False
    while not found:
        hexagon = h(n)
        if ispentagon(hexagon) and istriangle(hexagon):
            found = True
            print(hexagon)
        n += 1