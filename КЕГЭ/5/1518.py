def f(N):
    bN = bin(N)[2:]
    bN += bN[-2]
    bN += bN[1]
    return int(bN, 2)

for N in range(2, 100):
    if f(N) > 100:
        print(N)
        break
