for s in range(10000):
    res = s
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(res)