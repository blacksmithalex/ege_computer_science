file = open('27-B.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

vars = [[0] * 9 for _ in range(9)]
res = 0
for j in range(N):
    for x in range(9):
        res += vars[x][(j - a[j] - x) % 9]
    vars[a[j] % 9][j % 9] += 1
print(res)

