#ДЕЛ(n, m):= n % m == 0
#¬ДЕЛ(n, m):= n % m != 0 или not (n % m == 0)
def f(x, A):
    l1 = A < 50
    l2 = x % A != 0
    l3 = x % 10 == 0
    l4 = x % 12 != 0
    return l1 and (l2 <= (l3 <= l4))

for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)