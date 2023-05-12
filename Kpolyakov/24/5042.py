file = open('24-197.txt')
a = file.readline()
file.close()

vars = ['XXХ', 'XYX', 'XZX', 'YXY', 'YYY', 'YZY']
for v in vars:
    a = a.replace(v, 'W')
count, countm = 0, 0
for x in a:
    if x == 'W':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)
