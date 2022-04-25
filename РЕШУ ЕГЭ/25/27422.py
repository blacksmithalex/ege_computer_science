def dividers(n):
    res = []
    for d in range(2, n):
        if n % d == 0:
            res.append(d)
    return res

for n in range(174457, 174505 + 1):
    D = dividers(n)
    if len(D) == 2:
        print(*D)

