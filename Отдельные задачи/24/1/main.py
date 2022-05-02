file = open('24 варианты 1-4.txt')
a = file.readline()
file.close()
l, maxl = 0, 0

c1, c2 = '', ''
for x in a:
    c1, c2 = c2, x
    if (c1 == '1' and c2 == '2') or (c1 == '2' and c2 == '1') or (c1 == '1' and c2 == '3') or (c1 == '3' and c2 == '1'):
        if l > maxl:
            maxl = l
        l = 1
    else:
        l += 1
        if l > maxl:
            maxl = l
print(maxl)