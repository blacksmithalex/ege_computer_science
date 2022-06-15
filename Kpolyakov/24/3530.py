file = open('24-153.txt')
s = file.readline()
file.close()
count = 0
for i in range(len(s) - 1):
    if s[i] == 'A':
        lst = [s[i]]
        while len(lst) != 10 and i != len(s) - 1:
            i += 1
            if s[i] == 'F' and 6 <= len(lst) <= 9:
                count += 1
            lst += [s[i]]
print(count)