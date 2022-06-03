file = open('24-164.txt')
Lmax = 0
for a in file:
    if a.count('G') < 15:
        letters = set(a)
        for l in letters:
            L = a.rfind(l) - a.find(l)
            if L > Lmax:
                Lmax = L
print(Lmax)
