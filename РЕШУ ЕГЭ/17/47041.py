file = open('17-2.txt')
a = [int(x) for x in file]
file.close()

s1, count1 = 0, 0
for x in a:
    if x % 2 != 0:
        s1 += x
        count1 += 1
avg = s1 / count1

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = a[i] % 5 == 0 and a[i + 1] < avg
    l2 = a[i] < avg and a[i + 1] % 5 == 0
    if l1 or l2:
        count += 1
        if a[i] + a[i + 1] > sm:
            sm = a[i] + a[i + 1]
print(count, sm)