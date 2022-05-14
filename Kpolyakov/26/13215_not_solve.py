file = open('test.txt')
N = int(file.readline())
incomes = sorted([int(x) for x in file])
file.close()

cost = sum(incomes) * 0.6
rich = incomes[-N // 5:]
poor = incomes[:-N // 5]
res = cost - sum(rich) * 0.8

poor_income = sum(poor)
rich_income = sum(rich)
l, r = 0, 100
while abs(res - poor_income * r) > 0.01:
    c = (l + r) / 2
    if res < poor_income * c / 100:
        r = c
    else:
        l = c
print(rich_income, incomes[0] * r / 100)




