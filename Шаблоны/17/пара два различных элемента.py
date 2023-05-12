file = open('17.txt')
a = [int(x) for x in file]
file.close()

count, sm = 0, 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 2 != 0 and (a[i] * a[j]) % 3 == 0:
            count += 1
            sm = max(sm, a[i] + a[j])
print(count, sm)

