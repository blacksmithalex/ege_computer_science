file = open('27_B.txt')
n = int(file.readline())

R, L = [None] * 43, [None] * 43
Smax, Lmax = 0, 0
s, l = 0, 0
for _ in range(n):
    x = int(file.readline())
    s, l = s + x, l + 1
    if s % 43 == 0:
        Smax, Lmax = s, l
    else:
        r = s % 43
        if R[r] is None:
            R[r] = s
            L[r] = l
        else:
            news = s - R[r]
            newl = l - L[r]
            if news > Smax:
                Smax, Lmax = news, newl
            elif news == Smax and newl < Lmax:
                Lmax = newl
print(Lmax)

