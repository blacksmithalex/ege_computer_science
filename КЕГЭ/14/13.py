def f(N, d):
    digits = []
    while N != 0:
        digits.append(N % d)
        N //= d
    return digits[::-1]

N = 49**7 + 7**21 - 7
N7 = f(N, 7)
print(N7.count(6))
