file = open('zadanie24_1.txt')
a = file.readline()
file.close()

count, countm = 1, 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        count += 1
        if count > countm:
            countm = count
    else:
        count = 1
print(countm)