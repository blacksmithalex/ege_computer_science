file = open('24_105.txt')
a = file.readline()
file.close()

for letter in 'FAIL':
    count, countm = 0, 0
    for x in a:
        if x == letter:
            count += 1
            if count > countm:
                countm = count
        else:
            count = 0
    print(countm)
