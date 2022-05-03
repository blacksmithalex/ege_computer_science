file = open('test.txt')
n = int(file.readline())
count0 = 0
a = []
for _ in range(n):
    r = int(file.readline())
    if r % 3 == 0:
        count0 += 1
    else:
        a.append(r)
file.close()
n = len(a)
R0 = 2**count0 - 1

var = ['0', '1']
for _ in range(1, n):
    prev = var
    res = []
    for x in prev:
        res.append(x + '0')
        res.append(x + '1')
    var = res

var = var[1:]
R1 = 0
for v in var:
    S = 0
    for i in range(n):
        if int(v[i]) == 0:
            continue
        S += a[i]
    if S % 3 == 0:
        R1 += 1

print(R0 + R1 + R0 * R1)