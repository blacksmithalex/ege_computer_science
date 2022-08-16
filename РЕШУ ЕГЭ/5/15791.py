def f(N):
    N = bin(N)[2:]
    for _ in range(2):
        last = sum([int(x) for x in N]) % 2
        N += str(last)
    return int(N, 2)

for N in range(1, 100):
    if f(N) > 97:
        print(f(N))
        break