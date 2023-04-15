a = 'XXYZXXXXYYZZXXX'

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)


