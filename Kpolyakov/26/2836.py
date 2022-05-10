file = open('26-k6.txt')
N, K = [int(x) for x in file.readline().split()]
goods = []
for _ in range(N):
    weight, price = [int(x) for x in file.readline().split()]
    goods.append([price / weight, weight, price])
file.close()
goods = sorted(goods)
last_relative_price = goods[:K][-1][0]
ind_first = [x[0] for x in goods[:K]].index(last_relative_price)

for i in range(ind_first, K):
    for j in range(K, N):
        if goods[i][0] != goods[j][0]:
            break
        if goods[i][1] < goods[j][1]:
            goods[i], goods[j] = goods[j], goods[i]

cur_goods = [x[1] for x in goods[:K]]
Sum_W, Max_W = sum(cur_goods), max(cur_goods)
Ind_Max_W = cur_goods.index(Max_W)
print(Sum_W, [x[2] for x in goods[:K]][Ind_Max_W])






