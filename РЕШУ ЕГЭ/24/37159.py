file = open('24.txt')
a = file.readline()
file.close()
l, maxl = 0, 0

c1, c2 = '', ''
for x in a:
    c1, c2 = c2, x
    if (c1 == 'a' and c2 == 'd') or (c1 == 'd' and c2 == 'a'):
        if l > maxl:
            maxl = l
        l = 1
    else:
        l += 1
        if l > maxl:
            maxl = l
print(maxl)