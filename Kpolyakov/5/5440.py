def f(n, m):
    sn = sum([int(x) for x in bin(n)[2:]])**2
    sm = sum([int(x) for x in bin(m)[2:]])**2
    return sn - sm

alls = set()
for n in range(1, 1000):
    for m in range(1, 1000):
        if f(n, m) == 33:
            alls.add(n + m)
print(min(alls))