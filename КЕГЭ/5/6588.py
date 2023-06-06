def f(N):
    bN = bin(N)[2:]
    bN = bN.replace('1', 'A')
    bN = bN.replace('0', 'B')
    bN = bN.replace('A', '0')
    bN = bN.replace('B', '1')
    bN = '1' + bN
    count1 = bN.count('1')
    if count1 % 2 != 0:
        bN += '1'
    else:
        bN += '0'
    return int(bN, 2)

for N in range(1, 100):
    if f(N) > 180:
        print(N)
        break

