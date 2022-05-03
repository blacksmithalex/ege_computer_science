file = open('24_demo.txt')
a = file.readline()
file.close()

count, countm = 0, 0
for x in a:
    if (x == 'X' and count % 3 == 0) or (x == 'Y' and count % 3 == 1) or (x == 'Z' and count % 3 == 2):
        count += 1
        if count > countm:
            countm = count
    elif x == 'X':
        count = 1
    else:
        count = 0

print(countm)
