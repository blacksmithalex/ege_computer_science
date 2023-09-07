ip = [192, 168, 32, 160]
mask = [255, 255, 255, 240]

for i in range(4):
    print('Часть', i)
    for part in range(256):
        if part & mask[i] == ip[i]:
            print(bin(part)[2:])