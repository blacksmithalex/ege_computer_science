file = open('27_B.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

R, Rlens,= [None] * 89, [None] * 89
S, Smax, l, lmax = 0, 0, 0, 68000
for x in a:
    S += x
    l += 1
    if S % 89 == 0:
        Smax, lmax = S, l
    else:
        if R[S % 89] is None:
            R[S % 89] = S
            Rlens[S % 89] = l
        else:
            newS, newl = S - R[S % 89], l - Rlens[S % 89]
            if newS > Smax:
                Smax, lmax = newS, newl
            elif newS == Smax and newl < lmax:
                lmax = newl
print(lmax)


