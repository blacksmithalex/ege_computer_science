file = open('27-A.txt')
n = int(file.readline())
a = [int(x) for x in file]
file.close()

smax = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        subseq = a[i: j + 1]
        count2 = 0
        for x in subseq:
            if x > 2 and x % 2 == 0:
                count2 += 1
        if count2 % 30 == 0:
            smax = max(smax, sum(subseq))
print(smax)

