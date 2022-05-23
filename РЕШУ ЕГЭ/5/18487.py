def f(N):
    N = bin(N)[2:]
    return int(N[::-1], 2)

for N in range(1, 100):
    if f(N) == 13:
        print(N)

#Ответ: 88