def f(x, A):
    l1 = 120 % A == 0
    l2 = x % A != 0
    l3 = x % 18 == 0
    l4 = x % 24 != 0
    return l1 and (l2 <= (l3 <= l4))

for A in range(1, 200):
    flag = True
    for x in range(1, 200):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)