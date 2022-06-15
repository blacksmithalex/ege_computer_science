file = open('24.txt')
ml, mG = '', 1e16
for line in file:
    if line.count('G') < mG:
        ml, mG = line, line.count('G')
file.close()

for l in sorted(set(ml)):
    print(l, ml.count(l))


