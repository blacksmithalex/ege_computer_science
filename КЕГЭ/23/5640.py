def sum_of_digits(a):
    s = 0
    for x in str(a):
        s += int(x)
    return s

def f(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a - 4, b) + f(a - sum_of_digits(a), b)

print(f(36, 14) * f(14, 2))