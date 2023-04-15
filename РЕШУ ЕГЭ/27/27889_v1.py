from itertools import product
file = open('27-A_demo.txt')
n = int(file.readline())
pairs = [[int(x) for x in file.readline().split()] for _ in range(n)]
file.close()

sm = 10000 * n
for var in product('01', repeat = n):
    inds = [int(x) for x in var]
    s = 0
    for i in range(n):
        s += pairs[i][inds[i]]
    if s % 3 != 0:
        sm = min(sm, s)
print(sm)