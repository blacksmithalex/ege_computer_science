file = open('26.txt')
N, M = [int(x) for x in file.readline().split()]
a, b = [], []
for _ in range(N):
    price, type = file.readline().split()
    if type == 'A':
        a.append(int(price))
    else:
        b.append(int(price))
file.close()
a, b = sorted(a), sorted(b)
S, i, j = 0, 0, 0
while i < len(a) and j < len(b):
    if S + a[i] > M and S + b[j] > M:
        break
    if a[i] <= b[j]:
        if S + a[i] <= M:
            S += a[i]
            i += 1
    else:
        if S + b[j] <= M:
            S += b[j]
            j += 1
if i == len(a):
    while j < len(b):
        if S + b[j] <= M:
            S += b[j]
            j += 1
        else: break
if j == len(b):
    while i < len(a):
        if S + a[i] <= M:
            S += a[i]
            i += 1
        else: break

j -= 1
while j >= 0 and i < len(a):
    if S - b[j] + a[i] <= M:
        S = S - b[j] + a[i]
        i += 1
        j -= 1
    else: break

print(i, M - S)