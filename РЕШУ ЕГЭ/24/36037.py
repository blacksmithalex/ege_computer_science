file = open('24.txt')
a = file.readline()
file.close()

c1, c2, c3, c4 = '', '', '', ''
count, countm = 0, 0
for x in a:
    c1, c2, c3, c4 = c2, c3, c4, x
    if c1 == 'X' and c2 == 'Z' and c3 == 'Z' and c4 == 'Y':
        if count > countm:
            countm = count
        count = 3
    else:
        count += 1
        if count > countm:
            countm = count
print(countm)
