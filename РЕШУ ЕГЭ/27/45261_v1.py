def price(trash, finish, N):
    S = 0
    for i in range(N):
        S += 3 * min(abs(finish - i), N - abs(finish - i)) * trash[i]
    return S

file = open('107_27_A.txt')
N = int(file.readline())
trash = [int(x) for x in file]
file.close()

Mprice = 1e10
for finish in range(N):
    Mprice = min(price(trash, finish, N), Mprice)
print(Mprice)
