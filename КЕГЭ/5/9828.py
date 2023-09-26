def to3(N):
    res = ''
    while N != 0:
        res += str(N % 3)
        N //= 3
    return res[::-1]
def f(N):
    tN = to3(N)
    if N % 3 == 0:
        tN = '1' + tN + '02'
    else:
        r = to3((N % 3) * 4)
        tN += r
    return int(tN, 3)

for N in range(1, 600):
    if f(N) < 199:
        print(N)

