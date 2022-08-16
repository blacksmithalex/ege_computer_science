def f(N):
    res = bin(N)[2:]
    if N % 2 == 0:
        res += '00'
    else:
        res += '11'
    return int(res, 2)

for N in range(1, 100):
    if f(N) < 94:
        print(N)


