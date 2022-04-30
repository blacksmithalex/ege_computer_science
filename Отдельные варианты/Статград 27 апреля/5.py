def f(N):
    N = str(N)
    pairs = [int(N[i] + N[i + 1]) for i in range(len(N) - 1)]
    return max(pairs) - min(pairs)

for N in range(10, 1000):
    if f(N) == 44:
        print(N)
        break

#Ответ: 159