file = open('zadanie24_1.txt')
a = file.readline()
file.close()
count, mcount = 0, 0
for x in a:
    if x == 'A':
        count += 1
        if count > mcount:
            mcount = count
    else:
        count = 0
print(mcount)