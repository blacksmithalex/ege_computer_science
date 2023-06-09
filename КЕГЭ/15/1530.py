def f(x, A):
    l1 = x & 94 != 0
    l2 = x & 21 == 0
    l3 = x & A != 0
    return l1 <= (l2 <= l3)

for A in range(100):
    flag = True
    for x in range(100):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)