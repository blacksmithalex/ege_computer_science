file = open('26-44.txt')
N = int(file.readline())
groups = [[] for _ in range(20)]
for _ in range(N):
    price = int(file.readline())
    groups[(price - 1) // 500].append(price)
file.close()

sale, mprice = 0, 0
for prices in groups:
    prices = sorted(prices)
    sale += sum(prices[:len(prices) // 2]) / 2
    mprice = prices[len(prices) // 2 - 1] / 2
print(int(sale), int(mprice))

