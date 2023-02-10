file = open('24.txt')
a = file.readline()
file.close()

a = a.replace('CA', 'X')
a = a.replace('DA', 'X')
a = a.replace('FA', 'X')
a = a.replace('CO', 'X')
a = a.replace('DO', 'X')
a = a.replace('FO', 'X')

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)
