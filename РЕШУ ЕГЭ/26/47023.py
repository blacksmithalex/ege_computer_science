mpix = 10000
disp = [[0] * (mpix + 1) for _ in range(mpix + 1)]
file = open('26.txt')
n = int(file.readline())
for _ in range(n):
    xi, yi = [int(x) for x in file.readline().split()]
    disp[xi][yi] = 1
file.close()

countm, mi = 0, 0
for i in range(1, mpix + 1):
    count = 1
    inds = [j for j in range(1, mpix + 1) if disp[i][j] == 1]
    for j in range(len(inds) - 1):
        if inds[j + 1] - inds[j] == 2:
            count += 1
            if count > countm:
                countm = count
                mi = i
        else:
            count = 1
print(countm, mi)







