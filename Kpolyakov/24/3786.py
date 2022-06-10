def ml(a, l):
    count, countm = 0, 0
    for x in a:
        if x == l:
            count += 1
            if count > countm:
                countm = count
        else:
            count = 0
    return countm

file = open('24-164.txt')

mstr, mlen = '', 0
for line in file:
    letters = set(line)
    for l in letters:
        Res = ml(line, l)
        if Res > mlen:
            mstr, mlen = line, Res
file.close()

for l in sorted(set(mstr)):
    print(l, mstr.count(l))
print()
#Глазами определяем, что K встречается чаще всего (49 раз)
file = open('24-164.txt')
count = 0
for line in file:
    count += line.count('K')
print('K', count)
