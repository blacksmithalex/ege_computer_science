file = open('26-46.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()
alls = set(a)

count = 0
m = 10e9
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = a[i] + a[j] + a[k]
            if s % 3 == 0 and s // 3 in alls:
                count += 1
                if s // 3 < m:
                    m = s // 3
print(count, m)
