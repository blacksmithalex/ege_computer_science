res = []
for m in range(0, 30, 2):
    for n in range(1, 30, 2):
        N = 2 ** m * 5 ** n
        if 100000000 <= N <= 300000000:
            res.append([N, m + n])

for var in sorted(res):
    print(*var)

