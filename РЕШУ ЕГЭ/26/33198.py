file = open('26.txt')
N, M = [int(i) for i in file.readline().split()]
S, count, a, = 0, 0, []

for _ in range(N):
    w = int(file.readline())
    if 200 <= w <= 210:
        S += w
        count += 1
    else:
        a.append(w)
file.close()
a, N, maxi = sorted(a), len(a), 0

for i in range(N):
    if S + a[i] <= M:
        S += a[i]
        count += 1
        maxi = i

for i in range(maxi, -1, -1):
    for j in range(maxi + 1, N):
        if S - a[i] + a[j] <= M:
            S = S - a[i] + a[j]
            a[i], a[j] = a[j], a[i]

print(count, S)