def isFit(a, b, c, d):
    if a + b == c + d and (a + b) % 2 == 1:
        return True
    if a + c == b + d and (a + c) % 2 == 1:
        return True
    if a + d == b + c and (a + d) % 2 == 1:
        return True
    if b + c == a + d and (b + c) % 2 == 1:
        return True
    if b + d == a + c and (b + d) % 2 == 1:
        return True
    if c + d == a + b and (c + d) % 2 == 1:
        return True
    return False

file = open('test.txt')
count = 0
for line in file:
    a, b, c, d = [int(x) for x in line.split()]
    if isFit(a, b, c, d):
        count += 1
file.close()

print(count)
#Ответ: 54