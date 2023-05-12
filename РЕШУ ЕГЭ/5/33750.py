def f(N):
    bN = bin(N)[2:]
    bN = bN[:-1] + bN[1] * 2
    return int(bN, 2)

for N in range(2, 100):
    if f(N) > 76:
        print(N)
        break