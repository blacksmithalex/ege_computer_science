for m in range(1, 40, 2):
    for n in range(0, 40, 2):
        N = 2 ** m * 7 ** n
        if 1e8 <= N <= 3 * 1e8:
            print(N, m + n)