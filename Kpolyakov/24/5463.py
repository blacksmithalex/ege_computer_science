file = open('24-223.txt')
a = file.readline()
file.close()

a = a.replace('CACAC', 'CAC CAC')
a = a.replace('AB', 'X')
a = a.replace('CAC', 'Y')

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 2
        if count > countm:
            countm = count
    elif x == 'Y':
        count += 3
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)


