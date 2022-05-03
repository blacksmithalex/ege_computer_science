variants = {}
variants[0] = [[0]]
variants[1] = [[1]]

for i in range(2, 5):
    newvar = []
    for j in range(i, 0, -1):
        localvar = []
        prev = variants[i - j]
        for v in prev:
            localvar.append(v + [j])
        newvar.append(localvar)
    newvar.append([[i]])
    variants[i] = newvar

print(variants[4])