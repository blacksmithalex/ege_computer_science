def cmd1(n):
    return bin(int(n, 2) - 1)[2:]

def cmd2(n):
    return n[0] + '0' * len(n[1:])

def f(a, b):
    if int(a) < int(b):
        return 0
    if a == b:
        return 1
    else:
        if int(a[1:]) != 0:
            return f(cmd1(a), b) + f(cmd2(a), b)
        else:
            return f(cmd1(a), b)

print(f('1000000', '1000'))

