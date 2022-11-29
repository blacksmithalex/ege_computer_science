def f(x, y, A):
    return ((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))

count = 0
for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if f(x, y, A) == False:
                flag = False
    if flag:
        count += 1
print(count)