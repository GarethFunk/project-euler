def multipleoffiveorthree(n):
    if n%5 == 0 or n%3 == 0:
        return True
    else:
        return False

def sumofmultiples(n):
    s = 0
    for i in range(1, n):  # Don't include n in the range
        if multipleoffiveorthree(i):
            s += i
    return s

print(sumofmultiples(10))
print(sumofmultiples(1000))
