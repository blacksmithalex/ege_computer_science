def L(a, rule):
    count, countm = 0, 0
    for x in a:
        if (x == rule[0] and count % 3 == 0) or (x == rule[1] and count % 3 == 1) or (x == rule[2] and count % 3 == 2):
            count += 1
            if count > countm:
                countm = count
        elif x == rule[0]:
            count = 1
        else:
            count = 0
    return countm

countm = 0
file = open('24-171.txt')
for a in file:
    countm = max(L(a, 'XYZ'), L(a, 'YZX'), L(a, 'ZXY'), countm)
print(countm)