def f(N):
    N = bin(N)[2:]
    sdigits = N.count('1')
    if sdigits % 2 == 0:
        N = '10' + N[2:] + '0'
    else:
        N = '11' + N[2:] + '1'
    return int(N, 2)

for N in range(1, 100):
    R = f(N)
    if R < 35:
        print(N, R)
