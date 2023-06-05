file = open('inf_22_10_20_27a.txt')
n = int(file.readline())
S = 0
d1, d2 = [], []
for _ in range(n):
    a, b = sorted([int(x) for x in file.readline().split()])
    S += b
    d = b - a
    if d % 3 == 1:
        d1 = sorted(d1 + [d])[:2]
    elif d % 3 == 2:
        d2 = sorted(d2 + [d])[:2]

if S % 3 == 0:
    print(S)
elif S % 3 == 1:
    print(max(S - d1[0], S - d2[0] - d2[1]))
else:
    print(max(S - d2[0], S - d1[0] - d1[1]))
