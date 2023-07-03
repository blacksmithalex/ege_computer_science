from itertools import permutations

n = 1
for x in permutations(sorted('ВИКТОР'), 6):
    print(n, ''.join(x))
    n += 1