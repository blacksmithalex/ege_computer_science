file = open('24.txt')
a = file.readline()
file.close()

count = 0
countE = 0
countm = 0
for x in a:
    if x == 'A':
        if countE >= 3 and count > countm:
            countm = count
        count = 0
        countE = 0
    else:
        count += 1
        if x == 'E':
            countE += 1
        if countE >= 3 and count > countm:
            countm = count
print(countm)


