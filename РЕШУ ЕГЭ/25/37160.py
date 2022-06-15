def f(n):
    count = 0
    for d in range(18, n, 10):
        if n % d == 0:
            return d
    return -1

n = 500000 + 1
count = 0
while count != 5:
    if f(n) != -1:
        print(n, f(n))
        count += 1
    n += 1


