file = open('9_4697.txt')
count = 0
for line in file:
    a = [int(x) for x in line.split()]
    if len(set(a)) == 5:
        a1 = [] #не повт.
        a2 = [] #повт.
        for x in a:
            if a.count(x) == 1:
                a1.append(x)
            else:
                a2.append(x)
        s1 = sum(a1) / len(a1)
        if s1 <= sum(a2):
            count += 1
print(count)

