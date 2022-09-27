def f(N):
    Nb = bin(N)[2:]
    num = [str((int(x) + 1) % 2) for x in Nb]
    newN = int(''.join(num), 2)
    return N - newN

for N in range(128, 256):
    if f(N) == 105:
        print(N)

