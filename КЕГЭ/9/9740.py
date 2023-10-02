file = open('9_9740.txt')
count = 0
for line in file:
    line = [int(x) for x in line.split()]
    freq1 = []
    freq3 = []
    for x in line:
        if line.count(x) == 1:
            freq1.append(x)
        elif line.count(x) == 3:
            freq3.append(x)
    if len(freq1) == 4 and len(freq3) == 3:
        avg1 = sum(freq1) / 4
        avg3 = sum(freq3) / 3
        if avg1 <= avg3:
            count += 1
print(count)