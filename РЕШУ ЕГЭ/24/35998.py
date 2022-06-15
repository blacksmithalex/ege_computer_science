file = open('inf_26_04_21_24.txt')
mlen = 0
for line in file:
    if line.count('A') < 25:
        letters = set(line)
        for l in letters:
            dist = line.rfind(l) - line.find(l)
            if dist > mlen:
                mlen = dist
print(mlen)