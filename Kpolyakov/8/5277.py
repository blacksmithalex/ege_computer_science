from itertools import product
def f(a):
    return len(a) == len(set(a))

words = ['']
for v in product('АИКЛМЬ', repeat = 6):
    a = ''.join(v)
    words.append(a)

for v in product('АИКЛМЬ', repeat = 6):
    a = ''.join(v)
    na = words.index(a)
    nreva = words.index(a[::-1])
    if a[0] == 'К' and a[-1] == 'Ь' and f(a) and (abs(na - nreva) == 26655):
        print(a, words.index(a))