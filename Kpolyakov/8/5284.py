from itertools import product

count = 0
b = 'ВОЛК'
for a in product('ПОЛЯКВ', repeat = 4):
    a = ''.join(a)
    n = 0
    for i in range(4):
        if a[i] == b[i]:
            n += 1
    if n == 2:
        count += 1
print(count)

