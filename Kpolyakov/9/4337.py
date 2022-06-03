file = open('test.txt')
count = 0
for line in file:
    a, b, c, d = sorted([int(x) for x in line.split()])
    if d < a + b + c:
        count += 1
print(count)