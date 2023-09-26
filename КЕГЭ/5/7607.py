def f(N):
    bN = bin(N)[2:]
    if N % 3 == 0:
        bN += bN[-3:]
    else:
        r = bin((N % 3) * 3)[2:]
        bN += r
    return int(bN, 2)

for N in range(4, 100):
    if f(N) > 76:
        print(N)
        break
