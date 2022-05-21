file = open('27-A-2.txt')
N = int(file.readline())
a = [[int(x) for x in line.split()] for line in file]
file.close()
var = ['0', '1']
for _ in range(1, N):
    res = []
    for v in var:
        res.append(v + '0')
        res.append(v + '1')
    var = res
print(var[:5])
Smax = 0
for v in var:
    S, count0, count1 = 0, 0, 0
    for i in range(N):
        num = a[i][int(v[i])]
        S += num
        if num % 2 == 0:
            count0 += 1
        else:
            count1 += 1
    if S % 2 == 0 and count0 >= count1 and S > Smax:
        Smax = S
    elif S % 2 !=0 and count1 >= count0 and S > Smax:
        Smax = S
print(Smax)


