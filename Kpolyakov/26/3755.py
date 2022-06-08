file = open('26-42.txt')
N, S = [int(x) for x in file.readline().split()]
M, Z = 0, []
for _ in range(N):
    type, price, num = file.readline().split()
    if type == 'A':
        M += int(price) * int(num)
    else:
        Z.append([int(price), int(num)])
file.close()
if M <= S:
    print('OK')

Z = sorted(Z)
countZ = 0
for var in Z:
    price, num = var[0], var[1]
    for _ in range(num):
        if M + price <= S:
            M += price
            countZ += 1
print(countZ, S - M)