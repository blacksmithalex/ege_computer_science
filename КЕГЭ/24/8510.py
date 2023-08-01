file = open('24_8510.txt')
a = file.readline()
file.close()
count, countm = 1, 1
for i in range(len(a) - 1):
    if not (a[i] in 'NOP' and a[i + 1] in 'NOP'):
        count += 1
        if count > countm:
            countm = count
    else:
        count = 1
print(countm)