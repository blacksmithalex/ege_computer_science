file = open('26.txt')
N = int(file.readline())
a = set([int(i) for i in file])
nechet = []
for x in a:
    if x % 2 != 0:
        nechet.append(x)

count, Mavg = 0, 0
for i in range(len(nechet)):
    for j in range(i + 1, len(nechet)):
        avg = (nechet[i] + nechet[j]) // 2
        if avg in a:
            count += 1
            if avg > Mavg:
                Mavg = avg
print(count, Mavg)


