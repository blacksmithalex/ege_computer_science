file = open('17.txt')
a = [int(x) for x in file]
file.close()

count, sm = 0, 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i] % 19 == 0 or a[j] % 19 == 0):
            count += 1
            if (a[i] + a[j]) > sm:
                sm = a[i] + a[j]
print(count, sm)
