def R(N):
    N -= N % 4
    N = bin(N)[2:]
    for _ in range(2):
        N += str(sum([int(x) for x in N]) % 2)
    return int(N, 2)

for N in range(1, 100):
    if R(N) > 56:
        print(R(N))
        break
