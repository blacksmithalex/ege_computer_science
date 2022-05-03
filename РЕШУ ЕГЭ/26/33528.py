file = open('26.txt')
N, M = [int(x) for x in file.readline().split()]
B, S =  [], 0
for _ in range(N):
    price, num, type = file.readline().split()
    if type == 'A':
        S += int(price) * int(num)
    else:
        B.append([int(price), int(num)])
file.close()
B = sorted(B)
if S <= M:
    print('OK')

countB = 0
for var in B:
    price, num = var
    for _ in range(num):
        if S + price <= M:
            S += price
            countB += 1
print(countB, M - S)
