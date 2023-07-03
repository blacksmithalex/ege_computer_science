def f(N, d):
    digits = []
    while N != 0:
        digits.append(N % d)
        N //= d
    return digits[::-1]

N = 7 * 5**1984 - 6 * 25**777 + 5 * 125**333 - 4
N5 = f(N, 5)
print(sum(N5))