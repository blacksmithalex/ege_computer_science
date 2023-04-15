file = open('24-153.txt')
a = file.readline()
file.close()

INF = 10 ** 6
indA1 = -1
indA2 = -1
lmin = INF
for i in range(len(a)):
    if a[i] == 'A':
        if indA1 == -1 and indA2 == -1:
            indA1 = i
        elif indA1 != -1 and indA2 == -1:
            indA2 = i
        elif indA1 != -1 and indA2 != -1:
            indA1, indA2 = indA2, i
    if a[i] == 'F':
        l1, l2 = INF, INF
        if indA2 != -1:
            l1, l2 = i - indA1 + 1, i - indA2 + 1
        elif indA1 != -1:
            l1 = i - indA1 + 1
        if l2 != 2:
            lmin = min(lmin, l2)
        if l1 != 2:
            lmin = min(lmin, l1)
        indA1, indA2 = -1, -1
print(lmin)

