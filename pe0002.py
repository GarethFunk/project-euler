def sumevenfib(n):
    fib = [1, 2]
    s = 2
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
        if fib[-1]%2 == 0:
            s += fib[-1]
    return s

print(sumevenfib(4000000))
