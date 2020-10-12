# We don't need to do anything too clever here

n = 0
for i in range(1, 1001):
    n += i**i
print(str(n)[-10:])
