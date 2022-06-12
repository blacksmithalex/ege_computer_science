def cmd1(b):
    b = '0' * (8 - len(b)) + b
    return b[1:] + '0'

def cmd2(b):
    b = bin(int(b, 2) - 1)[2:]
    return '0' * (8 - len(b)) + b

b = bin(91)[2:]
b = cmd1(b)
b = cmd1(b)
b = cmd2(b)
b = cmd1(b)
b = cmd1(b)
b = cmd2(b)

print(int(b, 2))



