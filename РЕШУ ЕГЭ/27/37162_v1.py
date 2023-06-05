file = open('27_A.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

smax, lmax = 0, 0
for i in range(N):
    for j in range(i, N):
        subseq = a[i:j + 1]
        s = sum(subseq)
        l = len(subseq)
        if s % 89 == 0:
            if s > smax:
                smax, lmax = s, l
            elif s == smax and l < lmax:
                lmax = l
print(lmax)