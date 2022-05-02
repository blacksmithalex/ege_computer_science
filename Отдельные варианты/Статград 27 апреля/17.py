def isFit(a, b, c, avg):
    if len(set([a % 3, b % 3, c % 3])) != 3:
        return False
    res = [a < avg, b < avg, c < avg]
    if res.count(True) == 1:
        return True
    else:
        return False

file = open('17.txt')
a = [int(x) for x in file]
file.close()
S1, count1 = 0, 0
for x in a:
    if x % 2 == 1:
        S1 += x
        count1 += 1
avg = S1 / count1

count = 0
maxS = 0

for i in range(len(a) - 2):
    if isFit(a[i], a[i + 1], a[i + 2], avg):
        count += 1
        if a[i] + a[i + 1] + a[i + 2] > maxS:
            maxS = a[i] + a[i + 1] + a[i + 2]
print(count, maxS)

#Ответ: 792 25092

