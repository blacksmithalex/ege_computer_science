file = open('24.txt')
countN, s = 1e16, ''
for a in file:
    if a.count('N') < countN:
        countN, s = a.count('N'), a
file.close()

for l in sorted(set(s)):
    print(l, s.count(l))
