file = open('27-A_demo.txt')
S = 0
dmin = 10000
N = int(file.readline())
for _ in range(N):
    a, b = sorted([int(x) for x in file.readline().split()])
    S += b
    if (b - a) % 3 != 0 and (b - a) < dmin:
        dmin = b - a

if S % 3 != 0:
    print(S)
else:
    print(S - dmin)