file = open('107_24.txt')
a = file.readline()
file.close()

count, countm = 0, 0
for x in a:
    if ((x == 'A' or x == 'C') and count % 2 == 0) or (x == 'B' and count % 2 == 1):
        count += 1
        if count > countm:
            countm = count
    elif x == 'A' or x == 'C':
        count = 1
    else:
        count = 0

print(countm // 2)