def f(N):
    N = bin(N)[2:]
    N = N[:-1] + N[1] * 2
    return int(N, 2)

for N in range(2, 100):
    if f(N) > 92:
        print(N)
        break


        