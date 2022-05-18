file = open('inf_22_10_20_24.txt')
count = 0
for a in file:
    if a.count('E') > a.count('A'):
        count += 1
print(count)