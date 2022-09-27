def f(x, y, z, w):
    l1 = x == (not y)
    l2 = z == (y or w)
    return int(l1 <= l2)

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 0:
                    print(x, y, z, w, '|', f(x, y, z, w))