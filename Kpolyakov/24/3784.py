def num_of_pairs(a):
    count = 0
    for i in range(len(a) - 1):
        if ord(a[i + 1]) - ord(a[i]) == 1:
            count += 1
    return count

file = open('24-s1.txt')
Mpairs, Ma = 0, ''
for a in file:
    num = num_of_pairs(a)
    if num >= Mpairs:
        Mpairs, Ma = num, a
file.close()

for x in sorted(set(Ma)):
    print(x, Ma.count(x))
print()
#реже всего встречается буква B
file = open('24-s1.txt')
countB = 0
for a in file:
    countB += a.count('B')

print('B', countB)



