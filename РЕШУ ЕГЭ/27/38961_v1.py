file = open('27-A.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

Smax = 0
for i in range(N):
    for j in range(i, N):
        subseq = a[i:j + 1]
        count0 = 0
        for x in subseq:
            if x % 2 == 0:
                count0 += 1
        if count0 % 10 == 0 and sum(subseq) > Smax:
            Smax = sum(subseq)

print(Smax)

