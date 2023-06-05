file = open('27-B.txt')
n = int(file.readline())
a = sorted([int(x) for x in file], reverse=True)

smax = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            s = a[i] + a[j] + a[k]
            if s % 3 == 0 and s > smax:
                smax = s
                print(smax)