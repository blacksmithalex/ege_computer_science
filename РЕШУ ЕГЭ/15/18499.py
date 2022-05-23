def f(m, n, A):
    return (2 * m + 3 * n > 40) or ((m < A) and (n <= A))

for A in range(100):
    flag = True
    for m in range(100):
        for n in range(100):
            if f(m, n, A) == False:
                flag = False
    if flag == True:
        print(A)

#Ответ: 21