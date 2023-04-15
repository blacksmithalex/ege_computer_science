file = open('24-153.txt')
a = file.readline()
file.close()
indsA, indsF = [], []

for i in range(len(a)):
    if a[i] == 'A':
        indsA.append(i)
    elif a[i] == 'F':
        indsF.append(i)

lmin = 10**6
n, m = len(indsA), len(indsF)
for i in range(n):
    for j in range(m):
        if indsF[j] > indsA[i]:
            l = indsF[j]  - indsA[i] + 1
            if l != 2 and l < lmin:
                lmin = l
                print(lmin)

