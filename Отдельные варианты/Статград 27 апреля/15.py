def f(x, y, A):
    return (x**2 + y**2 < A) or (x > 3) or (y >= 5)

for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if f(x, y, A) == False:
                flag = False
    if flag == True:
        print(A)
        break

#Ответ: 26