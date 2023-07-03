def F1(x, y, z, w):
    l1 = x or (not y)
    l2 = w == z
    return int(l1 <= l2)

def F2(x, y, z, w):
    l1 = x or (not y)
    l2 = z <= w
    return int(l1 == l2)

print('x y z w | F1| F2')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                print(x, y, z, w, '|', F1(x, y, z, w), '|', F2(x, y, z, w))