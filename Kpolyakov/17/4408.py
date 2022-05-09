def to7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]
def isPalindrome(a):
    return a == a[::-1]

file = open('17-10.txt')
a = [int(x) for x in file]
file.close()

count, res = 0, '1'
for i in range(len(a) - 1):
    s = to7((a[i] + a[i + 1]))
    if isPalindrome(s):
        count += 1
        if int(s, 7) > int(res, 7):
            res = s

print(count, res)



