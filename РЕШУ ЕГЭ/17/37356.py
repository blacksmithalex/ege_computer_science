file = open('17.txt')
a = [int(x) for x in file]
file.close()

count, ms = 0, 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        s = a[i] + a[j]
        if s % 9 == 0:
            count += 1
            if s > ms:
                ms = s
print(count, ms)