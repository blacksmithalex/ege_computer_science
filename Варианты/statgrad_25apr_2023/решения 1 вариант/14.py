for p in range(5, 10):
    for x in range(1, p):
        for y in range(0, p):
            p1 = int('12', p)
            p2 = int('34', p)
            p3 = int(str(x) + str(y) + '2', p)
            if p1 * p2 == p3:
                print(x, y, p)
                print(int(str(y) + str(x), p))

