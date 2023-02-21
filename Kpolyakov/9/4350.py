file = open('test.txt')
count = 0
for line in file:
    a, b, c = sorted([int(x) for x in line.split()])
    qs = [b / a, c / b]
    if qs[0] == qs[1] and qs[0] != 1:
        count += 1
print(count)