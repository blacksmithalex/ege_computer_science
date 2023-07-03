f = open('27-A.txt')
n = f.readline()
a = [int(x) for x in f.readlines()]
k = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 9 == abs(i - j) % 9:
            k += 1
print(k)