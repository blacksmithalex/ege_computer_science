file = open('26.txt')
N, M = [int(x) for x in file.readline().split()]
S, A = 0, []
for _ in range(N):
    price, num, type = file.readline().split()
    if type == 'B':
        S += int(price) * int(num)
    else:
        A.append([int(price), int(num)])
file.close()
if S <= M:
    print('OK')

A = sorted(A)
countA = 0
for var in A:
    price, num = var
    for _ in range(num):
        if S + price <= M:
            S += price
            countA += 1

print(countA, M - S)
