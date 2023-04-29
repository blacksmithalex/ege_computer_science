def f(N):
    bN = bin(N)[2:]
    bN = '0' * (8 - len(bN)) + bN
    bN = bN.replace('0', 'X')
    bN = bN.replace('1', '0')
    bN = bN.replace('X', '1')
    return int(bN, 2) + 1

print(f(120))