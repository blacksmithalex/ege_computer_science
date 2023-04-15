file = open('27-B_demo.txt')
S, dmin = 0, 10000
n = int(file.readline())
for _ in range(n):
    a, b = sorted([int(x) for x in file.readline().split()])
    S += a
    d = b - a
    if d % 3 != 0 and d < dmin:
        dmin = d
if S % 3 != 0:
    print(S)
else:
    print(S + d)

