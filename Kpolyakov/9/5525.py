file = open('9-170.txt')
count = 0
for line in file:
    line = sorted([int(x) for x in line.split()])
    if len(set(line)) == 6:
        avg = sum(line) / 6
        mid = (line[2] + line[3]) / 2
        if avg >= mid:
            count += 1
print(count)

