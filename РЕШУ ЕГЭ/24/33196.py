file = open('24.txt')
a = file.readline()
file.close()

d = {}
for i in range(len(a) - 1):
    if a[i] == 'A':
        if a[i + 1] in d:
            d[a[i + 1]] += 1
        else:
            d[a[i + 1]] = 1
print(d)




