f = open('test.txt')
s = f.readlines()
maxl = 0
for a in s:
    if a.count('E') < 20:
        max = 0
        for l in set(a):
            diff = a.rfind(l) - a.find(l)
            if diff > max:
                max = diff
        if max > maxl:
            maxl = max
print(maxl)