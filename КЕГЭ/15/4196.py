def f(x, A):
    l1 = x % 3 == 0
    l2 = x % 5 != 0
    l3 = x + A >= 90
    return (l1 <= l2) or l3

for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)