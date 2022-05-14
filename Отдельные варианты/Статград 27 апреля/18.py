file = open('test.txt')
A = []
for line in file:
  A.append([int(x) for x in line.split()])
file.close()

F = [[0, 0] for _ in range(len(A))] #тут будет минималное количество топлива
moves = [[0, 0] for _ in range(len(A))] #тут будет количество ходов

F[0][0], F[0][1] = A[0][0], A[0][0] + A[0][1]
moves[0][0], moves[0][1] = 1, 2

for i in range(1, len(A)):
  for j in 0, 1:
    F[i][j] = F[i - 1][j] + A[i][j]
    moves[i][j] = moves[i - 1][j] + 1
  if F[i][0] + A[i][1] < F[i][1]:
    F[i][1] = F[i][0] + A[i][1]
    moves[i][1] = moves[i][0] + 1
  if F[i][1] + A[i][0] < F[i][0]:
    F[i][0] = F[i][1] + A[i][0]
    moves[i][0] = moves[i][1] + 1

print(F[-1][-1], moves[-1][-1])

#Ответ: 1832 47


