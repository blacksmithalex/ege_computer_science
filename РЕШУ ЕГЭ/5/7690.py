def f(N):
    s1 = int(str(N)[0]) + int(str(N)[1])
    s2 = int(str(N)[1]) + int(str(N)[2])
    if s1 > s2:
        return int(str(s1) + str(s2))
    else:
        return int(str(s2) + str(s1))

for N in range(100, 1000):
    if f(N) == 157:
        print(N)

