def Ml(a, l):
    count, countm = 0, 0
    for x in a:
        if x == l:
            count += 1
            if count > countm:
                countm = count
        else:
            count = 0
    return countm

s_Ml, l_Ml = '', 0
file = open('24-164.txt')
for line in file:
    letters = set(line)
    for l in letters:
        res = Ml(line, l)
        if res > l_Ml:
            s_Ml, l_Ml = line, res
file.close()

for l in sorted(set(s_Ml)):
    print(l, s_Ml.count(l))
print()
#Определяем, что z встречается чаще всего
file = open('24-164.txt')
count = 0
for line in file:
    count += line.count('Z')
print(count)