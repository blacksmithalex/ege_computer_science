a = [int(x) for x in open('17.txt')]
count = 0
maxS = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] * a[j] % 10 == 0:
            count += 1
            if a[i] + a[j] > maxS:
                maxS = a[i] + a[j]
print(count,maxS)