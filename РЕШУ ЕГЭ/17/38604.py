file = open('17.txt')
a = [int(x) for x in file]
file.close()
count, ms = 0, 0
for i in range(len(a) - 1):
        if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
            count += 1
            ms = max(ms, a[i] + a[i + 1])
print(count, ms)