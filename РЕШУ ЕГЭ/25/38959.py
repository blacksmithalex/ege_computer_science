from math import sqrt
def f(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    div.add(n)
    div = sorted(div)
    if len(div) < 5:
        return 0
    else:
        return div[0] * div[1] * div[2] * div[3] * div[4]

n = 200000000 + 1
count = 0
while count != 5:
    M = f(n)
    if 0 < M < n:
        print(M, n)
        count += 1
    n += 1