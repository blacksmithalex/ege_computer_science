file = open('27-B-2.txt')
n = int(file.readline())
sum = 0
dif1, dif2, dif3, dif4 = 1e16, 1e16, 1e16, 1e16
count0, count1 = 0, 0
for _ in range(n):
    y, x = sorted([int(x) for x in file.readline().split()])
    sum += x
    if x % 2 == 0:
        count0 += 1
    else:
        count1 += 1
    if x % 2 != y % 2:
        if x - y < dif1 and x % 2 != 0:
            dif2 = dif1
            dif1 = x - y
        elif x - y < dif2 and x % 2 != 0:
            dif2 = x - y
        if x - y < dif3 and x % 2 == 0:
                dif4 = dif3
                dif3 = x - y
        elif x - y < dif4 and x % 2 == 0:
                dif4 = x - y

if count1 > count0:
    if sum % 2 == 1:
        print(sum)
    elif dif3 <= dif1:
        print(sum - dif3)
    elif count1 - count0 != 1:
        print(sum - dif1)
    elif (dif1 + dif2) < dif3:
        print(sum - dif1 - dif2)
    else:
        print(sum - dif3)
else:
    if sum % 2 == 0:
        print(sum)
    elif dif1 <= dif3:
        print(sum - dif1)
    elif (count0 - count1) != 1:
        print(sum - dif3)
    elif (dif3 + dif4) < dif1:
        print(sum - dif3 - dif4)
    else:
        print(sum - dif1)
