file = open('6898.txt')
count = 0
for line in file:
    a = sorted([int(x) for x in line.split()])
    l1 = a[3] < a[0] + a[1] + a[2]
    l2 = (a[0] + a[1]) == (a[2] + a[3])
    l3 = (a[0] + a[2]) == (a[1] + a[3])
    l4 = (a[0] + a[3]) == (a[1] + a[2])
    if l1 and (l2 or l3 or l4):
        count += 1
print(count)
