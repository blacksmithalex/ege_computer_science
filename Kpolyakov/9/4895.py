file = open('9.txt')
count = 0
for line in file:
    d1, d2 = [int(x) for x in line.split()]
    S = d1 * d2 / 2
    if S == 48:
        count += 1
print(count)