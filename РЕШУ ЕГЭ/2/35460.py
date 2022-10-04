def f(x, y, z, w):
    l1 = (x or y) <= (z and w)
    l2 = x <= w
    return int((not l1) and l2)

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 1:
                    print(x, y, z, w, '|', f(x, y, z, w))
