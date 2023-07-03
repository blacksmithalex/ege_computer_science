from sys import setrecursionlimit
setrecursionlimit(100000)
def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + f(2 * n)
def g(n):
    return f(n) / n

g1000 = g(1000)
count = 0
for n in range(1, 1000000):
    if g(n) == g1000:
        count += 1
print(count)
