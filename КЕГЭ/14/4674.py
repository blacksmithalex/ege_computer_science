def f(N, d):
    digits = []
    while N != 0:
        digits.append(N % d)
        N //= d
    return digits[::-1]

N = 216**1315 - 4 * 36**1502 + 5 * 36**1510 - 3 * 6**1331 - 253
N6 = f(N, 6)
print(N6.count(0))