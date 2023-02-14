from itertools import product

count = 0
for a in product('МЕЧТА', repeat = 6):
    if a.count('А') >= 3:
        count += 1
print(count)