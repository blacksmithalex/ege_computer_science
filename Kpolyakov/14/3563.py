count = 0
for X in range(1, 1000):
    x16 = hex(X)[2:]
    x8 = oct(X)[2:]
    if len(x16) == 2 and len(x8) == 3:
        if x16[-1] == '5' and x8[-2] == '0':
            count += 1
print(count)

#Ответ: 3