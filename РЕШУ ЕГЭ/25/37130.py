def div7(n):
    for d in range(17, n, 10):
        if n % d == 0:
            return d
    return -1

n = 600000 + 1
count = 0
while count != 5:
    div = div7(n)
    if div != -1:
        print(n, div)
        count += 1
    n += 1



