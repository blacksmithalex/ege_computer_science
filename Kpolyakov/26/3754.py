file = open('26-42.txt')
N, S = [int(x) for x in file.readline().split()]
M, A = 0, []
for _ in range(N):
    type, price, num = file.readline().split()
    if type == 'Z':
        M += int(price) * int(num)
    else:
        A.append([int(price), int(num)])
file.close()
if M <= S:
    print('Все товары типа Z закупились')

A, countA = sorted(A), 0
for var in A:
    price, num = var
    for _ in range(num):
        if M + price <= S:
            M += price
            countA += 1
print(countA, S - M)