file = open('24-j8.txt')
a = file.readline()
file.close()

count, countm = 1, 1
for i in range(len(a) - 1):
    if int(a[i]) + int(a[i + 1]) >= 10:
        count += 1
        if count > countm:
            countm = count
    else:
        count = 1

print(countm)


