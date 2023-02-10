file = open('24.txt')
a = file.readline().split('E')
file.close()

count = 0
for line in a:
    if len(line) >= 10 and line.count('F') == 0:
        count += 1
print(count)
