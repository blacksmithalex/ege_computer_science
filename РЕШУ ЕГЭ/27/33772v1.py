file = open('27-A.txt')
N = int(file.readline())
a = [[int(x) for x in line.split()] for line in file]
file.close()

var = ['0', '1']
for _ in range(1, N):
    res = []
    for x in var:
        res.append(x + '0')
        res.append(x + '1')
    var = res

Smin = 10000 * N
for v in var:
    S, count0, count1 = 0, 0, 0
    for i in range(N):
        ind = int(v[i])
        elem = a[i][ind]
        if elem % 2 == 0:
            count0 += 1
        else:
            count1 += 1
        S += elem
    if ((S % 2 == 0 and count0 >= count1) or (S % 2 != 0 and count1 >= count0)) and S < Smin:
        Smin = S
print(Smin)
