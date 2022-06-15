file = open('27-72b.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

R = [None] * 71
S, count = 0, 0
for x in a:
    S += x
    r = S % 71
    if S % 71 == 0:
        count += 1
    if R[r] is None:
        R[r] = 1
    else:
        count += R[r]
        R[r] += 1

print(count)
