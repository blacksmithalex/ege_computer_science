file = open('27-A_2.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

X = 0
for i in range(N):
    for j in range(i + 1, N):
        p = a[i] * a[j]
        if p % 14 == 0:
            X = max(X, p)
print(X)