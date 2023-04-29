def f(N):
    bN = bin(N)[2:]
    bN = bN[:-2]
    return int(bN, 2)

uniq = set()
for N in range(20, 600 + 1):
    uniq.add(f(N))
print(len(uniq))


