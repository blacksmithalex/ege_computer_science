#980869 = 89 * 103 * 107
file = open('27-B.txt')
p89, p103, p107 = 0, 0, 0
count = 0
n = int(file.readline())
for i in range(1, n + 1):
    aj = int(file.readline())
    if aj % 89 == 0:
        p89 = i
    if aj % 103 == 0:
        p103 = i
    if aj % 107 == 0:
        p107 = i
    count += (i - min(p89, p103, p107))
print(count)
