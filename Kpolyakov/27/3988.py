file = open('27-65a.txt')
N = int(file.readline())
a = []
for _ in range(N):
    f, s = [int(x) for x in file.readline().split()]
    if s % 2 != 0:
        a.append([f, s])
N = len(a)
file.close()
var = ['0', '1']
for _ in range(1, N):
    res = []
    for v in var:
        res.append(v + '0')
        res.append(v + '1')
    var = res

S = 0
for v in var:
    Smin, Smax = 0, 0
    for i in range(N):
        if int(v[i]) == 1:
            Smin += min(a[i])
            Smax += max(a[i])
    if Smax % 2 == 0 and Smin % 2 != 0 and Smin + Smax > S:
        S = Smin + Smax

print(S)

