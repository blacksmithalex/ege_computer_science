file = open('27-B.txt')
INF = 1e8
N = int(file.readline())
r0, r1, r2 = [INF] * 3, [INF] * 3, [INF] * 3
for _ in range(N):
    num = int(file.readline())
    if num % 3 == 0:
        r0 = sorted(r0 + [num])[:-1]
    elif num % 3 == 1:
        r1 = sorted(r1 + [num])[:-1]
    else:
        r2 = sorted(r2 + [num])[:-1]

print(min(sum(r0), sum(r1), sum(r2), r0[0] + r1[0] + r2[0]))
