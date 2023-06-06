file = open('9_8497.txt')
count = 0
for line in file:
    a = sorted([int(x) for x in line.split()])
    if len(set(a)) == 5:
        s1 = 3 * (min(a) + max(a))
        s2 = 2 * (sum(a) - min(a) - max(a))
        if s1 >= s2:
            count += 1
print(count)