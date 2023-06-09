file = open('27A.txt')
N = int(file.readline())
K = int(file.readline())
a = [int(x) for x in file]
file.close()

sm = 0
for i in range(N):
    for j in range(i + K, N):
        sm = max(sm, a[i] + a[j])

print(sm)