def f(N):
    N = bin(N)[2:]
    if N.find('0') == 0:
        return -1
    ind = N.rfind('0')
    N = N[:ind] + N[:2] + N[ind + 1:]
    N = N[::-1]
    return int(N, 2)

for N in range(4, 1000):
    if f(N) == 119:
        print(N)

#Ответ: 58