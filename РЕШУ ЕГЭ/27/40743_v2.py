file = open('27-B.txt')
n = int(file.readline())
a = [int(x) for x in file]
file.close()

R = [None] * 30
S, Smax, count2 = 0, 0, 0
for x in a:
    S += x
    if x > 0 and x % 2 == 0:
        count2 += 1
    if count2 % 30 == 0:
        Smax = max(Smax, S)
        if R[0] is not None:
            Smax = max(Smax, S - R[0])
            R[0] = min(R[0], S)
        else:
            R[0] = S
    else:
        r = count2 % 30
        if R[r] is not None:
            newS = S - R[r]
            Smax = max(Smax, newS)
            R[r] = min(R[r], S)
        else:
            R[r] = S
print(Smax)





