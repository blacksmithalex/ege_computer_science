def f(x, y, z, w):
    l1 = not (y and (not x))
    l2 = not (x == z)
    return int(l1 and l2 and w)

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 1:
                    print(x, y, z, w, '|', f(x, y, z, w))