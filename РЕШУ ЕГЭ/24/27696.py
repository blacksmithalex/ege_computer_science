file = open('zadanie24_2.txt')
a = file.readline()
file.close()

count, countm = 0, 0
for x in a:
    if x == 'L':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)