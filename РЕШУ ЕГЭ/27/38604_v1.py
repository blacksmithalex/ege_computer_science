file = open('27_A.txt')
n = int(file.readline())
a = [int(x) for x in file]
file.close()

Smax, Lmax = 0, 0
for i in range(n):
    for j in range(i, n):
        subseq = a[i:j + 1]
        S = sum(subseq)
        if S % 43 != 0:
            continue
        if S > Smax:
            Smax, Lmax = S, len(subseq)
        elif S == Smax and Lmax > len(subseq):
            Lmax = len(subseq)
print(Lmax)
