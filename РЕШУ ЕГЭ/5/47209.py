def f(N):
    N = bin(N)[2:]
    S = sum([int(x) for x in N])
    if S % 2 == 0:
        N = '10' + N[2:] + '0'
    else:
        N = '11' + N[2:] + '1'
    return int(N, 2)

for N in range(1, 100):
    R = f(N)
    if R > 40:
        print(N, R)
        break

