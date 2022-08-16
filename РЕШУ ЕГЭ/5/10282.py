def f(N):
    s1 = int(str(N)[0]) + int(str(N)[2]) + int(str(N)[4])
    s2 = int(str(N)[1]) + int(str(N)[3])
    if s1 > s2:
        return int(str(s2) + str(s1))
    else:
        return int(str(s1)+ str(s2))

for N in range (10000, 99999):
    if f(N) == 723:
        print(N)