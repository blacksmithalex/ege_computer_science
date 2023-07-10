def f(x, A):
    l1 = x & 28 != 0
    l2 = x & 45 != 0
    l3 = x & 17 == 0
    l4 = x & A != 0
    return (l1 or l2) <= (l3 <= l4)

for A in range(300):
    flag = True
    for x in range(300):
        if not f(x, A):
            flag = False
    if flag:
        print(A)
