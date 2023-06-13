from math import ceil
file = open('27_A-2.txt')
N = int(file.readline())
elems = []
for _ in range(N):
    x, num = [int(x) for x in file.readline().split()]
    num = ceil(num / 36)
    elems.append([x, num])ч
answers = [0] * N
leftsum = 0
rightsum = 0
for i in range(1, N):
    answers[0] += (elems[i][0] - elems[0][0]) * elems[i][1]
    rightsum += elems[i][1]
for i in range(1, N):
    leftsum += elems[i - 1][1]
    dist = elems[i][0] - elems[i - 1][0]
    answers[i] = answers[i - 1] - rightsum * dist + leftsum * dist
    rightsum -= elems[i][1]
print(min(answers))


