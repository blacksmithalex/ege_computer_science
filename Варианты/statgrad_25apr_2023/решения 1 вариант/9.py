list = []

for line in file:
    list.append(line.split())

count = 0
for i in list:
    mx = max(int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]))
    srednee = (int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]) + int(i[4]) + int(i[5]) - mx) /5
    if i.count(str(mx)) == 1 and len(set(i)) <= 5 and (srednee * 3) < mx:
        count += 1
print(count)