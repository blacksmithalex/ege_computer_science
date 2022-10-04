file = open('17.txt')
N = 10000
a = [int(x) for x in file]
file.close()

count62, M62 = 0, 0
for i in range(N):
    for j in range(i + 1, N):
        if (a[i] * a[j]) % 62 == 0:
            count62 += 1
            M62 = max(a[i] + a[j], M62)
print(count62, M62)



