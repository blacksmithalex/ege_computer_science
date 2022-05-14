file = open('24-j5.txt')
a = file.readline()
file.close()

count, countm = 0, 0
for x in a:
    if (x == 'K' and count % 3 == 0) or (x == 'O' and count % 3 == 1) or (x == 'T' and count % 3 == 2):
        count += 1
        if count > countm:
            countm = count
    elif x == 'K':
        count = 1
    else:
        count = 0

print(countm // 3)


