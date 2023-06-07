from math import ceil
def price(elems, finish, N):
    S = 0
    for i in range(N):
        x, num = elems[i]
        S += abs(finish - x) * num
    return S

file = open('27_A-2.txt')
N = int(file.readline())
elems = []
for _ in range(N):
    x, num = [int(x) for x in file.readline().split()]
    num = ceil(num / 36)
    elems.append([x, num])

Mprice = 1e10
for i in range(N):
    Mprice = min(Mprice, price(elems, elems[i][0], N))
print(Mprice)


