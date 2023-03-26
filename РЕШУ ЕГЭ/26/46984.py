size = 10000
pix = [[0] * (size + 1) for _ in range(size + 1)]
file = open('26.txt')
N = int(file.readline())
for _ in range(N):
    row, num = [int(x) for x in file.readline().split()]
    pix[row][num] = 1
file.close()

mrow, countm = 0, 0
for row in range(1, size + 1):
    count = 0
    elems = pix[row]
    for p in elems:
        if p == 1:
            count += 1
            if count > countm:
                countm = count
                mrow = row
        else:
            count = 0
print(countm, mrow)
