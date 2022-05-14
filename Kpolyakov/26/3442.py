def solve(a, S):
    a = sorted(a)
    M, maxi = 0, 0
    for i in range(len(a)):
        if M + a[i] <= S:
            M += a[i]
            maxi = i
    t = a[maxi]
    for i in range(maxi + 1, len(a)):
        if M - t + a[i] <= S:
            M = M - t + a[i]
            t = a[i]
    return maxi + 1, t

file = open('26-j10.txt')
memD, memE, N = [int(x) for x in file.readline().split()]
D, E = [], []
for _ in range(N):
    f = int(file.readline())
    if f > 500:
        D.append(f)
    else:
        E.append(f)
file.close()
countD, maxD = solve(D, memD)
countE, maxE = solve(E, memE)

print(countD + countE, maxD + maxE)
