file = open('1_27_B.txt')
K = int(file.readline())
N = int(file.readline())
a = [int(x) for x in file]

ms = [0] * N
lastmax = 0
for i in range(N):
    if a[i] > lastmax:
        lastmax = a[i]
    ms[i] = lastmax

ma = 0
for i in range(K, N):
    ma = max(ma, a[i] + ms[i - K])
print(ma)