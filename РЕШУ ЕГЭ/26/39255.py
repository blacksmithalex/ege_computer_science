file = open('26.txt')
N, M = [int(x) for x in file.readline().split()]
A, B = [], []
for _ in range(N):
    price, type = file.readline().split()
    if type == 'A':
        A.append(int(price))
    else:
        B.append(int(price))
file.close()
A, B = sorted(A), sorted(B)
S, indA, indB = 0, 0, 0

while indA < len(A) and indB < len(B):
    if A[indA] < B[indB]:
        if S + A[indA] <= M:
            S += A[indA]
            indA += 1
        else:
            break
    else:
        if S + B[indB] <= M:
            S += B[indB]
            indB += 1
        else:
            break
if indB == len(B):
    while indA < len(A):
        if S + A[indA] <= M:
            S += A[indA]
            indA += 1
        else:
            break
if indA == len(A):
    while indB < len(B):
        if S + B[indB] <= M:
            S += B[indB]
            indB += 1
        else:
            break

indA -= 1
while indA >= 0 and indB < len(B):
    if S - A[indA] + B[indB] <= M:
        S = S - A[indA] + B[indB]
        indA -= 1
        indB += 1
    else:
        break

print(indB, M - S)



