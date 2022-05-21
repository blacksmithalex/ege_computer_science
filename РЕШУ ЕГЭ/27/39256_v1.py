file = open('27-A.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

maxS = 0
for i in range(N):
    for j in range(i, N):
        subseq = a[i:j + 1]
        count1 = 0
        for x in subseq:
            if x % 2 != 0:
                count1 += 1
        if count1 % 10 == 0 and sum(subseq) > maxS:
            maxS = sum(subseq)
print(maxS)





