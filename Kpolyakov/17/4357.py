file = open('17-7.txt')
a = [int(x) for x in file]
file.close()

def f(n):
    res = ''
    while n != 0:
        res += str(n % 8)
        n //= 8
    return res[::-1]

count, m = 0, 0
for x in a:
    to8 = f(x)
    if to8[-1] == '7' and to8[-2:] != '27':
        count += 1
        if x > m:
            m = x
print(count, m)