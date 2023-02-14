file = open('test.txt')
count = 0
for line in file:
    angles = [int(x) for x in line.split()]
    if max(angles) < 180:
        if (angles[0] + angles[2] == 180) and (angles[1] + angles[3] == 180):
            count += 1
print(count)

