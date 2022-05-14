file = open('26-k1.txt')
N, K = [int(x) for x in file.readline().split()]
a = sorted([int(x) for x in file])
file.close()
discount = int(sum(a[-K:]) * 0.2)
print(a[-K - 1], discount)