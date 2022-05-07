res = []
for i in range(10):
    for j in range(10):
        n = int('12345' + str(i) + '7' + str(j) + '8')
        if n % 23 == 0:
            res.append(n)

for x in res:
    print(x, x // 23)