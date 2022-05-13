f = open('test.txt')
s = f.readline()
maxx = 0
count = 1
for i in range(1, len(s)):
    if ord(s[i-1]) > ord(s[i]):
        count += 1
        if maxx < count:
            maxx = count
    else:
        count = 1
print(maxx)