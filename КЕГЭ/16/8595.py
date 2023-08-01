from sys import setrecursionlimit
setrecursionlimit(3000)
def F(n):
    if n < 3:
        return 2
    else:
        return 2 * F(n - 2)

print(F(2222) / F(2182))