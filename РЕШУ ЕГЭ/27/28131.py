file = open('28131_B.txt')
n = int(file.readline())
a = [int(x) for x in file]
file.close()
m = 120
R = [0] * m
ms = 0
ms1, ms2 = 0, 0
for j in range(n):
    rj = a[j] % m
    ri = (m - rj) % m
    if R[ri] != 0 and R[ri] < a[j]:
        if R[ri] + a[j] > ms:
            ms =  R[ri] + a[j]
            ms1 = R[ri]
            ms2 = R[rj]
    R[rj] = max(R[rj], a[j])
print(ms)
print(ms1, ms2)

