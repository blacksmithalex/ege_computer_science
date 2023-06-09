def f(x, A):
    l1 = x % 13 == 0
    l2 = not (40 <= x <= 60)
    l3 = A < x + 20
    return (l1 <= l2) or l3

for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)