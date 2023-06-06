def f(N):
    res = bin(N)[2:]
    if N % 2 == 0:
        res += '10'
    else:
        res = '1' + res + '01'
    return int(res, 2)

for N in range(1, 9):
    print(f(N))