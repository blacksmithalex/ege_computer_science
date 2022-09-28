def f(x, y, z, w):
    l1 = (not x) == z
    l2 = y == (w or x)
    return int(l1 <= l2)

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 0:
                    print(x, y, z, w, '|', f(x, y, z, w))
