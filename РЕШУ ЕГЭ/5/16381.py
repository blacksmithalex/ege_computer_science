def f(N):
    bN = bin(N)[2:] #1
    bN = bN[:-1] #2
    if N % 2 == 1: #3
        bN += '10'
    else:
        bN += '01'
    return int(bN, 2) #4

for N in range(2, 2000):
    if f(N) == 2018:
        print(N)