file = open('test.txt')
count = 0
for line in file:
    a, b, c = sorted([int(x) for x in line.split()])
    if (c**2 > a**2 + b**2) and (a + b > c):
        count += 1
print(count)
