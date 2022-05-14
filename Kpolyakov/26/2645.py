file = open('26-j3.txt')
S, N = [int(x) for x in file.readline().split()]
a = [int(x) for x in file]
file.close()
a = sorted(a, reverse=True)

M, count = 0, 0
for i in range(len(a)):
    if M + a[i] <= S:
        M += a[i]
        count += 1
        maxi = i
print(count, a[maxi])
