def f(N):
    N = bin(N)[2:]
    for _ in range(2):
        N += str(sum([int(x) for x in N]) % 2)
    return int(N, 2)

for N in range(1, 100):
    R = f(N)
    if R > 43:
        print(R)
        break

