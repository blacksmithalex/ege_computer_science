file = open('28128_B.txt')
N = int(file.readline())
a = sorted([int(x) for x in file], reverse=True)
file.close()

Msum = 0
for i in range(N):
    for j in range(i + 1, N):
        s = a[i] + a[j]
        if s % 3 == 0 and s > Msum:
            Msum = s
            print(Msum)