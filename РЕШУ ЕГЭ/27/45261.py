'''O(n^2)'''
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

'''O(n)'''
file = open('107_27_B.txt')
n = int(file.readline())
elems = [int(x) for x in file]
answers, sum = [0] * n, 0
file.close()

rightSum, leftSum = 0, 0
for i in range(1, n // 2):
  sum += elems[i] * i + elems[n - i] * i
  rightSum += elems[i]
  leftSum  += elems[n - i]
sum += elems[n // 2] * (n // 2)
answers[0] = sum

for i in range(1, n):
  answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + n // 2 - 1) % n];
  rightSum = rightSum - elems[i] + elems[(i + n // 2 - 1) % n]
  leftSum = leftSum - elems[(i + n // 2) % n] + elems[i - 1]
print(min(answers))
