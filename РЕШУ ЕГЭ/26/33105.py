from math import ceil
file = open('inf_22_10_20_26.txt')
N = int(file.readline())
a, S = [], 0
for _ in range(N):
    price = int(file.readline())
    if price <= 100:
        S += price
    else:
        a.append(price)
file.close()
a, N = sorted(a), len(a)

S += sum(a[:len(a) // 2]) * 0.7
S += sum(a[len(a) // 2:])

print(ceil(S), a[len(a) // 2 - 1])
