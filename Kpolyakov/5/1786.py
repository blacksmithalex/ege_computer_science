def f(N):
    if N % 2 == 0:
        return int(bin(N)[2:] + '01', 2)
    else:
        return int(bin(N)[2:] + '10', 2)

for N in range(1, 100):
    if f(N) > 73:
        print(N)
        break


