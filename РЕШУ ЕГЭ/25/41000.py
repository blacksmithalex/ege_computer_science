from math import sqrt
def f(N):
    div = {1}
    for d in range(2, int(sqrt(N)) + 1):
        if N % d == 0:
            div.add(d), div.add(N // d)
    div = sorted(div)
    if len(div) < 2:
        return 0
    return div[-2] + div[-1]

N = 11000000
count = 0
while count != 5:
    M = f(N)
    if 0 < M < 10000:
        print(M)
        count += 1
    N += 1
