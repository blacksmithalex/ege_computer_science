P = list(range(2, 22, 2))
Q = list(range(5, 55, 5))
A = list(range(1, 100))
for x in range(100):
    if (((x in A) <= (x in P)) and ((x in Q) <= (not (x in A)))) == 0:
        A.remove(x)
print(len(A))
