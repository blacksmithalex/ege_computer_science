def cmd1(b):
    b = int(b, 2)
    b -= 1
    return bin(b)[2:]

def cmd2(b):
    return b[0] + '0' * len(b[1:])

def num_of_p(a, b):
    if len(a) > len(b):
        return 0
    elif a == b:
        return 1
    else:
        if b[1:].count('1') != 0:
            return num_of_p(a, cmd1(b)) + num_of_p(a, cmd2(b))
        else:
            return num_of_p(a, cmd1(b))
print(num_of_p('100', '1100'))

