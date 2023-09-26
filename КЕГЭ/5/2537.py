def f(N):
    s1, s2 = 0, 0
    sN = str(N)
    for x in str(sN):
        if int(x) % 2 == 0:
            s1 += int(x)
    for i in range(1, len(sN), 2):
        s2 += int(sN[i])
    return abs(s1 - s2)

for N in range(2, 1000):
    if f(N) == 13:
        print(N)
        break

