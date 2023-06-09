file = open('27B.txt')
N = int(file.readline())
K = int(file.readline())
a = [int(x) for x in file]
file.close()

ms = [0] * N
lastmax = 0
for i in range(N):
    if a[i] > lastmax:
        lastmax = a[i]
    ms[i] = lastmax
sm = 0
for i in range(K, N):
    sm = max(sm, a[i] + ms[i - K])
print(sm)

