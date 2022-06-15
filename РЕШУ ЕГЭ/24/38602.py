file = open('24.txt')
a = file.readline()
file.close()

c1, c2 = '', ''
count, countm = 0, 0
for x in a:
    c1, c2 = c2, x
    if c1 == 'P' and c2 == 'P':
        if count > countm:
            countm = count
        count = 1
    else:
        count += 1
        if count > countm:
            countm = count
print(countm)
