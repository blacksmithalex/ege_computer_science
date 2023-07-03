def f(x, y):
    if x == y:
        return 1
    elif x > y or x == 11 or x == 15:
        return 0
    else:
        return f(x+1, y) + f(x*2, y) + f(x+3, y)

print(f(2, 8) * f(8, 20))