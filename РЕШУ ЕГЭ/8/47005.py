from itertools import permutations
def f(a):
    glas = ['А', 'О']
    sogl = list('ПРБЛ')
    for i in range(len(a) - 1):
        if (a[i] in glas and a[i + 1] in glas) or (a[i] in sogl and a[i + 1] in sogl):
            return False
    return True

res = set()
for x in permutations('ПАРАБОЛА'):
    x = ''.join(x)
    if f(x):
        res.add(x)
print(len(res))
