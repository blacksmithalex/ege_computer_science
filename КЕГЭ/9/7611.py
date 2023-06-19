file = open('7611.txt')
count = 0
for line in file:
    a = sorted([int(x) for x in line.split()])
    if len(set(a)) == 5:
        s1 = 2 * (max(a) + min(a))
        s2 = sum(a) - max(a) - min(a)
        if s1 >= s2:
            count += 1
print(count)
