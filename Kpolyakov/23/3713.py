def cmd1(a):
    return bin(int(a, 2) + 1)[2:]

def cmd2(a):
    return '1' + a

def f(a, b):
    if a == b:
        return 1
    elif int(a) > int(b):
        return 0
    else:
        return f(cmd1(a), b) + f(cmd2(a), b)

print(f('100', '110001'))