def f(x, y, z, w):
    l1 = not (y <= x)
    l2 = z <= w
    l3 = not z
    return int(l1 or l2 or l3)

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 0:
                    print(x, y, z, w, '|', f(x, y, z, w))


