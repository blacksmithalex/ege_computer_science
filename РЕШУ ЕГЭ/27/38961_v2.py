file = open('27-B.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()
k = 10
R = [None] * k
S, Smax, count2 = 0, 0, 0
for x in a:
    S += x
    if x % 2 == 0:
        count2 += 1
    r = count2 % k
    if r == 0:
        Smax = S
    else:
        if R[r] is None:
            R[r] = S
        else:
            newS = S - R[r]
            Smax = max(Smax, newS)
print(Smax)

