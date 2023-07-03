for i in range(1000000):
    n = bin(i)[2:]
    if i % 5 == 0:
        n = n + bin(5)[2:]
    else:
        n = n + '1'

    if int(n, 2) % 7 == 0:
        n = n + bin(7)[2:]
    else:
        n = n + '1'

    r = int(n, 2)
    if r < 1728404:
        print(i)