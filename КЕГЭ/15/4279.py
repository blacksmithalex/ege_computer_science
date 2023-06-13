def f(x, A):
    l1 = x & 1097 == 0
    l2 = x & 2047 != 0
    l3 = x & A != 0
    return l1 <= (l2 <= l3)

for A in range(1000):
    flag = True
    for x in range(30000):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)