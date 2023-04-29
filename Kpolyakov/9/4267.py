from math import sqrt
file = open('9-103.txt')
mdist = 0
for line in file:
    x, y = [int(x) for x in line.split()]
    dist = sqrt((x + 20)**2 + (y + 20)**2)
    mdist = max(mdist, dist)
print(int(mdist))