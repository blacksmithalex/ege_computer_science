def f(x, y, z):
    return int((x or y) <= (z == x))

print('x y z | f(x, y, z)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if f(x, y, z) == 0:
                print(x, y, z, '|', f(x, y, z))