file = open('24.txt')
a = file.readline()
file.close()

parts = a.split('A')
ml = 0
for p in parts:
    if p.count('E') >= 3 and len(p) > ml:
        ml = len(p)
print(ml)