def f(N):
    N = bin(N)[2:]
    for _ in range(3):
        count0, count1 = N.count('0'), N.count('1')
        if count0 == count1:
            N += N[-1]
        else:
            if count0 < count1:
                N += '0'
            else:
                N += '1'
    return int(N, 2)

for N in range(105, 200):
    if f(N) % 4 == 0:
        print(N)
        break