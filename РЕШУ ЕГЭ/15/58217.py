def istriangle(a, b, c):
    l1 = a + b > c
    l2 = a + c > b
    l3 = b + c > a
    return l1 and l2 and l3
def f(x, A):
    l1 = istriangle(x, 11, 16) == (not (max(x, 5) > 10))
    l2 = istriangle(4, A, x)
    return not (l1 and l2)

for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        if not f(x, A):
            flag = False
    if flag:
        print(A)
