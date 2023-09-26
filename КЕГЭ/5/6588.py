def f(N):
    bN = bin(N)[2:]
    bN = bN.replace('0', '*')
    bN = bN.replace('1', '0')
    bN = bN.replace('*', '1')
    bN = '1' + bN
    if bN.count('1') % 2 == 1:
        bN += '1'
    else:
        bN += '0'
    return int(bN, 2)

for N in range(1, 200):
    if f(N) > 180:
        print(N)
        break